#!/usr/bin/env python3
"""Renomeia PDFs para o título real do artigo, em snake_case.

Fonte do título: metadado 'Title' do PDF (pdfinfo). Se estiver ausente ou
parecer lixo (nome de arquivo de editoração, id sem espaços, etc.), cai para
um heurístico que lê a primeira página (pdftotext) e tenta achar a linha do
título, pulando cabeçalhos de revista/DOI/autores.

Requer poppler-utils (pdfinfo, pdftotext).

Uso:
    python3 sanitize_titles.py <arquivo.pdf | pasta> [...] [--apply] [--recursive]

Sem --apply roda em modo dry-run: só mostra a proposta de renomeação.
"""
import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

BOILERPLATE_PATTERNS = [
    r'^contents lists available at',
    r'^journal homepage',
    r'^received\b.*\d{4}',
    r'^date of (publication|current version)\b',  # 2ª linha de um cabeçalho de datas quebrado em duas
    r'^digital object identifier',
    r'^doi:?\s*10\.',
    r'^https?://',
    r'^www\.',
    r'^issn\b',
    r'^\d+\s*$',
    r'^research article\b',
    r'^review( article)?\b',
    r'^tutorial\b',
    r'^invited paper\b',
    r'^abstract\b',
    r'^index terms',
    r'^keywords',
    r'^article info',
    r'^arxiv:',
    r'^©',
    r'^accepted from open call$',
    r'^open access$',
]

# padrões de "ruído de cabeçalho" que podem aparecer no meio da linha
# (ex.: "E82  Vol. 17, No. 11 / November 2025 / Journal of Optical...")
MASTHEAD_PATTERNS = [
    r'\bvol\.?\s*\d+,?\s*no\.?\s*\d+',
    r'\(\d{4}\)\s*\d+\s*[:–-]\s*\d+',           # "Journal of Optics (2025) 54:39-45"
    r'\bissue\s*\d+',
    r'\bjournal of\b.{0,60}\b(20\d{2}|vol)\b',
    r'\bieee\b.{0,40}\bvol\.?\s*\d+',
]
AUTHOR_LINE_HINTS = re.compile(
    r'\b(university|department|institute|laboratory|@|member,?\s*ieee|senior member|fellow)\b',
    re.I,
)


def is_boilerplate(line: str) -> bool:
    low = line.strip().lower()
    if not low:
        return True
    if any(re.search(p, low) for p in BOILERPLATE_PATTERNS):
        return True
    if any(re.search(p, low) for p in MASTHEAD_PATTERNS):
        return True
    return False


def is_author_like(line: str) -> bool:
    """Detecta linhas de autoria — tanto em CAIXA ALTA separadas por vírgula
    (ex.: 'CATALINA CUEVAS-ALIAGA1 , JUAN PINTO-RÍOS 1') quanto em Title Case
    com iniciais/afiliações (ex.: 'M. A. Amirabadi, S. A. Nezamalhosseini,
    M. H. Kahaei, and Lawrence R. Chen')."""
    letters = [c for c in line if c.isalpha()]
    if len(letters) < 8:
        return False
    upper_ratio = sum(1 for c in letters if c.isupper()) / len(letters)
    has_separator = (',' in line) or re.search(r'\band\b', line, re.I)
    if upper_ratio > 0.85 and has_separator:
        return True
    if re.search(r'\b[A-Z]\.\s?[A-Z]?\.?\s+[A-Z][a-z]+', line):
        return True  # iniciais estilo "M. A. Amirabadi"
    if len(re.findall(r',\s*\*?\s*\d', line)) >= 2:
        return True  # marcadores de afiliação em sobrescrito: "Nome,1 Outro Nome,2"
    if len(re.findall(r'[a-z]\d\b', line)) >= 2:
        return True  # dígito de nota de rodapé grudado no fim do sobrenome: "Doherty1"
    segments = [s.strip() for s in line.split(',') if s.strip()]
    if len(segments) >= 2:
        short_capitalized = sum(
            1 for s in segments if s and 1 <= len(s.split()) <= 4 and s[0].isupper()
        )
        if short_capitalized / len(segments) >= 0.6:
            return True
    return False


