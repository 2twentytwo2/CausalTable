# rl/train_dapo.py — CFRL training core (design sketch)
# ---------------------------------------------------------------------------
# Causal Fine-grained RL for table QA. Base algorithm: DAPO-style policy
# optimization with token-level loss normalization, clip-higher, dynamic
# sampling, and overlong filtering.
#
# The two key causal mechanisms (implementation withheld):
#
#   (1) Mixed factual/counterfactual rollouts per group.
#       Each group of G rollouts contains responses to the SAME question on
#       the factual image and on counterfactually intervened image(s).
#       Within-group normalization A_i = (R_i - mean_g) / std_g therefore
#       credits responses that are correct *for the image they actually saw*.
#
#   (2) Between-condition contrast injected into the advantage.
#       delta_cf = mean_R(factual) - mean_R(counterfactual) is added to the
#       advantage with weight lambda, sharpening the causal signal across
#       conditions rather than only within a group.
#
# Reward (design sketch):
#   R = R_ans + alpha_loc * R_loc + alpha_fmt * R_fmt
#     R_ans : answer correctness against the GT of the *current* image
#             (factual or counterfactual — this is the consistency gate)
#     R_loc : evidence-localization reward, only active when the model has
#             been warm-started on box/coordinate format (otherwise ~0)
#     R_fmt : format constraints (plan/reason/action/answer structure)
#
# Single-round on-policy; no KL-to-reference (entropy monitored only).

import argparse


def compute_reward(rollout, sample, cfg):
    """Per-rollout reward. The GT switch between factual/counterfactual
    conditions is the causal gate of the whole method."""
    # --- reward components (omitted) ---
    raise NotImplementedError


def group_advantages(rewards, is_cf, lam):
    """Within-group normalization + between-condition contrast.

    rewards : per-rollout rewards, G per group
    is_cf   : boolean mask, which rollouts saw the counterfactual image
    lam     : weight of the between-condition contrast delta_cf
    """
    # A_i = (R_i - mu_g) / sigma_g + lam * (mean_f - mean_cf)   (omitted)
    raise NotImplementedError


def dapo_loss(logits, actions, advantages, eps_l, eps_h):
    """Token-level normalized policy loss with clip-higher and dynamic
    sampling (all-correct / all-wrong groups dropped)."""
    # --- loss (omitted) ---
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--algo", default="dapo", choices=["dapo", "grpo"])
    ap.add_argument("--lambda-cf", type=float, default=0.5)
    ap.add_argument("--no-cf", action="store_true", help="pure RL baseline")
    args = ap.parse_args()
    # training loop: sample groups -> mixed rollouts -> reward ->
    # group advantage with contrast -> token-level update (omitted)


if __name__ == "__main__":
    main()
