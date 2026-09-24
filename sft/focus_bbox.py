# sft/focus_bbox.py — SFT step-plan generation from cell annotations (sketch)
# ---------------------------------------------------------------------------
# Before RL, the base VLM is warm-started with a multi-step "focus" format:
# each training trajectory teaches the model to locate critical cells before
# answering. Difficulty tiers (decided by answer-type quantiles):
#
#   direct : easy question  -> no image edit, answer directly
#   single : medium         -> one step locating the critical cells
#   multi  : hard           -> staged: anchor column -> filter rows ->
#                              select answer column -> focus answer cells
#
# Actions are discrete row/column/cell indices (a "multiple choice" over the
# grid) rather than raw coordinates; pixel boxes are attached only for
# rendering the highlighted observation images. This keeps supervision robust
# to rendering style changes.

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class StepPlan:
    step_tag: str            # direct | where_col | filter_row | select_col | aggregate_focus
    edit_instruction: Dict   # {"type": "cells"|"row"|"col", "bbox_list": [...]}
    reason: str
    action_str: str          # JSON: {"type": ..., "idx": [...] | "cells": [[r,c], ...]}
    is_final: bool


def build_step_plans(sample, bbox_cache, mode: str) -> List[StepPlan]:
    """Derive the step sequence from gold evidence cells.

    sample    : QA item with cell-level annotations
    bbox_cache: grid geometry of the rendered table (rows/cols/cells)
    mode      : "direct" | "single" | "multi"
    """
    # --- tier logic + step composition from evidence cells (omitted) ---
    raise NotImplementedError


def main():
    # iterate samples, emit (question, steps, observation images) pairs for
    # SFT training (omitted)
    raise NotImplementedError
