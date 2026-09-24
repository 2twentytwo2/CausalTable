# eval/eval_external.py — External benchmark evaluation (sketch)
# ---------------------------------------------------------------------------
# Generalization check on public table-VQA benchmarks (MMTab across 8
# sub-datasets; TableVista visual variants). Key design points:
#
#   * Same prompt as internal eval (answer-only, no coordinate request) to
#     avoid confounding format with capability.
#   * Per-sub-dataset accuracy + macro average; McNemar tests for paired
#     model comparisons on the identical sample set.
#   * Perturbation-retention rate: accuracy on answer-preserving shuffles
#     (see data/build_perturb_data.py) — measures whether gains come from
#     reading evidence rather than layout overfitting.
#
# Batch inference utilities (vLLM / KV-cache loaders for different model
# families) are engineering details and omitted.

import argparse


def run_benchmark(model, samples, prompt_mode="answer_only"):
    # --- batched inference + answer extraction + matching (omitted) ---
    raise NotImplementedError


def mcnemar_paired(model_a_preds, model_b_preds, golds):
    """Exact McNemar test on paired correctness."""
    # --- paired test (omitted) ---
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--bench", required=True, choices=["mmtab", "tablevista"])
    args = ap.parse_args()
    # (omitted)


if __name__ == "__main__":
    main()
