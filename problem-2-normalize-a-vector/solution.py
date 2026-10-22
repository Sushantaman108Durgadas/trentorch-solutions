import numpy as np


def solve(x):
  """Implement Normalize a Vector from the mathematical contract in README.md."""
  arr = np.asarray(x, dtype=float)

  if arr.size == 0:
    raise ValueError("Cannot normalize an empty vector.")

  norm = np.linalg.norm(arr)

  if norm == 0:
    raise ValueError("Cannot normalize a zero vector.")

  return arr / norm
