# analysis/iou_evidence.py — Evidence-coordinate IoU audit (sketch)
# ---------------------------------------------------------------------------
# When a model emits pixel boxes for evidence, how good are they? Pipeline:
#
#   1. Parse action boxes from model outputs (row/col/cell unions).
#   2. Build gold cell geometry: join benchmark samples to annotated cell
#      coordinates; when physical geometry is needed, extract table structure
#      with a table-structure OCR model and fall back to uniform grid.
#   3. IoU of predicted union box vs. gold evidence union (and vs. answer
#      cell alone), plus center-hit and any-overlap rates.
#
# Use cases in the paper: (a) models never trained to emit coordinates emit
# none on external benchmarks — IoU is uncomputable, showing evidence
# grounding must be trained explicitly; (b) an SFT-grounding model transfers
# poorly across rendering domains, motivating RL-stage localization training
# in-domain.

import argparse


def pred_union_bbox(actions):
    """Union of cell-level boxes if present, else row/col boxes."""
    # --- union logic (omitted) ---
    raise NotImplementedError


def gold_geometry(sample, structure_cache):
    """Gold evidence boxes from annotations + table structure extraction."""
    # --- join + structure extraction + cache (omitted) ---
    raise NotImplementedError


def iou(a, b):
    # standard box IoU (omitted)
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--details", required=True, help="inference dump jsonl")
    args = ap.parse_args()
    # (omitted)


if __name__ == "__main__":
    main()
