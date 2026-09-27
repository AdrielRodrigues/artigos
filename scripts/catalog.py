#!/usr/bin/env python3
"""Gera um catálogo único com todos os artigos de todas as pastas-tema,
a partir do front matter de md/<nome>.md (o mesmo que fix_frontmatter.py
escreve: title, tema_principal, ano, autores, veiculo, pdf).

Diferente de summary.md (por tema, preserva edições manuais célula a
célula), este catálogo é puramente derivado: não há nada pra preservar,
então ele é sempre regravado do zero a cada execução — não existe modo
--apply, só rodar de novo quando o front matter mudar.

Saída: catalog.md (tabela legível, na raiz) e catalog.csv (mesmas linhas,
pra filtrar/ordenar por ano numa planilha ou com pandas).

Uso:
    python3 catalog.py [--sort ano|tema|titulo]

Padrão de ordenação: ano decrescente (artigos sem ano detectado ficam no
final, agrupados, pra ficarem visíveis em vez de se misturarem com datas
reais).
"""
import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fix_frontmatter import discover_theme_dirs, parse_front_matter, get_field  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def load_records(theme_dirs):
    records = []
    for theme_dir in theme_dirs:
        md_dir = theme_dir / "md"
        if not md_dir.is_dir():
            continue
        for md_path in sorted(md_dir.glob("*.md")):
            if md_path.name == "concepts.md" or md_path.name.endswith("_summary.md"):
                continue
            text = md_path.read_text(encoding="utf-8")
            fm_block, _ = parse_front_matter(text)

            title = (get_field(fm_block, "title") or md_path.stem).strip().strip('"')
            tema = get_field(fm_block, "tema_principal") or theme_dir.name

            ano_raw = get_field(fm_block, "ano")
            ano = None
            if ano_raw and ano_raw.strip().lower() not in ("null", "none", ""):
                try:
                    ano = int(ano_raw.strip())
                except ValueError:
                    ano = None

            autores = (get_field(fm_block, "autores") or "[]").strip()
            veiculo_raw = get_field(fm_block, "veiculo")
            veiculo = ""
            if veiculo_raw and veiculo_raw.strip().lower() not in ("null", "none", ""):
                veiculo = veiculo_raw.strip().strip('"')

            records.append({
                "ano": ano,
                "tema": tema,
                "titulo": title,
                "autores": autores,
                "veiculo": veiculo,
                "md_rel": f"{theme_dir.name}/md/{md_path.name}",
                "pdf_rel": f"{theme_dir.name}/pdf/{md_path.stem}.pdf",
            })
    return records


SORT_KEYS = {
    "ano": lambda r: (r["ano"] is None, -(r["ano"] or 0), r["tema"], r["titulo"].lower()),
    "tema": lambda r: (r["tema"], r["titulo"].lower()),
    "titulo": lambda r: r["titulo"].lower(),
}


def write_md(records, out_path: Path):
    lines = [
        "# Catálogo geral",
        "",
        "Gerado automaticamente por `scripts/catalog.py` — não editar à mão "
        "(rode o script de novo depois de mudar o front matter).",
        "",
        f"Total: {len(records)} artigo(s).",
        "",
        "| Ano | Tema | Artigo | Veículo |",
        "|-----|------|--------|---------|",
    ]
    for r in records:
        ano_cell = str(r["ano"]) if r["ano"] is not None else "?"
        artigo_cell = f"[{r['titulo']}]({r['md_rel']})"
        lines.append(f"| {ano_cell} | {r['tema']} | {artigo_cell} | {r['veiculo']} |")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(records, out_path: Path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ano", "tema", "titulo", "autores", "veiculo", "md", "pdf"])
        for r in records:
            w.writerow([
                r["ano"] if r["ano"] is not None else "",
                r["tema"], r["titulo"], r["autores"], r["veiculo"],
                r["md_rel"], r["pdf_rel"],
            ])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sort", choices=SORT_KEYS.keys(), default="ano")
    args = ap.parse_args()

    theme_dirs = discover_theme_dirs(None)
    records = load_records(theme_dirs)
    records.sort(key=SORT_KEYS[args.sort])

    write_md(records, ROOT / "catalog.md")
    write_csv(records, ROOT / "catalog.csv")

    sem_ano = sum(1 for r in records if r["ano"] is None)
    com_veiculo = sum(1 for r in records if r["veiculo"])
    print(f"{len(records)} artigo(s) catalogado(s) -> catalog.md, catalog.csv")
    print(f"  sem ano: {sem_ano}")
    print(f"  com veiculo detectado: {com_veiculo}")


if __name__ == "__main__":
    main()
