#!/usr/bin/env python3
"""Gera manifest.json (raiz) — a lista que o index.html lê pra montar a página.

Descobre sozinho todas as pastas-tema (qualquer subpasta com md/) e, pra cada
artigo que já tem resumo (md/<nome>_summary.md), registra título/ano/veículo
(do front matter de md/<nome>.md, via catalog.load_records) e os caminhos
relativos. Cada tema também guarda o link pro concepts.md e pro summary.md,
quando existirem.

Não depende de summary.md (ao contrário de update_summary.py), então temas
ainda sem índice próprio — fl_ran, intelligent — aparecem normalmente.

Idempotente: o arquivo só é regravado se o conteúdo mudou, e não há
timestamp dentro dele — assim a GitHub Action não commita à toa.

Uso:
    python3 build_manifest.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog import load_records  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = ROOT / "manifest.json"


def discover_themes():
    return [p for p in sorted(ROOT.iterdir())
            if p.is_dir() and not p.name.startswith(".") and (p / "md").is_dir()]


def build_theme(theme_dir: Path):
    papers = []
    for r in load_records([theme_dir]):
        slug = Path(r["md_rel"]).stem
        summary_rel = f"{theme_dir.name}/md/{slug}_summary.md"
        if not (ROOT / summary_rel).is_file():
            continue  # só entra no index quem já tem resumo
        papers.append({
            "slug": slug,
            "title": r["titulo"],
            "ano": r["ano"],
            "veiculo": r["veiculo"],
            "summary": summary_rel,
            "md": r["md_rel"],
            "pdf": r["pdf_rel"],
        })
    papers.sort(key=lambda p: p["title"].lower())

    def rel_if_exists(name):
        return f"{theme_dir.name}/{name}" if (theme_dir / name).is_file() else None

    return {
        "name": theme_dir.name,
        "count": len(papers),
        "concepts": rel_if_exists("concepts.md"),
        "summary_index": rel_if_exists("summary.md"),
        "papers": papers,
    }


def main():
    themes = [t for t in (build_theme(d) for d in discover_themes()) if t["papers"]]
    manifest = {"themes": themes}
    text = json.dumps(manifest, ensure_ascii=False, indent=1) + "\n"

    old = OUT_PATH.read_text(encoding="utf-8") if OUT_PATH.is_file() else None
    if old == text:
        print("manifest.json: sem mudanças")
    else:
        OUT_PATH.write_text(text, encoding="utf-8")
        print("manifest.json: atualizado")
    total = sum(t["count"] for t in themes)
    for t in themes:
        extra = " +concepts" if t["concepts"] else ""
        print(f"  {t['name']}: {t['count']}{extra}")
    print(f"{total} resumo(s) em {len(themes)} tema(s)")


if __name__ == "__main__":
    main()
