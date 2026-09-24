# CausalTable

**Causal Counterfactual RL for Evidence-Grounded Table Understanding**

CausalTable is a research framework that trains and probes multimodal LLMs to
*read table evidence causally* — not to memorize answers. It couples
counterfactual data interventions, causal advantage shaping in RL, and an
echo-rate analysis protocol that separates genuine perception from prior
memorization.

> **Code status:** this repository currently publishes **design sketches**
> (module contracts + algorithmic outlines). Full runnable implementations,
> rendered datasets, and exact hyperparameters will be released upon paper
> acceptance. See the [Disclaimer](#disclaimer).

---

## 1. Motivation

Table VQA models can score well by exploiting dataset priors: memorized
answers, layout shortcuts, or text-only leakage. We ask a stricter question:

> *If the visual evidence in a table changes, does the model's answer — and
> its cited evidence location — change accordingly?*

CausalTable operationalizes this with three controlled interventions on
annotated table images and trains models whose advantages are shaped by the
*factual/counterfactual contrast itself*.

## 2. The Three Interventions

| Intervention | Operation | Causal change |
|---|---|---|
| **structural** | row/column permutation | evidence coordinates move; content and answer unchanged |
| **semantic** | replace a cell in the answer's causal upstream | answer flips; evidence location unchanged |
| **query** | rewrite the query to point elsewhere | evidence and answer migrate together |

All factual/counterfactual image pairs are **jointly rendered with identical
geometry**, so pixel differences land only on intervened cells. Hard
validation enforces: answer flips where they must, evidence moves where it
must, else the sample is dropped.

## 3. Method Overview

```
                annotated tables (cell-level gold evidence)
                              │
              ┌───────────────┴────────────────┐
              ▼                                ▼
     counterfactual pair builder              SFT warm-start
     (3 interventions + hard checks)          (multi-step focus format)
              │                                │
              └───────────────┬────────────────┘
                              ▼
                   Causal fine-grained RL
        group = rollouts on factual + CF images (same question)
                              │
                              ▼
              ┌───────────────┴────────────────┐
              ▼                                ▼
            MMTab                         TableVista
```

Key design decisions:


- **Between-condition contrast** — the group-mean reward gap
  (factual − counterfactual) is injected into the advantage with weight λ,
  sharpening the causal signal across conditions.
- **Answer-consistency gate** — rewards always check the ground truth of the
  *current* image; repeating the factual answer on a CF image earns nothing.
- **Discrete actions** — evidence is cited as row/column/cell indices
  (a multiple-choice over the grid), robust to rendering style shifts.
- **Invariance control** — answer-preserving shuffles measure over-
  sensitivity, so "follow" gains are not merely layout jitter.

## 4. Evaluation Protocol

1. **External generalization**: MMTab (8 sub-datasets) and TableVista with
   paired McNemar significance tests; perturbation-retention on
   answer-preserving shuffles.
4. **Evidence grounding**: critical-cell exact / ±1-cell tolerant hit rates,
   and box-IoU audits for coordinate-emitting models.


## 6. Repository Layout

```
CausalTable/
├── data/
│   ├── build_cf_data.py        # counterfactual pair construction (3 interventions + hard validation)
│   └── build_perturb_data.py   # answer-preserving perturbation (invariance control)
├── sft/
│   └── focus_bbox.py           # multi-step focus trajectories from cell annotations
├── rl/
│   ├── train_dapo.py           # causal fine-grained RL (mixed groups + contrast injection)
│   └── train_exp4.py           # injection-position ablations (reward/adv/gate/paired)
├── eval/
│   ├── eval_cf.py              # internal causal metrics (follow/stale/other, per-type/per-shift)
│   └── eval_external.py        # MMTab/TableVista + McNemar + perturbation retention
└── analysis/
    ├── causal_effect.py        # follow/invariance/echo probe across VLMs
    ├── critical_cells.py       # cross-model evidence localization benchmark
    └── iou_evidence.py         # evidence-coordinate IoU audits
```

## 7. Requirements (sketch level)

- Python ≥ 3.10, PyTorch ≥ 2.x, transformers, vLLM (batch inference)
- A table-structure OCR model for gold geometry construction (any
  structure-recognition model; see paper for details)
- GPUs: single 80GB card suffices for 7–8B models with LoRA + gradient
  checkpointing

## 8. Disclaimer

This repository documents the **method design and evaluation protocol**.
Runnable code, datasets, and configurations are withheld while the paper is
under review to protect the novelty of the contribution; they will be
released in full upon acceptance. If you wish to compare against this work
before then, please contact the authors.

## License

For research use. License terms finalized with the full release.
