#!/usr/bin/env python3
"""Padroniza o front matter de todo md/<nome>.md (texto completo do artigo).

Campos mantidos: title, tema_principal, temas_relacionados, pdf.

O campo "status" é removido caso exista — desde que texto/resumo passaram
a ser rastreados como pendente/ok em summary.md, esse campo por arquivo
ficava redundante e podia dessincronizar.

Regras por campo:
  title              mantém o que já houver; se o arquivo não tiver front
                      matter, usa o primeiro "# Título" do corpo.
  tema_principal      nome da pasta-tema onde o arquivo está (sempre
                      recalculado — reflete onde o arquivo mora agora).
  temas_relacionados  mantém o que já houver; senão fica [].
  pdf                 sempre recalculado como ../pdf/<nome>.pdf.

Arquivos ignorados: concepts.md e *_summary.md (não são o texto completo
de um artigo).

Uso:
    python3 fix_frontmatter.py [pasta-tema ...] [--apply]

Sem argumentos, processa todas as pastas-tema (qualquer subpasta de
artigos/ com md/ e pdf/). Sem --apply roda em modo dry-run.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


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


def first_heading(body: str):
    """Primeiro cabeçalho do corpo, aceitando # ou ## (alguns arquivos usam
    ## como título principal em vez de #)."""
    for line in body.splitlines()[:30]:
        m = re.match(r'^#{1,2}\s+(.+?)\s*$', line.strip())
        if m:
            return m.group(1)
    return None


def build_front_matter(title, tema_principal, temas_relacionados, pdf_rel):
    title_escaped = title.replace('"', '\\"')
    return (
        "---\n"
        f'title: "{title_escaped}"\n'
        f"tema_principal: {tema_principal}\n"
        f"temas_relacionados: {temas_relacionados}\n"
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

    if not title:
        title = first_heading(body) or name

    new_fm = build_front_matter(title, tema_principal, temas_relacionados, pdf_rel)
    new_content = new_fm + "\n" + body.lstrip("\n")
    return new_content, new_content != original


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folders", nargs="*", help="Pastas-tema a processar (padrão: todas)")
    ap.add_argument("--apply", action="store_true", help="Grava os arquivos (padrão: dry-run)")
    args = ap.parse_args()

    theme_dirs = discover_theme_dirs(args.folders)
    if not theme_dirs:
        sys.exit("nenhuma pasta-tema encontrada")

    total = 0
    for theme_dir in theme_dirs:
        md_dir = theme_dir / "md"
        changed = []
        for md_path in sorted(md_dir.glob("*.md")):
            if md_path.name == "concepts.md" or md_path.name.endswith("_summary.md"):
                continue
            new_content, is_changed = process_file(md_path, theme_dir.name)
            if is_changed:
                changed.append(md_path.name)
                if args.apply:
                    md_path.write_text(new_content, encoding="utf-8")
        if changed:
            print(f"{theme_dir.name}:")
            for f in changed:
                print(f"  {f}")
            total += len(changed)
        else:
            print(f"{theme_dir.name}: sem mudanças")

    if not args.apply:
        print(f"\nDry-run — {total} arquivo(s) mudariam. Rode com --apply para gravar.")
    else:
        print(f"\n{total} arquivo(s) atualizado(s).")


if __name__ == "__main__":
    main()
