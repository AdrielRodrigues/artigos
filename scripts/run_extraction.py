#!/usr/bin/env python3
"""Detecta PDFs sem texto completo (md/) e/ou resumo (md/*_summary.md) e,
opcionalmente, manda extraí-los via a API do projeto API-text-extract
(endpoint /batches), de forma assíncrona: o envio não espera o
processamento terminar.

Convenção (a mesma do update_summary.py):
  Texto completo = <tema>/md/<nome>.md
  Resumo         = <tema>/md/<nome>_summary.md

Uso:
    python3 run_extraction.py [pasta-tema ...]            # dry-run, só lista
    python3 run_extraction.py [pasta-tema ...] --apply     # envia os lotes e sai
    python3 run_extraction.py --check                      # busca resultados prontos

--apply envia um lote (POST /batches) por pasta-tema com os PDFs
pendentes e retorna na hora, sem esperar o processamento — o estado de
cada lote fica salvo em .run_extraction_state.json (na raiz do projeto).

--check consulta cada lote pendente (GET /batches/{id}) uma única vez
(sem polling/espera) e baixa (GET /download e /download-summary) só o
que já tiver terminado; um md já existente nunca é sobrescrito. PDFs
ainda em processamento continuam salvos no estado pra uma próxima
chamada de --check.

Sem argumentos, processa todas as pastas-tema encontradas (qualquer
subpasta de artigos/ que tenha pdf/, md/ e summary.md).
"""
import argparse
import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_API_URL = "http://127.0.0.1:40004"
STATE_PATH = ROOT / ".run_extraction_state.json"


def discover_theme_dirs(explicit):
    if explicit:
        return [Path(e) for e in explicit]
    dirs = []
    for p in sorted(ROOT.iterdir()):
        if p.is_dir() and (p / "summary.md").is_file() and (p / "pdf").is_dir():
            dirs.append(p)
    return dirs


def find_missing(theme_dir: Path):
    """Retorna [(pdf_path, precisa_texto, precisa_resumo), ...] pros PDFs
    de theme_dir/pdf/ que não têm o .md e/ou o _summary.md correspondente."""
    pdf_dir = theme_dir / "pdf"
    md_dir = theme_dir / "md"
    missing = []
    for pdf_path in sorted(pdf_dir.glob("*.pdf")):
        name = pdf_path.stem
        precisa_texto = not (md_dir / f"{name}.md").is_file()
        precisa_resumo = not (md_dir / f"{name}_summary.md").is_file()
        if precisa_texto or precisa_resumo:
            missing.append((pdf_path, precisa_texto, precisa_resumo))
    return missing


def status_label(precisa_texto, precisa_resumo):
    texto = "pendente" if precisa_texto else "ok"
    resumo = "pendente" if precisa_resumo else "ok"
    return f"texto={texto} resumo={resumo}"


def load_state():
    if not STATE_PATH.is_file():
        return []
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))["batches"]


def save_state(batches):
    STATE_PATH.write_text(json.dumps({"batches": batches}, indent=2), encoding="utf-8")


def submit_batch(api_url: str, pdf_paths):
    """Sobe todos os PDFs de uma vez via POST /batches e retorna o batch_id."""
    handles = [open(p, "rb") for p in pdf_paths]
    try:
        files = [("files", (p.name, fh, "application/pdf")) for p, fh in zip(pdf_paths, handles)]
        resp = requests.post(f"{api_url}/batches", files=files)
    finally:
        for fh in handles:
            fh.close()
    resp.raise_for_status()
    return resp.json()["batch_id"]


def download(api_url: str, endpoint: str, filename: str, dest_path: Path):
    resp = requests.get(f"{api_url}/{endpoint}/{filename}")
    resp.raise_for_status()
    dest_path.write_bytes(resp.content)


def submit_theme(theme_dir: Path, api_url: str, batches):
    """Lista pendências de theme_dir e, se houver, manda um lote e registra
    o resultado em `batches` (sem esperar o processamento)."""
    missing = find_missing(theme_dir)
    if not missing:
        print(f"{theme_dir.name}: sem pendências")
        return 0

    print(f"{theme_dir.name}:")
    for pdf_path, precisa_texto, precisa_resumo in missing:
        print(f"  {pdf_path.name}: {status_label(precisa_texto, precisa_resumo)}")

    pdf_paths = [m[0] for m in missing]
    try:
        batch_id = submit_batch(api_url, pdf_paths)
    except requests.RequestException as e:
        print(f"  -> falha ao enviar lote ({e})", file=sys.stderr)
        return len(missing)

    batches.append({
        "batch_id": batch_id,
        "api_url": api_url,
        "theme_dir": str(theme_dir),
        "files": [
            {"pdf": pdf_path.name, "name": pdf_path.stem,
             "precisa_texto": precisa_texto, "precisa_resumo": precisa_resumo}
            for pdf_path, precisa_texto, precisa_resumo in missing
        ],
    })
    print(f"  -> lote '{batch_id}' enviado ({len(missing)} arquivo(s)), processando em background.")
    return len(missing)


