# eval/eval_cf.py — Internal evaluation: three causal dimensions (sketch)
# ---------------------------------------------------------------------------
# Metric families on the held-out counterfactual test set:
#
#   1. factual_acc        accuracy on factual images (standard capability)
#   2. cf_sensitive_rate  on CF images, the fraction of outputs that follow
#                         the *new* evidence (the core causal metric);
#                         decomposed into:
#                           follow  = outputs the new answer
#                           stale   = repeats the old (factual) answer
#                           other   = neither
#   3. per-shift-type     the same rates broken down by intervention type
#                         (structural row/col move vs. semantic value swap)
#                         and by whether evidence cells moved or stayed
#   4. grounding IoU      evidence-box overlap when the model emits
#                         coordinates (Phase-2-style models)
#
# A model that memorizes answers shows high stale; a model that truly reads
# evidence shows high follow with low stale.

import argparse
import json


def classify_output(pred_text, factual_answer, cf_answer):
    """Bucket a prediction into follow / stale / other."""
    # --- normalization + matching rules (omitted) ---
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--data", required=True)
    args = ap.parse_args()
    # loop over paired samples, bucket predictions, aggregate three
    # dimensions, dump metrics.json (omitted)


if __name__ == "__main__":
    main()
