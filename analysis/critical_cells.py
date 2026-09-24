# analysis/critical_cells.py — Cross-model evidence localization (sketch)
# ---------------------------------------------------------------------------
# Do VLMs know WHERE the answer is? Each model is asked for the critical
# cell coordinates (1-based, headers counted) plus the answer, on a fixed
# sampled benchmark subset (e.g., HiTab with gold linked_cells; AIT-QA/WTQ
# with unique-match pseudo-gold evidence).
#
# Metrics:
#   cell_exact  : predicted cell == gold answer cell
#   cell<=1     : Manhattan distance <= 1 (tolerance against row/column
#                 counting noise — recommended for cell-level evaluation)
#   ans_acc     : answer accuracy
#   parse_fail  : no parsable coordinates
#
# Findings summarized in the paper: a strong general VLM clearly leads both
# format-following and capability dimensions; interleaved "visual thinking"
# models fail to ground coordinates in text; legacy 7B VLMs follow the format
# perfectly while degenerating to a default cell — instruction following and
# perception are fully decoupled.

import argparse


def gold_evidence(sample):
    """Gold answer cell from annotations; pseudo-gold via unique text match."""
    # --- join + unique-match fallback (omitted) ---
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--infer-file", required=True)
    args = ap.parse_args()
    # parse predictions, join gold, aggregate per-dataset metrics (omitted)


if __name__ == "__main__":
    main()