def check_batch(batch_entry):
    """Consulta um lote uma vez, baixa o que já terminou e retorna a lista
    dos arquivos que ainda estão em processamento (pra manter no estado)."""
    api_url = batch_entry["api_url"]
    batch_id = batch_entry["batch_id"]
    theme_dir = Path(batch_entry["theme_dir"])
    md_dir = theme_dir / "md"

    try:
        resp = requests.get(f"{api_url}/batches/{batch_id}")
        resp.raise_for_status()
        result = resp.json()
    except requests.RequestException as e:
        print(f"{theme_dir.name} (lote {batch_id}): falha ao consultar ({e})", file=sys.stderr)
        return batch_entry["files"]

    by_filename = {entry["filename"]: entry for entry in result["files"]}
    still_pending = []
    for file_record in batch_entry["files"]:
        status_entry = by_filename.get(file_record["pdf"])
        name = file_record["name"]

        if status_entry is None:
            print(f"{theme_dir.name}: {file_record['pdf']}: ausente na resposta do lote", file=sys.stderr)
            still_pending.append(file_record)
            continue

        if status_entry.get("message"):
            print(f"{theme_dir.name}: {file_record['pdf']}: falhou ({status_entry['message']})", file=sys.stderr)
            continue

        if status_entry.get("summary_status") != "completed":
            still_pending.append(file_record)
            continue

        try:
            if file_record["precisa_texto"]:
                download(api_url, "download", status_entry["ocr_output_filename"], md_dir / f"{name}.md")
            if file_record["precisa_resumo"]:
                download(api_url, "download-summary", status_entry["summary_output_filename"], md_dir / f"{name}_summary.md")
            print(f"{theme_dir.name}: {file_record['pdf']}: extraído com sucesso")
        except requests.RequestException as e:
            print(f"{theme_dir.name}: {file_record['pdf']}: falhou ao baixar resultado ({e})", file=sys.stderr)
            still_pending.append(file_record)

    return still_pending


def cmd_apply(theme_dirs, api_url):
    batches = load_state()
    total_missing = 0
    for theme_dir in theme_dirs:
        total_missing += submit_theme(theme_dir, api_url, batches)
    save_state(batches)
    print(f"\n{total_missing} PDF(s) pendente(s) enviado(s). Rode --check mais tarde pra buscar os resultados.")


def cmd_check():
    batches = load_state()
    if not batches:
        print("nenhum lote pendente")
        return

    remaining_batches = []
    for batch_entry in batches:
        still_pending = check_batch(batch_entry)
        if still_pending:
            batch_entry["files"] = still_pending
            remaining_batches.append(batch_entry)

    save_state(remaining_batches)
    if remaining_batches:
        pending_count = sum(len(b["files"]) for b in remaining_batches)
        print(f"\n{pending_count} PDF(s) ainda em processamento.")
    else:
        print("\ntodos os lotes pendentes foram concluídos.")


def cmd_dry_run(theme_dirs):
    total_missing = 0
    for theme_dir in theme_dirs:
        missing = find_missing(theme_dir)
        if not missing:
            print(f"{theme_dir.name}: sem pendências")
            continue
        print(f"{theme_dir.name}:")
        for pdf_path, precisa_texto, precisa_resumo in missing:
            print(f"  {pdf_path.name}: {status_label(precisa_texto, precisa_resumo)}")
        total_missing += len(missing)

    print(f"\nDry-run — {total_missing} PDF(s) com pendência. Rode com --apply para enviar pro lote da API.")
    if load_state():
        print("(há lotes já enviados aguardando --check)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folders", nargs="*", help="Pastas-tema a processar (padrão: todas)")
    ap.add_argument("--apply", action="store_true",
                     help="Envia os PDFs pendentes pro lote da API e retorna na hora (sem esperar)")
    ap.add_argument("--check", action="store_true",
                     help="Busca o resultado dos lotes já enviados, baixando o que já estiver pronto")
    ap.add_argument("--api-url", default=DEFAULT_API_URL, help=f"URL base da API (default: {DEFAULT_API_URL})")
    args = ap.parse_args()

    if args.check:
        cmd_check()
        return

    theme_dirs = discover_theme_dirs(args.folders)
    if not theme_dirs:
        sys.exit("nenhuma pasta-tema encontrada")

    if args.apply:
        cmd_apply(theme_dirs, args.api_url)
    else:
        cmd_dry_run(theme_dirs)


if __name__ == "__main__":
    main()
