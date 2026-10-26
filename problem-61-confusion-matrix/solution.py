import numpy as np


def solve(y, pred):
  """Implement Confusion Matrix from the mathematical contract in README.md."""
  y = np.asarray(y, dtype="float")
  pred = np.asarray(pred, dtype="float")

  # Check if shapes match
  if y.shape != pred.shape:
    raise ValueError("y and pred must have the same shape")

  # Reshape 1D arrays to 2D for processing
  if y.ndim == 1:
    y = y.reshape(-1, 1)
    pred = pred.reshape(-1, 1)
  elif y.ndim > 2:
    raise ValueError("Arrays must be 1D or 2D")

  # Check if inputs contain only binary values (0 and 1)
  if not np.all(np.isin(y, [0, 1])) or not np.all(np.isin(pred, [0, 1])):
    raise ValueError("Inputs must contain only binary values (0 and 1)")

  row, col = y.shape
  x = np.array([[0, 0], [0, 0]])

  for i in range(row):
    for j in range(col):
      if y[i, j] == pred[i, j] and y[i, j] == 1:
        x[1, 1] += 1
      elif y[i, j] == pred[i, j] and y[i, j] == 0:
        x[0, 0] += 1
      elif y[i, j] != pred[i, j] and y[i, j] == 0:
        x[0, 1] += 1
      else:
        x[1, 0] += 1

  return x
