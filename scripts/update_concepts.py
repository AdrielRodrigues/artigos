#!/usr/bin/env python3
"""Atualiza <tema>/concepts.md de forma incremental, só com os artigos novos.

Em vez de refazer o glossário inteiro, cada artigo cujo resumo ainda não foi
incorporado passa por duas etapas (cada uma é uma chamada ao LLM):
  1. Roteamento: dado o índice de conceitos já existentes (título + 1ª frase)
     e o resumo do artigo, diz quais conceitos o artigo toca e quais são novos.
  2. Fusão pontual: pra cada conceito existente tocado, reescreve só aquela
     seção incorporando o que o artigo diz; pra conceito novo, cria a seção.
As demais seções não são tocadas, então o diff no git mostra só o que mudou.

Rastreabilidade:
  - cada seção "## Conceito" leva, logo abaixo do título, um comentário
        <!-- sources: slug_a, slug_b | gen: <sha1 curto do corpo> -->
    (invisível quando renderizado) e, no fim, uma linha visível
        *Fontes: [Título](md/slug_summary.md); ...*
    com os artigos que sustentam o conceito;
  - <tema>/concepts.state.json guarda {"papers": {slug: sha1 do _summary.md}},
    ou seja, quais resumos já foram incorporados (e em que versão).

Edição manual é respeitada: se o corpo de uma seção não bate mais com o
hash "gen", o script não a sobrescreve — a versão proposta vai para
<tema>/concepts.proposed.md pra você revisar e colar à mão.

O LLM é plugável e roda sob demanda: --llm-cmd "<comando>" recebe o prompt
no stdin e deve escrever a resposta no stdout (ex.: --llm-cmd "claude -p").

Uso:
    python3 update_concepts.py [tema ...]                         # dry-run: lista pendências
    python3 update_concepts.py tema --apply --llm-cmd "claude -p"  # incorpora os pendentes
    python3 update_concepts.py tema --bootstrap [--apply] [--llm-cmd CMD]
        # adota um concepts.md antigo (sem comentários de fonte): preenche
        # "sources" de cada seção (via LLM, se dado) e marca todos os resumos
        # atuais como já incorporados. Rode uma vez por tema.
    python3 update_concepts.py tema --rebuild --apply --llm-cmd CMD
        # recomeça do zero: descarta as seções e o state (mantém a introdução)
        # e relê TODOS os resumos. Retomável: se for interrompido, rode o
        # comando normal (sem --rebuild) que ele continua de onde parou.
    python3 update_concepts.py tema --reorganize --apply --llm-cmd CMD [--structure-hint ARQ.md]
        # converte um concepts.md plano em hierárquico (tópicos "##" > subtópicos
        # "###"), mesclando duplicatas. Não relê artigos: reaproveita o texto e as
        # fontes atuais. --structure-hint aponta um .md cuja estrutura de títulos
        # serve de modelo (ex.: versão antiga tirada do git).
    python3 update_concepts.py tema --consolidate --llm-cmd CMD    # só sugere duplicatas

Tema sem concepts.md: criado do zero pelo mesmo caminho incremental.
Sem argumento de tema, processa todas as pastas com md/.
"""
import argparse
import hashlib
import json
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fix_frontmatter import get_field, parse_front_matter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

PREAMBLE_DEFAULT = (
    "# Key Concepts\n\n"
    "Reference notes synthesizing the core concepts needed to read this "
    "collection of papers.\n"
)
SOURCES_LINE_RE = re.compile(r"\n*\*Fontes:.*\*\s*$", re.S)
LLM_TIMEOUT = 900
LLM_RETRIES = 4
LLM_BACKOFF = (20, 60, 120, 240)  # segundos entre tentativas
HEADING_RE = re.compile(r"^## +(.+?)\s*$")
HEADING3_RE = re.compile(r"^### +(.+?)\s*$")
HIER_RE = re.compile(r"^### .*\n+<!--\s*sources:", re.M)  # "###" seguido do comentário de fontes
META_RE = re.compile(r"^<!--\s*sources:\s*(.*?)\s*\|\s*gen:\s*([0-9a-f]*)\s*-->\s*$")


# ---------------------------------------------------------------- utilidades

def sha1(text: str, n: int = 12) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:n]


