# rl/train_exp4.py — Where to inject the counterfactual signal? (ablation sketch)
# ---------------------------------------------------------------------------
# Question: the counterfactual sensitivity signal can enter the learning
# pipeline at different points. We compare four injection positions with the
# SAME total signal budget:
#
#   reward : shift the per-rollout reward (factual vs. CF baselines differ)
#   adv    : inject the between-condition contrast into the advantage
#            (the default CFRL design)
#   gate   : modulate how much of the reward is counted by an
#            "informativeness gate" (e.g., agreement-dependent weighting)
#   paired : per-identity paired difference — compare each factual rollout
#            with its counterfactual twin directly, learn from the delta
#
# Finding (summary): under matched budgets the four positions are
# statistically indistinguishable on accuracy; the choice is not the
# bottleneck. This motivated our shift of attention to evidence grounding
# (see analysis/).
#
# Implementation (group construction, gate functions, paired estimators)
# omitted.

import argparse


def make_injection(kind: str):
    """Return the (reward_fn, advantage_fn) pair for the given position."""
    # --- four injection variants (omitted) ---
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", required=True,
                    choices=["reward", "adv", "gate", "paired"])
    ap.add_argument("--data", required=True)
    args = ap.parse_args()
    # shared training loop with pluggable injection (omitted)


if __name__ == "__main__":
    main()
