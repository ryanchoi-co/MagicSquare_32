"""Shared grid fixtures (Report/08 G0~G3) — RED skeleton placeholders only.

Uncomment literals when moving from skeleton to full RED/GREEN tests.
"""

from __future__ import annotations

# --- G0: complete 4×4 magic square (Report/08) ---
# GRID_G0: list[list[int]] = [
#     [16, 3, 2, 13],
#     [5, 10, 11, 8],
#     [9, 6, 7, 12],
#     [4, 15, 14, 1],
# ]

# --- G1: partial grid, blanks (2,2) and (3,3) 1-index; Step A golden ---
# GRID_G1: list[list[int]] = [
#     [16, 3, 2, 13],
#     [5, 0, 11, 8],
#     [9, 6, 0, 12],
#     [4, 15, 14, 1],
# ]
# GOLDEN_G1_STEP_A: list[int] = [2, 2, 7, 3, 3, 10]

# --- G2: B-only success [PLACEHOLDER — Report/08, SC-DOM-SOL-001] ---
# GRID_G2: list[list[int]] | None = None  # TBD
# GOLDEN_G2_STEP_B: list[int] = [3, 3, 6, 4, 4, 1]

# --- G3: both placements fail [PLACEHOLDER] ---
# GRID_G3: list[list[int]] | None = None  # TBD