def discover_themes(explicit):
    if explicit:
        # caminho que existe a partir do cwd vale como está; senão, nome de tema na raiz
        return [Path(e).resolve() if Path(e).is_dir() else ROOT / e for e in explicit]
    return [p for p in sorted(ROOT.iterdir())
            if p.is_dir() and not p.name.startswith(".") and (p / "md").is_dir()]


def clean_label(text: str) -> str:
    return re.sub(r"[\[\]\n]", " ", text).strip()


def first_sentence(text: str, limit: int = 220) -> str:
    flat = " ".join(text.split())
    m = re.search(r"(?<=[.!?])\s", flat)
    s = flat[:m.start()] if m else flat
    return s[:limit]


def extract_json(text: str):
    text = re.sub(r"```(?:json)?", "", text)
    for open_c, close_c in (("{", "}"), ("[", "]")):
        i, j = text.find(open_c), text.rfind(close_c)
        if i != -1 and j > i:
            try:
                return json.loads(text[i:j + 1])
            except json.JSONDecodeError:
                continue
    raise ValueError("resposta do LLM sem JSON válido:\n" + text[:500])


# ---------------------------------------------------------- concepts.md / state

class Section:
    def __init__(self, title, body, sources=None, gen=None, has_meta=False, group=None):
        self.group = group  # tópico ("##") quando o arquivo é hierárquico; None = arquivo plano
        self.title = title
        self.body = body.strip()
        self.sources = list(sources or [])
        self.gen = gen
        self.has_meta = has_meta

    @property
    def edited(self):
        """True se o corpo não bate mais com o hash gravado (edição manual)."""
        return self.has_meta and self.gen != sha1(self.body)

    def render(self, titles=None, level=2):
        titles = titles or {}
        meta = f"<!-- sources: {', '.join(self.sources)} | gen: {sha1(self.body)} -->"
        out = f"{'#' * level} {self.title}\n{meta}\n{self.body}\n"
        if self.sources:
            links = "; ".join(
                f"[{clean_label(titles.get(s, s))}](md/{s}_summary.md)" for s in self.sources)
            out += f"\n*Fontes: {links}*\n"
        return out


def parse_concepts(text: str):
    """Devolve (preâmbulo, seções). Arquivo plano: cada "## X" é uma seção.
    Arquivo hierárquico (há "### X" seguido de comentário de fontes): "## X" é
    um tópico (Section.group das seções abaixo) e cada "### X" é uma seção."""
    hier = bool(HIER_RE.search(text))
    preamble, raw = [], []
    cur, group = None, None
    for line in text.splitlines():
        m2 = HEADING_RE.match(line)
        m3 = HEADING3_RE.match(line) if hier else None
        if m3:
            cur = {"title": m3.group(1), "lines": [], "group": group}
            raw.append(cur)
        elif m2:
            if hier:
                group, cur = m2.group(1), None  # texto solto sob o tópico é descartado
            else:
                cur = {"title": m2.group(1), "lines": [], "group": None}
                raw.append(cur)
        elif cur is None:
            if not hier or group is None:
                preamble.append(line)
        else:
            cur["lines"].append(line)
    out = []
    for s in raw:
        lines = s["lines"]
        while lines and not lines[0].strip():
            lines = lines[1:]
        sources, gen, has_meta = [], None, False
        if lines:
            mm = META_RE.match(lines[0])
            if mm:
                sources = [x.strip() for x in mm.group(1).split(",") if x.strip()]
                gen, has_meta = mm.group(2) or None, True
                lines = lines[1:]
        body = SOURCES_LINE_RE.sub("", "\n".join(lines))
        out.append(Section(s["title"], body, sources, gen, has_meta, s["group"]))
    return "\n".join(preamble).rstrip() + "\n", out


def write_concepts(path: Path, preamble: str, sections, titles=None):
    if any(s.group for s in sections):
        # hierárquico: tópicos na ordem da primeira aparição, seções agrupadas sob cada um
        order = []
        for s in sections:
            g = s.group or "Outros"
            if g not in order:
                order.append(g)
        parts = [preamble.rstrip() + "\n"]
        for g in order:
            parts.append(f"## {g}\n")
            parts += [s.render(titles, level=3) for s in sections if (s.group or "Outros") == g]
    else:
        parts = [preamble.rstrip() + "\n"] + [s.render(titles) for s in sections]
    path.write_text("\n".join(parts), encoding="utf-8")


def load_state(theme_dir: Path):
    p = theme_dir / "concepts.state.json"
    if p.is_file():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"papers": {}}


