# data/build_cf_data.py — Counterfactual table data construction (design sketch)
# ---------------------------------------------------------------------------
# Pipeline overview (implementation withheld until paper acceptance):
#
#   1. Source tables   HiTab train/dev with exact cell-level annotations
#                     (linked_cells). Only lookup / simple-arithmetic QA are
#                     kept; open-ended reasoning questions are dropped.
#   2. Three interventions on the *cell grid*, applied to the logical matrix:
#        - structural (row/col swap)   evidence moves, answer text unchanged
#        - semantic  (value replace)   answer flips, evidence cell unchanged
#        - query     (query rewrite)   evidence and answer both migrate
#   3. Joint re-render: factual and counterfactual images are rendered by the
#      SAME renderer with identical geometry, so pixel diffs land only on the
#      intervened cells (rendering-consistency guarantee).
#   4. Hard validation: a sample is kept only if
#        new_answer != original_answer            (for semantic/query)
#        evidence coordinates actually moved      (for structural)
#   5. Output: paired jsonl + factual/counterfactual image dirs + build stats.
#
# The exact swap/replace operators, answer re-computation, and geometry-lock
# rendering details are part of the contribution and omitted here.

import argparse


def apply_structural_intervention(matrix, evidence_cells, rng):
    """Row/column permutation that relocates evidence while preserving content.

    Returns (new_matrix, new_evidence_cells, new_answer) or None if the
    intervention would collide with the hard-validation rules.
    """
    # --- intervention operator (omitted) ---
    raise NotImplementedError


def apply_semantic_intervention(matrix, answer_cell, value_pool, rng):
    """Same-distribution value replacement inside the causal upstream of the
    answer, then re-run the answer calculator. Answer must flip."""
    # --- replacement + re-computation logic (omitted) ---
    raise NotImplementedError


def apply_query_intervention(question, matrix, candidate_cells):
    """Query rewrite that points at a different cell: evidence and answer
    migrate together."""
    # --- rewrite template logic (omitted) ---
    raise NotImplementedError


def render_pair(matrix, matrix_cf, table_style):
    """Joint rendering with locked geometry: both images share layout, fonts,
    and cell boundaries; only intervened cells differ."""
    # --- renderer with geometry lock (omitted) ---
    raise NotImplementedError


def hard_validate(sample):
    """Keep-or-drop gate: answer flip / evidence movement must hold exactly."""
    # --- validation rules (omitted) ---
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="train")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    # main loop over annotated tables: sample intervention type, build pair,
    # validate, render, dump jsonl (omitted)


if __name__ == "__main__":
    main()
