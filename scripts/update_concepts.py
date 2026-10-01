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
    (invisível quando renderizado);
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
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fix_frontmatter import get_field, parse_front_matter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

PREAMBLE_DEFAULT = (
    "# Key Concepts\n\n"
    "Reference notes synthesizing the core concepts needed to read this "
    "collection of papers.\n"
)
HEADING_RE = re.compile(r"^## +(.+?)\s*$")
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
    def __init__(self, title, body, sources=None, gen=None, has_meta=False):
        self.title = title
        self.body = body.strip()
        self.sources = list(sources or [])
        self.gen = gen
        self.has_meta = has_meta

    @property
    def edited(self):
        """True se o corpo não bate mais com o hash gravado (edição manual)."""
        return self.has_meta and self.gen != sha1(self.body)

    def render(self):
        meta = f"<!-- sources: {', '.join(self.sources)} | gen: {sha1(self.body)} -->"
        return f"## {self.title}\n{meta}\n{self.body}\n"


def parse_concepts(text: str):
    preamble, sections = [], []
    cur = None
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            cur = {"title": m.group(1), "lines": []}
            sections.append(cur)
        elif cur is None:
            preamble.append(line)
        else:
            cur["lines"].append(line)
    out = []
    for s in sections:
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
        out.append(Section(s["title"], "\n".join(lines), sources, gen, has_meta))
    return "\n".join(preamble).rstrip() + "\n", out


def write_concepts(path: Path, preamble: str, sections):
    parts = [preamble.rstrip() + "\n"] + [s.render() for s in sections]
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
    res = subprocess.run(shlex.split(cmd), input=prompt, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"LLM falhou ({res.returncode}): {res.stderr.strip()[:500]}")
    return res.stdout


def route_prompt(sections, paper: Paper) -> str:
    index = "\n".join(f"- {s.title}: {first_sentence(s.body)}" for s in sections) or "(vazio)"
    return f"""You maintain a glossary of key concepts for a collection of research papers.

EXISTING CONCEPTS (title: first sentence):
{index}

NEW PAPER SUMMARY — "{paper.title}":
{paper.body}

Decide which concepts this paper contributes to. For each relevant concept return:
- "match": the EXACT title of an existing concept, or null if the concept is new;
- "new_title": a short title for the concept when match is null, otherwise null;
- "excerpt": 1-3 neutral sentences stating what THIS paper says about the concept.
Prefer matching an existing concept over creating a new one. Only create a new
concept when the idea is a distinct, reusable concept that a reader of the field
would need explained. Skip purely paper-specific details.

Answer with JSON only: {{"concepts": [{{"match": ..., "new_title": ..., "excerpt": ...}}]}}"""


def merge_prompt(section: Section, paper: Paper, excerpt: str) -> str:
    return f"""Update one section of a concept glossary (neutral, extractive tone — explain what the field says, no personal opinion; same language and style as the current text).

CONCEPT: {section.title}

CURRENT TEXT:
{section.body}

NEW INFORMATION from the paper "{paper.title}":
{excerpt}

Rewrite the concept text so it incorporates the new information, keeping everything still valid and staying concise (one paragraph unless the current text already has more structure). Do not mention the paper by name unless it is essential. Output ONLY the new text, with no heading and no commentary."""


def create_prompt(title: str, paper: Paper, excerpt: str) -> str:
    return f"""Write one entry of a concept glossary for a collection of research papers (neutral, extractive tone — explain what the field says, no personal opinion; English; a single concise paragraph).

CONCEPT: {title}

INFORMATION from the paper "{paper.title}":
{excerpt}

Output ONLY the entry text, with no heading and no commentary."""


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


def propose(theme_dir: Path, title, text, paper: Paper):
    p = theme_dir / "concepts.proposed.md"
    prev = p.read_text(encoding="utf-8") if p.is_file() else "# Propostas de atualização (seções editadas à mão)\n"
    p.write_text(prev.rstrip() + f"\n\n## {title}\n<!-- proposta a partir de: {paper.slug} -->\n{text.strip()}\n",
                 encoding="utf-8")


