# analysis/causal_effect.py — Follow / Invariance / Echo rates (design sketch)
# ---------------------------------------------------------------------------
# A three-intervention probe of *causal* table understanding, applicable to
# any VLM (no training involved). For each intervention we ask the model for
# the evidence coordinates AND the answer:
#
#   intervention   operation                    causal change
#   -------------  ---------------------------  ----------------------------
#   structural     row/column permutation       evidence moves, content same
#   semantic       replace upstream cell value  answer flips
#   query          rewrite query to other cell  evidence + answer migrate
#
# Three rates (per intervention, per dimension answer/position):
#
#   follow rate  : outputs match the post-intervention ground truth
#   invariance   : outputs unchanged vs. the model's own factual output
#                  (behavioral inertia — NOT gold-based)
#   echo rate    : outputs equal the *factual gold* mapped into the CF image
#                  (the "prior fingerprint"; echoing means the model did not
#                  read the current image)
#
# Construction guarantees: paired original/CF images share exact geometry;
# structural interventions must move evidence; semantic diffs must land only
# on intervened cells; query interventions keep images byte-identical.
#
# Headline findings (numbers in paper): modern VLMs show near-zero echo on
# the answer dimension (they do read the image), but position grounding sits
# near the floor — evidence localization, not answer sensitivity, is the
# bottleneck RL should target.

import argparse


def build_probe_set(src_tables, n_per_intervention=200, seed=0):
    # --- paired probe construction with hard validation (omitted) ---
    raise NotImplementedError


def parse_output(text):
    """Extract evidence coordinates (1-based row/col) and answer."""
    # --- parser (omitted) ---
    raise NotImplementedError


def three_rates(preds_cf, preds_orig, gold_cf, gold_orig):
    """follow / invariance / echo per dimension."""
    # --- rate computation (omitted) ---
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--probe", required=True)
    args = ap.parse_args()
    # (omitted)


if __name__ == "__main__":
    main()
