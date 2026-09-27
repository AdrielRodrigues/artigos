#!/usr/bin/env python3
"""Padroniza o front matter de todo md/<nome>.md (texto completo do artigo).

Campos mantidos: title, tema_principal, temas_relacionados, ano, autores,
veiculo, pdf.

O campo "status" é removido caso exista — desde que texto/resumo passaram
a ser rastreados como pendente/ok em summary.md, esse campo por arquivo
ficava redundante e podia dessincronizar.

Regras por campo:
  title              mantém o que já houver, a menos que pareça um
                      masthead de revista salvo por engano (bug de versão
                      antiga); nesse caso, ou se o arquivo não tiver front
                      matter, usa o primeiro "# Título" do corpo que não
                      seja masthead/rótulo de seção.
  tema_principal      nome da pasta-tema onde o arquivo está (sempre
                      recalculado — reflete onde o arquivo mora agora).
  temas_relacionados  mantém o que já houver; senão fica [].
  ano                 mantém o que já houver (nunca sobrescreve correção
                      manual); senão tenta detectar via copyright/received-
                      accepted/arXiv id no corpo; senão fica null e o
                      arquivo entra no relatório de revisão manual.
  autores             mantém o que já houver; senão fica [] — não há
                      tentativa de detecção automática (nomes são difícil
                      de extrair de forma confiável; um campo vazio e
                      visível é melhor que um dado errado e silencioso).
                      Preencher à mão.
  veiculo             mantém o que já houver; senão tenta detectar a
                      partir do cabeçalho de masthead (nome da revista/
                      conferência que o parser de title já identifica e
                      descarta); senão fica null.
  pdf                 sempre recalculado como ../pdf/<nome>.pdf.

Arquivos ignorados: concepts.md e *_summary.md (não são o texto completo
de um artigo).

Uso:
    python3 fix_frontmatter.py [pasta-tema ...] [--apply]

Sem argumentos, processa todas as pastas-tema (qualquer subpasta de
artigos/ com md/ e pdf/). Sem --apply roda em modo dry-run.
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURRENT_YEAR = datetime.date.today().year


def discover_theme_dirs(explicit):
    if explicit:
        return [Path(e) for e in explicit]
    dirs = []
    for p in sorted(ROOT.iterdir()):
        if p.is_dir() and (p / "md").is_dir() and (p / "pdf").is_dir():
            dirs.append(p)
    return dirs


def parse_front_matter(text: str):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[4:end], text[end + 5:]
    return None, text


def get_field(fm_block, key):
    if fm_block is None:
        return None
    m = re.search(rf'^{key}:\s*(.*)$', fm_block, re.M)
    return m.group(1).strip() if m else None


# Cabeçalhos de masthead de revista (ex.: "Contents lists available at
# ScienceDirect" / "journal homepage: ...") acabam virando um H1 com o nome
# da revista (ex.: "# Optical Fiber Technology") antes do título de verdade.
MASTHEAD_HINT_RE = re.compile(r'contents lists available at|journal homepage', re.I)
# Rótulos de seção que também aparecem como H1/H2 antes do título de verdade.
SECTION_LABEL_RE = re.compile(
    r'^(regular articles?|research articles?|review( article)?|tutorial|'
    r'invited paper|short communication|technical note|letter to (the )?editor)$',
    re.I,
)


def heading_lines(body: str):
    return body.splitlines()[:40]


def is_masthead_heading(text: str, idx: int, lines):
    if SECTION_LABEL_RE.match(text.strip()):
        return True
    neighborhood = " ".join(lines[max(0, idx - 2):idx] + lines[idx + 1:idx + 3])
    return bool(MASTHEAD_HINT_RE.search(neighborhood))


# Cabeçalhos genéricos que a extração às vezes gera quando o título de
# verdade não sobrevive (ex.: um "# Article" de template de revista) — se
# vier assim, é melhor tratar como "sem título" do que salvar o genérico.
GENERIC_TITLE_RE = re.compile(
    r'^(article|paper|title|untitled|abstract|original article)$', re.I,
)


def is_generic_placeholder_title(text: str) -> bool:
    return bool(GENERIC_TITLE_RE.match(text.strip()))


def is_bad_title_heading(text: str, idx: int, lines) -> bool:
    return is_masthead_heading(text, idx, lines) or is_generic_placeholder_title(text)


# Marcadores de ênfase markdown (**negrito**, *itálico*, __sub__) que às
# vezes sobrevivem à extração do PDF dentro do próprio título. Só remove
# pares abre/fecha, pra não mexer num underscore ou asterisco solto que
# apareça por acaso no meio do texto (ou no fallback vindo do nome do
# arquivo, que tem underscore como separador de palavra — esse não passa
# por aqui, ver process_file).
def clean_title_text(title: str) -> str:
    cleaned = re.sub(r'\*\*(.+?)\*\*', r'\1', title)
    cleaned = re.sub(r'__(.+?)__', r'\1', cleaned)
    cleaned = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'\1', cleaned)
    cleaned = re.sub(r'(?<!\w)_(.+?)_(?!\w)', r'\1', cleaned)
    return re.sub(r'\s{2,}', ' ', cleaned).strip()


# --- detecção de ano ---------------------------------------------------
# Ordem de prioridade: copyright explícito > received/accepted/published >
# id de arXiv (prefixo YYMM) > "vol. X, no. Y, <ano>" de citação de revista.
# Todas restritas a um intervalo plausível pra evitar pegar, por exemplo,
# um ano citado dentro de uma referência bibliográfica do corpo do texto.
YEAR_MIN, YEAR_MAX = 1990, CURRENT_YEAR + 1

COPYRIGHT_YEAR_RE = re.compile(r'(?:©|\(c\)|copyright)\s*(\d{4})', re.I)
RECEIVED_ACCEPTED_RE = re.compile(
    r'(?:received|accepted|published|revised)[^.\n]{0,40}?(\d{4})', re.I
)
ARXIV_ID_RE = re.compile(r'arxiv:\s*(\d{2})(\d{2})\.\d{4,5}', re.I)
VOL_NO_YEAR_RE = re.compile(
    r'\bvol\.?\s*\d+,?\s*no\.?\s*\d+[^.\n]{0,20}?(\d{4})', re.I
)


def _plausible_year(y: int):
    return y if YEAR_MIN <= y <= YEAR_MAX else None


def detect_year(body: str):
    """Melhor esforço: procura um ano plausível nas primeiras ~200 linhas
    (onde normalmente aparece cabeçalho/masthead/copyright), tentando os
    padrões em ordem de confiança. Retorna None se nada plausível achado —
    nesse caso o campo fica null e o arquivo entra no relatório de revisão."""
    head = "\n".join(body.splitlines()[:200])
    for rx in (COPYRIGHT_YEAR_RE, RECEIVED_ACCEPTED_RE):
        m = rx.search(head)
        if m:
            y = _plausible_year(int(m.group(1)))
            if y:
                return y
    m = ARXIV_ID_RE.search(head)
    if m:
        y = _plausible_year(2000 + int(m.group(1)))
        if y:
            return y
    m = VOL_NO_YEAR_RE.search(head)
    if m:
        y = _plausible_year(int(m.group(1)))
        if y:
            return y
    return None


def detect_venue(body: str):
    """Melhor esforço: reaproveita a mesma heurística de masthead usada pra
    filtrar o título — o texto que ali é descartado (nome de revista/
    conferência) é exatamente o que queremos aqui como veículo."""
    lines = heading_lines(body)
    for i, line in enumerate(lines):
        m = re.match(r'^#{1,2}\s+(.+?)\s*$', line.strip())
        if not m:
            continue
        text = m.group(1).strip()
        if SECTION_LABEL_RE.match(text):
            continue  # "Regular Articles" etc. não é veículo, é rótulo
        if is_masthead_heading(text, i, lines):
            return text
    return None


def first_heading(body: str):
    """Primeiro cabeçalho do corpo que não pareça masthead de revista (nome
    da revista, "Regular Articles", etc.) nem um placeholder genérico
    ("Article", "Untitled", ...), aceitando # ou ## (alguns arquivos usam
    ## como título principal em vez de #)."""
    lines = heading_lines(body)
    for i, line in enumerate(lines):
        m = re.match(r'^#{1,2}\s+(.+?)\s*$', line.strip())
        if not m:
            continue
        if is_bad_title_heading(m.group(1), i, lines):
            continue
        return m.group(1)
    return None