def process_theme(theme_dir: Path, args):
    name = theme_dir.name
    concepts_path = theme_dir / "concepts.md"
    papers = list_papers(theme_dir)
    state = load_state(theme_dir)
    known = state["papers"]

    if concepts_path.is_file():
        preamble, sections = parse_concepts(concepts_path.read_text(encoding="utf-8"))
    else:
        preamble, sections = PREAMBLE_DEFAULT, []

    unadopted = [s for s in sections if not s.has_meta]

    # ---- consolidate (só relatório)
    if args.consolidate:
        if not args.llm_cmd:
            sys.exit("--consolidate precisa de --llm-cmd")
        print(f"{name}: sugestões de consolidação")
        print(json.dumps(extract_json(call_llm(args.llm_cmd, consolidate_prompt(sections))),
                         ensure_ascii=False, indent=1))
        return

    # ---- bootstrap
    if args.bootstrap:
        todo = [s for s in sections if not s.has_meta]
        print(f"{name}: bootstrap — {len(todo)} seção(ões) sem fontes, {len(papers)} resumo(s) a marcar")
        if not args.apply:
            print("  (dry-run — use --apply [--llm-cmd CMD])")
            return
        plist = [Paper(theme_dir, slug) for slug in papers]
        for s in todo:
            if args.llm_cmd:
                resp = extract_json(call_llm(args.llm_cmd, bootstrap_prompt(s, plist)))
                s.sources = [x for x in resp.get("sources", []) if x in papers]
            s.has_meta = True
            s.gen = sha1(s.body)
            print(f"  {s.title}: {len(s.sources)} fonte(s)")
        if sections:
            write_concepts(concepts_path, preamble, sections)
        for p in plist:
            known[p.slug] = p.hash
        save_state(theme_dir, state)
        print(f"  {len(plist)} resumo(s) marcados como incorporados")
        return

    # ---- pendências
    pending = [slug for slug, path in papers.items()
               if known.get(slug) != Paper(theme_dir, slug).hash]
    removed = [slug for slug in known if slug not in papers]

    if unadopted and pending:
        print(f"{name}: {len(unadopted)} seção(ões) de concepts.md sem comentário de fontes. "
              f"Rode antes: update_concepts.py {name} --bootstrap --apply [--llm-cmd CMD]")
        return

    if not pending and not removed:
        print(f"{name}: em dia ({len(papers)} resumos, {len(sections)} conceitos)")
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
            write_concepts(concepts_path, preamble, sections)
        save_state(theme_dir, state)
    for t in orphans:
        print(f"  ! '{t}' ficou sem fontes — candidata a remoção (não apagada)")

    # ---- incorporar pendentes, um a um (retomável)
    for slug in pending[:args.max_papers] if args.max_papers else pending:
        paper = Paper(theme_dir, slug)
        print(f"  roteando: {paper.title}")
        routes = extract_json(call_llm(args.llm_cmd, route_prompt(sections, paper))).get("concepts", [])
        for r in routes:
            excerpt = (r.get("excerpt") or "").strip()
            if not excerpt:
                continue
            target = find_section(sections, r["match"]) if r.get("match") else None
            if target is None:
                title = (r.get("new_title") or r.get("match") or "").strip()
                if not title:
                    continue
                target = find_section(sections, title)
                if target is None:
                    body = call_llm(args.llm_cmd, create_prompt(title, paper, excerpt)).strip()
                    sections.append(Section(title, body, [slug], sha1(body), True))
                    print(f"    novo: {title}")
                    continue
            new_body = call_llm(args.llm_cmd, merge_prompt(target, paper, excerpt)).strip()
            if target.edited:
                propose(theme_dir, target.title, new_body, paper)
                print(f"    editada à mão, proposta em concepts.proposed.md: {target.title}")
                continue
            target.body = new_body
            if slug not in target.sources:
                target.sources.append(slug)
            print(f"    atualizado: {target.title}")
        write_concepts(concepts_path, preamble, sections)
        known[slug] = paper.hash
        save_state(theme_dir, state)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("temas", nargs="*", help="pastas-tema (padrão: todas)")
    ap.add_argument("--apply", action="store_true", help="grava alterações (padrão: dry-run)")
    ap.add_argument("--llm-cmd", help='comando que lê o prompt no stdin e imprime a resposta (ex.: "claude -p")')
    ap.add_argument("--bootstrap", action="store_true", help="adota um concepts.md existente (preenche fontes)")
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
