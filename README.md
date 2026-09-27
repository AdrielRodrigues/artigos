# Repo overview

A personal literature collection on optical networks, 5G/6G, and related AI/ML topics. Each top-level folder is a subject bucket; papers move through a small pipeline as they're read and synthesized.

## Folders

- `5g6g/`, `mode_fibers/`, `pon/` — subject-sorted collections. The folder name is the theme.
- `projeto_universal/`, `reading/` — not yet subject-sorted. Papers land here first and get moved into a themed folder once a clear subject emerges from my own judgment.
- `01_notes/` — my own reading notes and interpretation of papers, kept separate from the generated files below. Format documented in `01_notes/README.md`.
- `scripts/` — extraction/formatting automation (PDF → text, frontmatter, titles, summary index).
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
3. Update the topic's `summary.md` index.
4. Once a topic folder has enough papers, (re)generate `concepts.md` to synthesize cross-paper concepts.
5. Read the paper and add personal notes in `01_notes/` (see that folder's own README for the format).

## What each file type is *for*

- **`md/*_summary.md`** — a neutral, per-paper distillation: what the paper says, extracted, no personal judgment.
- **`summary.md`** — a directory: every paper title in the topic plus a link to its files. For finding things, not for understanding them.
- **`concepts.md`** — cross-paper synthesis: the same concept explained once, merged from however many papers in the topic discuss it. Still extractive/neutral — it explains what the field says, not what I think of it.
- **`01_notes/`** — my own reading, critique, and connections. The only place in this repo that isn't a distillation of the source material but my own thinking about it.