def looks_like_masthead_title(title: str, body: str) -> bool:
    """Verifica se um título já salvo no front matter na verdade veio de um
    cabeçalho de masthead (bug de execuções antigas do fix_frontmatter) ou
    é um placeholder genérico tipo "Article"."""
    if is_generic_placeholder_title(title):
        return True
    lines = heading_lines(body)
    for i, line in enumerate(lines):
        m = re.match(r'^#{1,2}\s+(.+?)\s*$', line.strip())
        if m and m.group(1).strip() == title.strip():
            return is_masthead_heading(m.group(1), i, lines)
    return False


def build_front_matter(title, tema_principal, temas_relacionados, ano, autores, veiculo, pdf_rel):
    title_escaped = title.replace('"', '\\"')
    ano_str = str(ano) if ano is not None else "null"
    if veiculo:
        veiculo_str = '"' + veiculo.replace('"', '\\"') + '"'
    else:
        veiculo_str = "null"
    return (
        "---\n"
        f'title: "{title_escaped}"\n'
        f"tema_principal: {tema_principal}\n"
        f"temas_relacionados: {temas_relacionados}\n"
        f"ano: {ano_str}\n"
        f"autores: {autores}\n"
        f"veiculo: {veiculo_str}\n"
        f"pdf: {pdf_rel}\n"
        "---\n"
    )


