# Confusion Matrix

Beginner | problemset | classical-ml | metrics

Build the $2\times2$ confusion matrix of binary labels and predictions. Rows are the **actual** class and columns are the **predicted** class.

Implement `solve(y,pred)`.

**Returns.** Return a $2\times2$ integer array `[[TN, FP], [FN, TP]]`.

### Examples

**Example 1**

Input:

```python
solve([0, 1, 1, 0], [0, 1, 0, 1])
```

Output:

```text
[[1, 1], [1, 1]]
```

**Example 2**

Input:

```python
solve([1, 1, 1, 0], [1, 1, 0, 0])
```

Output:

```text
[[1, 0], [1, 2]]
```
