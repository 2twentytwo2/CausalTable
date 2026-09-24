# data/build_perturb_data.py — Answer-preserving perturbation set (design sketch)
# ---------------------------------------------------------------------------
# Purpose: measure *invariance*. Row/column shuffles that provably do NOT
# change the answer (the shuffled cells are answer-irrelevant). A model that
# truly reads evidence should keep the same answer across the original and
# perturbed images (low flip rate).
#
# Construction: for each QA sample, enumerate permutations of rows/columns
# that avoid the gold evidence cells; verify with the answer calculator that
# the answer is invariant; render with the same joint-geometry renderer.
# Flip rate on this set isolates "over-sensitivity to layout" from genuine
# counterfactual sensitivity (evaluated on the CF set).

import argparse


def enumerate_answer_preserving_permutations(matrix, evidence_cells):
    """Permutations whose moved cells do not intersect gold evidence."""
    # --- enumeration + invariance check (omitted) ---
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="annotated QA samples")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    # build keep/flip paired set (omitted)


if __name__ == "__main__":
    main()