def process_file(md_path: Path, tema_principal: str):
    original = md_path.read_text(encoding="utf-8")
    fm_block, body = parse_front_matter(original)

    name = md_path.stem
    pdf_rel = f"../pdf/{name}.pdf"

    title = get_field(fm_block, "title")
    if title:
        title = title.strip().strip('"')
    temas_relacionados = get_field(fm_block, "temas_relacionados") or "[]"

    used_filename_fallback = False
    if not title or looks_like_masthead_title(title, body):
        title = first_heading(body)
        if not title:
            title = name
            used_filename_fallback = True

    if not used_filename_fallback:
        # só limpa ênfase markdown em título vindo de texto de verdade —
        # o fallback é o nome do arquivo, cujo underscore é separador de
        # palavra, não marcador de itálico.
        title = clean_title_text(title)

    ano_raw = get_field(fm_block, "ano")
    if ano_raw and ano_raw.strip().lower() not in ("null", "none", ""):
        ano = int(ano_raw.strip())
        needs_year_review = False
    else:
        ano = detect_year(body)
        needs_year_review = ano is None

    autores = get_field(fm_block, "autores") or "[]"

    veiculo_raw = get_field(fm_block, "veiculo")
    if veiculo_raw and veiculo_raw.strip().lower() not in ("null", "none", ""):
        veiculo = veiculo_raw.strip().strip('"')
    else:
        veiculo = detect_venue(body)

    new_fm = build_front_matter(title, tema_principal, temas_relacionados, ano, autores, veiculo, pdf_rel)
    new_content = new_fm + "\n" + body.lstrip("\n")
    return new_content, new_content != original, needs_year_review


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folders", nargs="*", help="Pastas-tema a processar (padrão: todas)")
    ap.add_argument("--apply", action="store_true", help="Grava os arquivos (padrão: dry-run)")
    args = ap.parse_args()

    theme_dirs = discover_theme_dirs(args.folders)
    if not theme_dirs:
        sys.exit("nenhuma pasta-tema encontrada")

    total = 0
    needs_review = []
    for theme_dir in theme_dirs:
        md_dir = theme_dir / "md"
        changed = []
        for md_path in sorted(md_dir.glob("*.md")):
            if md_path.name == "concepts.md" or md_path.name.endswith("_summary.md"):
                continue
            new_content, is_changed, needs_year_review = process_file(md_path, theme_dir.name)
            if is_changed:
                changed.append(md_path.name)
                if args.apply:
                    md_path.write_text(new_content, encoding="utf-8")
            if needs_year_review:
                needs_review.append(f"{theme_dir.name}/md/{md_path.name}")
        if changed:
            print(f"{theme_dir.name}:")
            for i, f in enumerate(changed, start=1):
                print(f"  [{i}] {f}")
            total += len(changed)
        else:
            print(f"{theme_dir.name}: sem mudanças")

    if not args.apply:
        print(f"\nDry-run — {total} arquivo(s) mudariam. Rode com --apply para gravar.")
    else:
        print(f"\n{total} arquivo(s) atualizado(s).")

    if needs_review:
        print(f"\n{len(needs_review)} arquivo(s) sem ano detectado (ano: null) — preencher à mão:")
        for f in needs_review:
            print(f"  - {f}")
    print("\nLembrete: campo 'autores' não é detectado automaticamente — preencher à mão em cada arquivo.")


if __name__ == "__main__":
    main()
