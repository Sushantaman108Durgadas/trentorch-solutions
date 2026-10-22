import numpy as np


def solve(A, steps=100):
  arr = np.asarray(A, dtype=float)
  row = arr.shape[0]
  new_arr = np.ones(row)

  for i in range(steps):
    # 1. Multiply matrix by vector
    new_arr = arr @ new_arr

    # 2. Find the norm
    norm = np.linalg.norm(new_arr)

    # 3. Handle zero vectors to avoid division by zero
    if norm == 0:
      break

    # 4. Normalize *inside* the loop at every step
    new_arr = new_arr / norm

  return new_arr
