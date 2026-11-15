# 74. Search a 2D Matrix

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Binary Search on a Flattened Matrix**

## 📌 Problem

Given an `m x n` matrix where each row is sorted and the first value of every row is greater than the last value of the previous row, decide whether `target` exists in the matrix.

The solution must run in `O(log(m * n))` time.

```text
matrix = [[1,  3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
target = 3   →  true
target = 13  →  false
```

## 💡 Approach

Because each row starts after the previous row ends, reading the matrix row by row gives **one long sorted list**:

```text
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
```

We never build that list. We just run a normal binary search over the **virtual indices** `0` to `rows * cols - 1`.

1. Set `left = 0` and `right = rows * cols - 1`.
2. While `left <= right`, take `mid = (left + right) // 2`.
3. Convert the flat index to matrix coordinates:

```python
value = matrix[mid // cols][mid % cols]
```

4. If `value == target`, return `True`.
5. If `value < target`, the target must be to the right, so `left = mid + 1`.
6. Otherwise it must be to the left, so `right = mid - 1`.
7. If the loop ends, the target is not in the matrix, so return `False`.

## 🔎 Why Use Index Arithmetic?

For a flat index `i` in a matrix with `cols` columns:

```text
row    = i // cols
column = i % cols
```

This lets us treat a 2D structure as a 1D sorted array without copying anything, so the extra space stays constant.

## ⏱️ Complexity

**Time:** `O(log(m * n))`

Each iteration halves the search range, which starts at `m * n` elements.

**Space:** `O(1)`

We only keep a few integer variables.

## 🔑 Key Takeaway

Binary search only needs a **sorted order and a way to read the element at an index**. If a 2D structure is sorted when read in order, map a single index to `(row, column)` and search as usual.

This builds on **Binary Search**, the first problem of this topic, with the only new idea being the index conversion.

> **Find the hidden sorted order → map the index to the data → halve the search range.**
