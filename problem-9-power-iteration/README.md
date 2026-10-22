# Power Iteration

Advanced | problemset | maths-stats-for-ml | eigenvalues

Estimate the dominant eigenvector of a symmetric matrix with power iteration: repeatedly multiply a vector by the matrix and renormalize it.

Implement `solve(A, steps=100)`.

**Returns.** Return a unit-length NumPy vector after `steps` iterations (default 100), starting from the all-ones vector. If an iterate becomes the zero vector (for example for the zero matrix) it is returned as is. The overall sign depends on the starting vector.

### Examples

**Example 1**

Input:

```python
solve([[2.0, 0.0], [0.0, 1.0]])
```

Output:

```text
[1.0, 0.0]
```

**Example 2**

Input:

```python
solve([[2.0, 1.0], [1.0, 2.0]])
```

Output:

```text
[0.707107, 0.707107]
```
