# 128. Longest Consecutive Sequence

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Array + Hash Set**

## 📌 Problem

Given an unsorted integer array `nums`, return the length of the longest sequence of **consecutive numbers** (like `1, 2, 3, 4`). The numbers do not need to be next to each other in the array, and the algorithm must run in `O(n)` time.

For example:

```text
nums = [100, 4, 200, 1, 3, 2]
```

The longest consecutive sequence is `[1, 2, 3, 4]`, so the answer is `4`.

## 💡 Approach

Sorting would make this easy, but it costs `O(n log n)`. To stay at `O(n)`, we use a **set** for instant membership checks.

1. Put all numbers into a set. This also removes duplicates.
2. For each number in the set, check whether `value - 1` is also in the set.
3. If it is, this number is in the middle of a sequence, so we skip it. Some other number is the start.
4. If it is not, this number is the **start of a sequence**. Count upward while `value + length` is in the set.
5. Keep the largest length found and return it.

For example, with `{100, 4, 200, 1, 3, 2}`:

```text
100 → 99 missing, so start → 101 missing → length 1
4   → 3 exists, skip
200 → 199 missing, so start → length 1
1   → 0 missing, so start → 2, 3, 4 exist → length 4
3   → 2 exists, skip
2   → 1 exists, skip
```

The answer is `4`.

## 🔎 Why Use a Hash Set?

The question we keep asking is **"is this number present?"**

A set answers that in `O(1)` on average, without scanning the array. It also ignores duplicates for free, which is why `[1, 0, 1, 2]` correctly gives `3`.

## ⏱️ Complexity

**Time:** `O(n)`

Building the set is `O(n)`. The inner `while` loop only runs for numbers that start a sequence, so every number is visited by a counting loop at most once overall.

**Space:** `O(n)`

The set can hold every distinct number in the array.

## 🔑 Key Takeaway

Skipping non-starting numbers is what turns a seemingly quadratic "count from every number" idea into a linear one. Each sequence is counted exactly once, from its first element.

Compared to earlier problems, the hash structure is used differently again:

- **Two Sum:** `value → index`
- **Valid Anagram:** `character → frequency`
- **Contains Duplicate:** have we seen this value?
- **Longest Consecutive Sequence:** does the neighbor `value ± 1` exist?

> **Put everything in a set → only start from the beginning of a run → extend while the next value exists.**
