# Repo overview

A personal literature collection on optical networks, 5G/6G, and related AI/ML topics. Each top-level folder is a subject bucket; papers move through a small pipeline as they're read and synthesized.

## Folders

- `5g6g/`, `mode_fibers/`, `pon/` — subject-sorted collections. The folder name is the theme.
- `projeto_universal/`, `reading/` — not yet subject-sorted. Papers land here first and get moved into a themed folder once a clear subject emerges from my own judgment.
- `01_notes/` — my own reading notes and interpretation of papers, kept separate from the generated files below. Format documented in `01_notes/README.md`.
- `scripts/` — extraction/formatting automation (PDF → text, frontmatter, titles, summary index, site manifest, incremental concepts).
- `to_add/{pdf,md}/` — inbox for new papers not yet processed.

## Per-topic structure

Each subject folder (`5g6g/`, `mode_fibers/`, `pon/`, and eventually the untriaged ones) follows the same layout:

```
<topic>/
  pdf/*.pdf              original paper PDFs
  md/*.md                full extracted text, one per PDF, same base filename
  md/*_summary.md        per-paper summary, same base filename + _summary
  summary.md             index of every paper in this topic, linking to its md/summary
  concepts.md            cross-paper synthesized concept glossary (not present for every topic yet)
```

The filename convention *is* the index: `paper.pdf` ↔ `md/paper.md` ↔ `md/paper_summary.md`. No separate manifest is needed to pair them.

## Pipeline for a new paper

1. Drop the PDF into `to_add/pdf/` (or directly into a topic's `pdf/` if the subject is already obvious).
2. Run the extraction scripts (`scripts/run_extraction.py`) to produce the full-text `md` and the per-paper `_summary.md`.
3. Update the topic's `summary.md` index (`scripts/update_summary.py --apply`).
4. Fold the new summaries into the topic's `concepts.md` — incrementally, only the new papers (see below).
5. Commit and push. `index.html` needs no edit: it reads `manifest.json`, which a GitHub Action regenerates (see below).
6. Read the paper and add personal notes in `01_notes/` (see that folder's own README for the format).

## Website (GitHub Pages)

`index.html` is a static shell: it fetches `manifest.json` and builds the list of summaries per topic (plus a "conceitos" link to each topic's `concepts.md`). Never edit the list by hand.

- `scripts/build_manifest.py` generates `manifest.json` from the filesystem — any folder with `md/` is a topic; a paper is listed once it has `md/<name>_summary.md`. It only rewrites the file if the content changed.
- `.github/workflows/manifest.yml` runs it on every push that touches `**/md/**` or `**/concepts.md` and commits `manifest.json` back if it changed. After a push that triggers it, `git pull --rebase` before the next push.
- `.nojekyll` at the root stops GitHub Pages from converting the `.md` files (they have front matter) into `.html`.
- To preview locally: `python3 scripts/build_manifest.py && python3 -m http.server`.

## Incremental `concepts.md`

`scripts/update_concepts.py` adds new papers to `concepts.md` without reprocessing the old ones. Each `## Concept` section carries a hidden `<!-- sources: ... | gen: ... -->` line, and `<topic>/concepts.state.json` records which summaries were already folded in. For each new summary the LLM (any command that reads a prompt on stdin and prints the answer, passed with `--llm-cmd`) routes it to existing concepts or new ones, and only those sections are rewritten. Sections you edited by hand are never overwritten: the proposal goes to `<topic>/concepts.proposed.md`.

```
python3 scripts/update_concepts.py <topic>                                   # dry-run: what's pending
python3 scripts/update_concepts.py <topic> --apply --llm-cmd "claude -p"      # fold in pending papers
python3 scripts/update_concepts.py <topic> --bootstrap --apply [--llm-cmd …]  # one-time: adopt an existing concepts.md
python3 scripts/update_concepts.py <topic> --reorganize --apply --llm-cmd … [--structure-hint old.md]  # flat -> topics (##) > subtopics (###)
python3 scripts/update_concepts.py <topic> --consolidate --llm-cmd …          # suggest merges/renames (writes nothing)
```

A `concepts.md` can be flat (one `## Concept` per entry) or hierarchical (`## Topic` with `### Concept` entries; `projeto_universal` is hierarchical). Incremental updates keep whichever shape the file has, and a new concept is filed under the topic the LLM picks. `--rebuild` always restarts flat, so run `--reorganize` again afterwards.

A topic with no `concepts.md` yet is created from scratch by the same command.

## What each file type is *for*

- **`md/*_summary.md`** — a neutral, per-paper distillation: what the paper says, extracted, no personal judgment.
- **`summary.md`** — a directory: every paper title in the topic plus a link to its files. For finding things, not for understanding them.
- **`concepts.md`** — cross-paper synthesis: the same concept explained once, merged from however many papers in the topic discuss it. Still extractive/neutral — it explains what the field says, not what I think of it.
- **`01_notes/`** — my own reading, critique, and connections. The only place in this repo that isn't a distillation of the source material but my own thinking about it.