def save_state(theme_dir: Path, state):
    (theme_dir / "concepts.state.json").write_text(
        json.dumps(state, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")


# ----------------------------------------------------------------- resumos

class Paper:
    def __init__(self, theme_dir: Path, slug: str):
        self.slug = slug
        self.summary_path = theme_dir / "md" / f"{slug}_summary.md"
        raw = self.summary_path.read_text(encoding="utf-8")
        self.hash = sha1(raw, 16)
        fm, self.body = parse_front_matter(raw)
        self.index_terms = self._index_terms(fm)
        md_path = theme_dir / "md" / f"{slug}.md"
        title = None
        if md_path.is_file():
            md_fm, _ = parse_front_matter(md_path.read_text(encoding="utf-8"))
            title = get_field(md_fm, "title")
        self.title = (title or slug).strip().strip('"')

    @staticmethod
    def _index_terms(fm):
        if not fm:
            return []
        terms, on = [], False
        for line in fm.splitlines():
            if line.strip().startswith("index_terms"):
                on = True
            elif on and line.strip().startswith("- "):
                terms.append(line.strip()[2:].strip())
            elif on and line.strip():
                break
        return terms

    def compact(self, n_chars=400):
        terms = "; ".join(self.index_terms)
        return f"- {self.slug} | {self.title} | {terms} | {' '.join(self.body.split())[:n_chars]}"


def list_papers(theme_dir: Path):
    return {p.name[:-len("_summary.md")]: p
            for p in sorted((theme_dir / "md").glob("*_summary.md"))}


# --------------------------------------------------------------------- LLM

def call_llm(cmd: str, prompt: str) -> str:
    last = None
    for attempt in range(1 + LLM_RETRIES):
        try:
            res = subprocess.run(shlex.split(cmd), input=prompt, capture_output=True,
                                 text=True, timeout=LLM_TIMEOUT)
            if res.returncode == 0 and res.stdout.strip():
                return res.stdout
            detail = (res.stderr.strip() or res.stdout.strip())[:300]
            last = f"código {res.returncode}: {detail}"
        except subprocess.TimeoutExpired:
            last = "timeout"
        wait = LLM_BACKOFF[min(attempt, len(LLM_BACKOFF) - 1)]
        print(f"    (LLM: tentativa {attempt + 1} falhou — {last}; nova tentativa em {wait}s)", flush=True)
        if attempt < LLM_RETRIES:
            time.sleep(wait)
    raise RuntimeError(f"LLM falhou após {1 + LLM_RETRIES} tentativas: {last}")


def call_json(cmd: str, prompt: str):
    """Chama o LLM e extrai JSON; repete a chamada se a resposta não for JSON válido."""
    last = None
    for attempt in range(1 + LLM_RETRIES):
        try:
            return extract_json(call_llm(cmd, prompt))
        except ValueError as e:
            last = e
            print(f"    (resposta sem JSON válido, tentativa {attempt + 1})", flush=True)
    raise RuntimeError(str(last))


def route_prompt(sections, paper: Paper) -> str:
    hier = any(s.group for s in sections)
    if hier:
        groups = {}
        for s in sections:
            groups.setdefault(s.group or "Outros", []).append(s)
        index = "\n".join(
            f"[TOPIC] {g}\n" + "\n".join(f"  - {s.title}: {first_sentence(s.body, 160)}" for s in ss)
            for g, ss in groups.items())
    else:
        index = "\n".join(f"- {s.title}: {first_sentence(s.body)}" for s in sections) or "(vazio)"
    group_field = (
        '\n- "group": for a NEW concept, the EXACT title of the existing [TOPIC] it belongs under '
        '(or a new topic title if none fits); null for existing concepts.' if hier else "")
    group_json = ', "group": ...' if hier else ""
    return f"""You maintain a glossary of key concepts for a collection of research papers.

EXISTING CONCEPTS (title: first sentence):
{index}

NEW PAPER SUMMARY — "{paper.title}":
{paper.body}

Decide which glossary entries this paper contributes to. For each relevant concept return:
- "match": the EXACT title of an existing concept, or null if the concept is new;
- "new_title": a short, specific title for the concept when match is null, otherwise null;
- "focus": one sentence on what THIS paper adds about the concept (a pointer for the editor, not the final text).{group_field}
Prefer matching an existing concept over creating a new one. Create a new concept only for a distinct,
reusable idea (technology, architecture, algorithm family, metric, standard, open problem) that a reader of
the field would need explained; skip details that only matter inside this single paper. A typical paper
touches 3-8 concepts.

Answer with JSON only: {{"concepts": [{{"match": ..., "new_title": ..., "focus": ...{group_json}}}]}}"""


def merge_prompt(targets, paper: Paper, style) -> str:
    """targets: lista de (Section existente | None, título, focus)."""
    blocks = []
    for sec, title, focus in targets:
        cur = sec.body if sec else "(new entry — write it from scratch)"
        blocks.append(f"### {title}\nFOCUS: {focus}\nCURRENT TEXT:\n{cur}")
    style_txt = "\n\n".join(f"{s.title}\n{s.body[:900]}" for s in style) or "(none)"
    return f"""You are editing a concept glossary (neutral, extractive tone: explain what the field says, no personal opinion; English).

STYLE EXAMPLES (match this level of detail and tone — one dense paragraph per concept, concrete facts such as numbers, standards, method names):
{style_txt}

PAPER SUMMARY — "{paper.title}":
{paper.body}

ENTRIES TO WRITE OR UPDATE:
{chr(10).join(blocks)}

For each entry, return the complete new text. For an existing entry, keep everything still valid and weave in
what this paper adds. For a new entry, write it from the paper. Keep the text self-contained and do not cite
the paper by name unless essential. Do not include headings or source lines in the text.

Answer with JSON only: {{"sections": [{{"title": "<exact title as given above>", "body": "<text>"}}]}}"""


def intro_prompt(sections, titles) -> str:
    cs = "; ".join(s.title for s in sections[:80])
    ps = "\n".join(f"- {t}" for t in list(titles.values())[:60])
    return f"""Write the introduction line of a concept glossary. Format: one sentence starting exactly with
"Reference notes synthesizing the core concepts needed to read this collection of papers on" followed by a
comma-separated list of the collection's main topics. Output only that sentence.

PAPERS:
{ps}

CONCEPTS: {cs}"""


def bootstrap_prompt(section: Section, papers) -> str:
    cat = "\n".join(p.compact() for p in papers)
    return f"""Below is one entry of a concept glossary and the list of paper summaries (slug | title | index terms | opening of the summary) the glossary was built from.
Which papers does this entry draw on? Return only papers that clearly discuss the concept.

CONCEPT: {section.title}

ENTRY:
{section.body}

PAPERS:
{cat}

Answer with JSON only: {{"sources": ["slug", ...]}}  (slugs exactly as listed)"""


def reorganize_prompt(sections, hint: str) -> str:
    idx = "\n".join(f"- {s.title}: {first_sentence(s.body, 200)}" for s in sections)
    hint_txt = hint.strip() or "(none)"
    return f"""You are organizing a flat concept glossary into a two-level hierarchy: topics (broad areas) containing subtopics (the individual concepts).

CURRENT ENTRIES (title: first sentence):
{idx}

PREFERRED STRUCTURE (headings of a previous version the reader liked: "##" = topic, "###" = subtopic). Reuse these topic and subtopic titles, and their logical order, wherever the content fits; add or rename topics only when needed:
{hint_txt}

Rules:
- Assign EVERY current entry to exactly one subtopic; never drop an entry.
- Use roughly 8-16 topics. Order topics and subtopics logically (foundations first, then technologies, then control/AI, then cross-cutting issues).
- You may merge entries that are duplicates or near-duplicates into one subtopic (list all of them in "from"); only merge when they genuinely describe the same idea.
- You may rename a subtopic for clarity; prefer the preferred-structure title when the content matches.
- "from" must contain exact current entry titles.

Answer with JSON only: {{"topics": [{{"title": "...", "subtopics": [{{"title": "...", "from": ["exact current title", ...]}}]}}]}}"""


def merge_entries_prompt(title, entries) -> str:
    blocks = "\n\n".join(f"ENTRY: {s.title}\n{s.body}" for s in entries)
    return f"""Merge these glossary entries into ONE entry titled "{title}". Keep every distinct fact (numbers, standards, method names, caveats), remove repetition, neutral extractive tone, English. Use one dense paragraph, or two if the content is long. Output ONLY the merged text, with no heading and no commentary.

{blocks}"""


def consolidate_prompt(sections) -> str:
    idx = "\n".join(f"- {s.title}: {first_sentence(s.body)}" for s in sections)
    return f"""Review this concept glossary for redundancy. Identify groups of entries that are duplicates or near-duplicates and should be merged, and entries whose title could be clearer.

ENTRIES:
{idx}

Answer with JSON only: {{"merge": [{{"titles": ["A", "B"], "into": "Suggested title", "why": "..."}}], "rename": [{{"from": "...", "to": "...", "why": "..."}}]}}"""


# ------------------------------------------------------------------ operações

def find_section(sections, title):
    for s in sections:
        if s.title == title:
            return s
    low = title.strip().lower()
    for s in sections:
        if s.title.strip().lower() == low:
            return s
    return None


def pick_group(sections, wanted):
    """Tópico existente que casa com `wanted` (sem diferenciar maiúsculas); senão, o próprio `wanted`
    como tópico novo; sem sugestão, o tópico da última seção."""
    existing = []
    for s in sections:
        g = s.group or "Outros"
        if g not in existing:
            existing.append(g)
    if wanted:
        for g in existing:
            if g.strip().lower() == wanted.strip().lower():
                return g
        return wanted.strip()
    return existing[-1] if existing else "Outros"


def reorganize(theme_dir, preamble, sections, titles, args):
    concepts_path = theme_dir / "concepts.md"
    if any(s.group for s in sections):
        sys.exit(f"{theme_dir.name}: concepts.md já é hierárquico")
    if any(not s.has_meta for s in sections):
        sys.exit(f"{theme_dir.name}: há seções sem comentário de fontes — rode --bootstrap antes")
    if not (args.apply and args.llm_cmd):
        sys.exit("--reorganize precisa de --apply e --llm-cmd")
    hint = ""
    if args.structure_hint:
        hint = "\n".join(l for l in Path(args.structure_hint).read_text(encoding="utf-8").splitlines()
                         if l.startswith("## ") or l.startswith("### "))
    print(f"{theme_dir.name}: reorganizando {len(sections)} conceito(s) em tópicos/subtópicos")
    plan = call_json(args.llm_cmd, reorganize_prompt(sections, hint)).get("topics", [])

    by_title = {s.title.strip().lower(): s for s in sections}
    used, out, used_titles = set(), [], set()
    for topic in plan:
        gtitle = (topic.get("title") or "").strip()
        for sub in topic.get("subtopics", []):
            srcs = []
            for ft in sub.get("from", []):
                key = ft.strip().lower()
                if key in by_title and key not in used:
                    used.add(key)
                    srcs.append(by_title[key])
            if not gtitle or not srcs:
                continue
            title = (sub.get("title") or srcs[0].title).strip()
            if title.lower() in used_titles:
                title = f"{title} ({gtitle})"
            used_titles.add(title.lower())
            if len(srcs) == 1:
                body = srcs[0].body
                merged = False
            else:
                print(f"  mesclando {len(srcs)} em: {title}", flush=True)
                if any(s.edited for s in srcs):
                    print("    (aviso: uma das seções foi editada à mão; o texto mesclado a absorve)")
                body = call_llm(args.llm_cmd, merge_entries_prompt(title, srcs)).strip()
                merged = True
            sources = []
            for s in srcs:
                for x in s.sources:
                    if x not in sources:
                        sources.append(x)
            out.append(Section(title, body, sources, sha1(body), True, gtitle))
    leftover = [s for k, s in by_title.items() if k not in used]
    for s in leftover:
        print(f"  ! não atribuída pelo LLM, mantida em 'Outros': {s.title}")
        out.append(Section(s.title, s.body, s.sources, s.gen, True, "Outros"))
    write_concepts(concepts_path, preamble, out, titles)
    n_topics = len({s.group for s in out})
    print(f"  {len(out)} subtópico(s) em {n_topics} tópico(s) (de {len(sections)} conceitos planos)")


def propose(theme_dir: Path, title, text, paper: Paper):
    p = theme_dir / "concepts.proposed.md"
    prev = p.read_text(encoding="utf-8") if p.is_file() else "# Propostas de atualização (seções editadas à mão)\n"
    p.write_text(prev.rstrip() + f"\n\n## {title}\n<!-- proposta a partir de: {paper.slug} -->\n{text.strip()}\n",
                 encoding="utf-8")


def process_theme(theme_dir: Path, args):
    name = theme_dir.name
    concepts_path = theme_dir / "concepts.md"
    summary_files = list_papers(theme_dir)
    plist = {slug: Paper(theme_dir, slug) for slug in summary_files}
    titles = {slug: p.title for slug, p in plist.items()}
    state = load_state(theme_dir)
    known = state["papers"]

    if concepts_path.is_file():
        preamble, sections = parse_concepts(concepts_path.read_text(encoding="utf-8"))
    else:
        preamble, sections = PREAMBLE_DEFAULT, []

    # ---- rebuild: descarta seções e state (mantém a introdução), relê tudo
    style = [s for s in sections if s.body][:2]
    if args.rebuild:
        if not (args.apply and args.llm_cmd):
            sys.exit("--rebuild precisa de --apply e --llm-cmd")
        print(f"{name}: rebuild — descartando {len(sections)} seção(ões) e {len(known)} marca(s); "
              f"relendo {len(plist)} resumo(s)")
        sections, known = [], {}
        state["papers"] = known
        write_concepts(concepts_path, preamble, sections, titles)
        save_state(theme_dir, state)

    unadopted = [s for s in sections if not s.has_meta]
    if not style:
        style = sections[:2]

    # ---- reorganize (plano -> hierárquico)
    if args.reorganize:
        reorganize(theme_dir, preamble, sections, titles, args)
        return

    # ---- consolidate (só relatório)
    if args.consolidate:
        if not args.llm_cmd:
            sys.exit("--consolidate precisa de --llm-cmd")
        print(f"{name}: sugestões de consolidação")
        print(json.dumps(call_json(args.llm_cmd, consolidate_prompt(sections)),
                         ensure_ascii=False, indent=1))
        return

    # ---- bootstrap
    if args.bootstrap:
        todo = [s for s in sections if not s.has_meta]
        print(f"{name}: bootstrap — {len(todo)} seção(ões) sem fontes, {len(plist)} resumo(s) a marcar")
        if not args.apply:
            print("  (dry-run — use --apply [--llm-cmd CMD])")
            return
        for s in todo:
            if args.llm_cmd:
                resp = call_json(args.llm_cmd, bootstrap_prompt(s, list(plist.values())))
                s.sources = [x for x in resp.get("sources", []) if x in plist]
            s.has_meta = True
            s.gen = sha1(s.body)
            print(f"  {s.title}: {len(s.sources)} fonte(s)")
        if sections:
            write_concepts(concepts_path, preamble, sections, titles)
        for slug, p in plist.items():
            known[slug] = p.hash
        save_state(theme_dir, state)
        print(f"  {len(plist)} resumo(s) marcados como incorporados")
        return

    # ---- pendências
    pending = [slug for slug, p in plist.items() if known.get(slug) != p.hash]
    removed = [slug for slug in known if slug not in plist]

    if unadopted and pending:
        print(f"{name}: {len(unadopted)} seção(ões) de concepts.md sem comentário de fontes. "
              f"Rode antes: update_concepts.py {name} --bootstrap --apply [--llm-cmd CMD] "
              f"(ou --rebuild pra refazer do zero)")
        return

    if not pending and not removed:
        print(f"{name}: em dia ({len(plist)} resumos, {len(sections)} conceitos)")
        return

    print(f"{name}: {len(pending)} resumo(s) pendente(s), {len(removed)} removido(s)")
    for slug in pending:
        print(f"  + {slug}")
    for slug in removed:
        print(f"  - {slug} (resumo não existe mais)")
    if not args.apply:
        print("  (dry-run — use --apply --llm-cmd CMD)")
        return
    if pending and not args.llm_cmd:
        sys.exit("--apply com resumos pendentes precisa de --llm-cmd")

    # ---- resumos removidos: tira o slug das fontes, só avisa sobre órfãs
    orphans = []
    for slug in removed:
        for s in sections:
            if slug in s.sources:
                s.sources.remove(slug)
                if not s.sources:
                    orphans.append(s.title)
        del known[slug]
    if removed:
        if sections:
            write_concepts(concepts_path, preamble, sections, titles)
        save_state(theme_dir, state)
    for t in orphans:
        print(f"  ! '{t}' ficou sem fontes — candidata a remoção (não apagada)")

    # ---- incorporar pendentes, um a um (retomável)
    batch = pending[:args.max_papers] if args.max_papers else pending
    for n, slug in enumerate(batch, 1):
        paper = plist[slug]
        print(f"  [{n}/{len(batch)}] {paper.title}", flush=True)
        routes = call_json(args.llm_cmd, route_prompt(sections, paper)).get("concepts", [])

        targets, seen, groups_of = [], set(), {}  # targets: (Section|None, título, focus)
        for r in routes:
            focus = (r.get("focus") or r.get("excerpt") or "").strip()
            sec = find_section(sections, r["match"]) if r.get("match") else None
            title = sec.title if sec else (r.get("new_title") or r.get("match") or "").strip()
            if not title or title.lower() in seen:
                continue
            if sec is None:
                sec = find_section(sections, title)
                title = sec.title if sec else title
            seen.add(title.lower())
            if sec is None and r.get("group"):
                groups_of[title.lower()] = r["group"]
            targets.append((sec, title, focus or "(see paper summary)"))
        if not targets:
            print("    (nenhum conceito relevante)")
        else:
            by_title = {}
            for attempt in range(1 + LLM_RETRIES):
                resp = call_json(args.llm_cmd, merge_prompt(targets, paper, style))
                by_title = {s["title"].strip().lower(): s["body"].strip()
                            for s in resp.get("sections", []) if s.get("title") and s.get("body")}
                missing = [t for _, t, _ in targets if t.lower() not in by_title]
                if not missing:
                    break
                print(f"    (LLM não devolveu {len(missing)} seção(ões), tentativa {attempt + 1})", flush=True)
            for sec, title, _ in targets:
                if title.lower() not in by_title:
                    print(f"    ! PULADO (LLM não devolveu): {title}")
                    continue
                body = by_title[title.lower()]
                if sec is None:
                    grp = None
                    if any(s.group for s in sections):
                        grp = pick_group(sections, groups_of.get(title.lower()))
                    sections.append(Section(title, body, [slug], sha1(body), True, grp))
                    print(f"    novo: {title}" + (f"  [{grp}]" if grp else ""))
                elif sec.edited:
                    propose(theme_dir, sec.title, body, paper)
                    print(f"    editada à mão, proposta em concepts.proposed.md: {sec.title}")
                else:
                    sec.body = body.strip()
                    sec.gen = sha1(sec.body)  # sem isso a próxima atualização acharia que foi edição manual
                    if slug not in sec.sources:
                        sec.sources.append(slug)
                    print(f"    atualizado: {sec.title}")
        if not style:
            style = sections[:2]
        write_concepts(concepts_path, preamble, sections, titles)
        known[slug] = paper.hash
        save_state(theme_dir, state)

    # ---- introdução (só pra tema novo, ainda com a introdução padrão)
    if batch == pending and sections and preamble.strip() == PREAMBLE_DEFAULT.strip():
        line = call_llm(args.llm_cmd, intro_prompt(sections, titles)).strip().splitlines()[0]
        preamble = "# Key Concepts\n\n" + line.strip() + "\n"
        write_concepts(concepts_path, preamble, sections, titles)
        print("  introdução gerada")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("temas", nargs="*", help="pastas-tema (padrão: todas)")
    ap.add_argument("--apply", action="store_true", help="grava alterações (padrão: dry-run)")
    ap.add_argument("--llm-cmd", help='comando que lê o prompt no stdin e imprime a resposta (ex.: "claude -p")')
    ap.add_argument("--bootstrap", action="store_true", help="adota um concepts.md existente (preenche fontes)")
    ap.add_argument("--rebuild", action="store_true",
                    help="descarta seções e state e relê todos os resumos (mantém a introdução)")
    ap.add_argument("--reorganize", action="store_true",
                    help="converte concepts.md plano em tópicos/subtópicos (sem reler artigos)")
    ap.add_argument("--structure-hint", help="arquivo .md cuja estrutura de títulos serve de modelo")
    ap.add_argument("--consolidate", action="store_true", help="sugere fusões/renomeações (não grava)")
    ap.add_argument("--max-papers", type=int, default=0, help="limita quantos resumos incorporar nesta execução")
    args = ap.parse_args()

    themes = discover_themes(args.temas)
    if not themes:
        sys.exit("nenhuma pasta-tema encontrada")
    for theme_dir in themes:
        if not (theme_dir / "md").is_dir():
            print(f"{theme_dir.name}: sem md/, ignorado")
            continue
        process_theme(theme_dir, args)


if __name__ == "__main__":
    main()
