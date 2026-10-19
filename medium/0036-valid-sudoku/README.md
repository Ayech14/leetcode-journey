# 36. Valid Sudoku

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Matrix + Hash Set**

## 📌 Problem

Given a partially filled `9 x 9` Sudoku board, decide whether it is **valid so far**.

Only the filled cells matter. A board is valid when no digit `1-9` repeats in:

- any row,
- any column,
- any of the nine `3 x 3` sub-boxes.

The board does not have to be solvable, we only check that the digits already placed do not break a rule.

For example, if the top-left box contains two `8`s:

```text
8 3 .
6 . .
. 9 8
```

the board is invalid.

## 💡 Approach

Every filled cell belongs to exactly **one row, one column and one box**. So we keep a set of the digits seen so far for each of them:

```python
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]
```

Then we scan the board once:

1. Skip empty cells (`"."`).
2. Work out which box the cell is in:

   ```text
   box = (r // 3) * 3 + c // 3
   ```

   Integer division groups rows and columns into blocks of three, so the boxes are numbered `0-8`, left to right, top to bottom.
3. If the digit is already in `rows[r]`, `cols[c]` or `boxes[box]`, it is a repeat, so return `False`.
4. Otherwise add the digit to all three sets.

If the whole board is scanned without finding a repeat, return `True`.

## 🔎 Why Use Hash Sets?

For each row, column and box, we only need to answer one question: **have I already seen this digit here?**

A set answers that with `O(1)` average-case lookup and insertion, and it cannot hold duplicates by design.

## ⏱️ Complexity

**Time:** `O(1)`

The board is always `9 x 9`, so we visit at most `81` cells, with `O(1)` set operations for each. In terms of an `n x n` board it would be `O(n²)`.

**Space:** `O(1)`

We store at most `81` digits across the `27` sets. For an `n x n` board this would be `O(n²)`.

## 🔑 Key Takeaway

When a rule says "no duplicates within a group", keep **one set per group** and check it before inserting. A single pass is enough, and each cell just has to work out which groups it belongs to.

The only tricky part is mapping a cell to its group, here `(r // 3) * 3 + c // 3` for the box.

This is the same "have I seen it?" idea as **Contains Duplicate** and **Two Sum**, but applied to several groups at once.

> **Find the group each item belongs to → check that group's set → otherwise record the item.**