def looks_like_bad_metadata(title: str) -> bool:
    if not title:
        return True
    t = title.strip()
    if len(t) < 12:
        return True
    if re.search(r'\.(indd|docx?|qxd|tex|wpd)$', t, re.I):
        return True
    if re.fullmatch(r'[\w.\-]+', t) and ' ' not in t:
        return True  # parece nome de arquivo/id, não título com espaços
    return False


def pdfinfo_title(pdf_path: Path) -> str:
    try:
        out = subprocess.run(
            ["pdfinfo", str(pdf_path)], capture_output=True, text=True, timeout=30
        ).stdout
    except Exception:
        return ""
    for line in out.splitlines():
        if line.startswith("Title:"):
            return line[len("Title:"):].strip()
    return ""


def first_page_title(pdf_path: Path) -> str:
    try:
        out = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "1", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, timeout=30,
        ).stdout
    except Exception:
        return ""
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    candidate = []
    for line in lines:
        if is_boilerplate(line):
            if candidate:
                break
            continue
        if AUTHOR_LINE_HINTS.search(line) or is_author_like(line):
            break
        if len(line) < 4:
            continue
        candidate.append(line)
        if len(candidate) >= 4:  # título raramente passa de ~4 linhas quebradas
            break
    title = " ".join(candidate).strip()
    if len(title.split()) > 25:
        return ""  # provavelmente colou ruído; melhor sinalizar do que inventar
    return title


def slugify(title: str) -> str:
    t = html.unescape(title)
    t = re.sub(r'[Ͱ-Ͽ]', '', t)  # letras gregas soltas (ex.: λ)
    t = re.sub(r'[:?,()]', '', t)
    t = t.replace('/', '-')
    t = t.lower()
    t = re.sub(r'\s+', '_', t.strip())
    t = re.sub(r'_+', '_', t)
    t = re.sub(r'[^a-z0-9\-_À-ÿ]', '', t)
    t = re.sub(r'-{2,}', '-', t)
    return t


def resolve_title(pdf_path: Path):
    title = pdfinfo_title(pdf_path)
    source = "metadados"
    if looks_like_bad_metadata(title):
        title = first_page_title(pdf_path)
        source = "primeira página"
    return title.strip(), source


def unique_target(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    i = 2
    while True:
        cand = dest.with_name(f"{stem}_{i}{suffix}")
        if not cand.exists():
            return cand
        i += 1


def collect_pdfs(paths, recursive):
    pdfs = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            it = p.rglob("*.pdf") if recursive else p.glob("*.pdf")
            pdfs.extend(sorted(it))
        elif p.suffix.lower() == ".pdf":
            pdfs.append(p)
    return pdfs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="PDFs ou pastas contendo PDFs")
    ap.add_argument("--apply", action="store_true", help="Executa a renomeação (padrão: dry-run)")
    ap.add_argument("--recursive", action="store_true", help="Procura PDFs recursivamente nas pastas informadas")
    args = ap.parse_args()

    for tool in ("pdfinfo", "pdftotext"):
        if shutil.which(tool) is None:
            sys.exit(f"erro: '{tool}' não encontrado (instale poppler-utils)")

    pdfs = collect_pdfs(args.paths, args.recursive)
    if not pdfs:
        sys.exit("nenhum PDF encontrado")

    rows = []
    for pdf in pdfs:
        title, source = resolve_title(pdf)
        if not title:
            rows.append((pdf, None, None, "SEM TÍTULO — revisar manualmente"))
            continue
        new_name = slugify(title) + ".pdf"
        status = "sem mudança" if new_name == pdf.name else f"via {source}"
        rows.append((pdf, title, new_name, status))

    width = min(max((len(str(r[0])) for r in rows), default=10), 70)
    for pdf, title, new_name, status in rows:
        print(f"{str(pdf):<{width}}  ->  {new_name or '(sem proposta)':<60}  [{status}]")

    if not args.apply:
        print("\nDry-run — nada foi alterado. Rode de novo com --apply para renomear.")
        return

    applied = 0
    for pdf, title, new_name, status in rows:
        if not new_name or new_name == pdf.name:
            continue
        dest = unique_target(pdf.with_name(new_name))
        pdf.rename(dest)
        applied += 1
        print(f"renomeado: {pdf.name} -> {dest.name}")
    print(f"\n{applied} arquivo(s) renomeado(s).")


if __name__ == "__main__":
    main()
