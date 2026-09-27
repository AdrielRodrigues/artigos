#!/usr/bin/env python3
"""Sincroniza summary.md com o que existe de fato em pdf/ e md/.

Duas colunas de status, cada uma só "pendente" ou "ok" — sem conteúdo:
  Texto completo = ok se <tema>/md/<nome>.md existir
  Resumo         = ok se <tema>/md/<nome>_summary.md existir

A coluna Artigo vira link pro .md (título do front matter, ou do primeiro
"# Título" se não houver front matter) assim que o texto completo existir.
A coluna Temas relacionados nunca é tocada — é informação editorial que não
dá pra derivar do sistema de arquivos.

PDFs em pdf/ sem linha na tabela ganham uma linha nova (pendente/pendente).

Uso:
    python3 update_summary.py [pasta-tema ...] [--apply]

Sem argumentos, processa todas as pastas-tema encontradas (qualquer
subpasta de artigos/ que tenha pdf/, md/ e summary.md).
Sem --apply roda em modo dry-run: só mostra o que mudaria.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HEADER_RE = re.compile(r'^\|\s*Texto completo\s*\|', re.I)
SEP_RE = re.compile(r'^\|[-\s]+\|[-\s]+\|[-\s]+\|[-\s]+\|\s*$')
ROW_RE = re.compile(r'^\|(.*)\|(.*)\|(.*)\|(.*)\|\s*$')
LINK_RE = re.compile(r'\[(.*)\]\(md/([^)]+)\.md\)\s*$')
BACKTICK_RE = re.compile(r'`([^`]+)\.pdf`')


def discover_theme_dirs(explicit):
    if explicit:
        return [Path(e) for e in explicit]
    dirs = []
    for p in sorted(ROOT.iterdir()):
        if p.is_dir() and (p / "summary.md").is_file() and (p / "pdf").is_dir():
            dirs.append(p)
    return dirs


def get_title(md_path: Path, fallback: str) -> str:
    try:
        with open(md_path, encoding="utf-8") as f:
            head = [next(f) for _ in range(30)]
    except (StopIteration, FileNotFoundError):
        head = []
    if head and head[0].strip() == "---":
        for line in head[1:]:
            if line.strip() == "---":
                break
            m = re.match(r'^title:\s*"?(.*?)"?\s*$', line)
            if m:
                return m.group(1)
    for line in head:  # sem front matter: usa o primeiro H1 (# Título)
        m = re.match(r'^#\s+(.+?)\s*$', line)
        if m:
            return m.group(1)
    return fallback


def name_from_row(artigo_cell: str):
    m = LINK_RE.search(artigo_cell)
    if m:
        return m.group(2)
    m = BACKTICK_RE.search(artigo_cell)
    if m:
        return m.group(1)
    return None


def build_row(texto, resumo, temas, artigo):
    return f"| {texto} | {resumo} | {temas} | {artigo} |"


def compute_cells(name: str, md_dir: Path, artigo_cell: str):
    md_path = md_dir / f"{name}.md"
    summary_path = md_dir / f"{name}_summary.md"
    has_md = md_path.is_file()
    has_summary = summary_path.is_file()

    texto = "ok" if has_md else "pendente"
    resumo = "ok" if has_summary else "pendente"

    if has_md:
        if LINK_RE.search(artigo_cell):
            new_artigo = artigo_cell  # já é link com título curado — não mexe
        else:
            title = get_title(md_path, fallback=name)
            new_artigo = f"[{title}](md/{name}.md)"
    else:
        new_artigo = f"`{name}.pdf`"  # md sumiu (ou nunca existiu) — volta pra referência ao pdf

    return texto, resumo, new_artigo


def process_theme(theme_dir: Path, apply: bool):
    summary_path = theme_dir / "summary.md"
    pdf_dir = theme_dir / "pdf"
    md_dir = theme_dir / "md"

    with open(summary_path, encoding="utf-8") as f:
        lines = f.readlines()

    known_names = set()
    new_lines = []
    changes = []
    header_idx = None

    for i, raw in enumerate(lines):
        line = raw.rstrip("\n")
        if HEADER_RE.match(line):
            header_idx = i
            new_lines.append(raw)
            continue
        if SEP_RE.match(line):
            new_lines.append(raw)
            continue
        m = ROW_RE.match(line) if line.startswith("|") else None
        if not m:
            new_lines.append(raw)
            continue

        old_texto, old_resumo, temas_cell, artigo_cell = (c.strip() for c in m.groups())
        name = name_from_row(artigo_cell)
        if name is None:
            new_lines.append(raw)
            continue
        if name in known_names:
            changes.append((name, f"{old_texto}/{old_resumo}", "(linha duplicada removida)"))
            continue
        known_names.add(name)

        new_texto, new_resumo, new_artigo = compute_cells(name, md_dir, artigo_cell)
        new_row = build_row(new_texto, new_resumo, temas_cell, new_artigo)
        if new_row != line:
            changes.append((name, f"{old_texto}/{old_resumo}", f"{new_texto}/{new_resumo}"))
        new_lines.append(new_row + "\n")

    # PDFs sem linha na tabela ainda -> adiciona pendente/pendente
    existing_pdfs = sorted(p.stem for p in pdf_dir.glob("*.pdf"))
    missing = [name for name in existing_pdfs if name not in known_names]
    if missing and header_idx is not None:
        insert_at = header_idx + 2  # header + separador
        added_lines = []
        for name in missing:
            artigo_cell = f"`{name}.pdf`"
            texto, resumo, artigo = compute_cells(name, md_dir, artigo_cell)
            added_lines.append(build_row(texto, resumo, "", artigo) + "\n")
            changes.append((name, "(novo)", f"{texto}/{resumo}"))
        new_lines = new_lines[:insert_at] + added_lines + new_lines[insert_at:]

    if apply:
        with open(summary_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    return changes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folders", nargs="*", help="Pastas-tema a processar (padrão: todas)")
    ap.add_argument("--apply", action="store_true", help="Grava summary.md (padrão: dry-run)")
    args = ap.parse_args()

    theme_dirs = discover_theme_dirs(args.folders)
    if not theme_dirs:
        sys.exit("nenhuma pasta-tema encontrada")

    total_changes = 0
    for theme_dir in theme_dirs:
        changes = process_theme(theme_dir, args.apply)
        if not changes:
            print(f"{theme_dir.name}: sem mudanças")
            continue
        print(f"{theme_dir.name}:")
        for i, (name, old, new) in enumerate(changes, start=1):
            print(f"  [{i}] {name}: {old} -> {new}")
        total_changes += len(changes)

    if not args.apply:
        print(f"\nDry-run — {total_changes} mudança(s) não aplicada(s). Rode com --apply para gravar.")
    else:
        print(f"\n{total_changes} mudança(s) gravada(s).")


if __name__ == "__main__":
    main()
