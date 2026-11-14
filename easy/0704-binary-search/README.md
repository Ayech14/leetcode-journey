# 704. Binary Search

## 🟢 Difficulty

**Easy**

## 🧠 Pattern

**Array + Binary Search**

## 📌 Problem

Given an array `nums` sorted in ascending order and an integer `target`, return the index of `target` in the array, or `-1` if it is not there.

The algorithm must run in `O(log n)` time.

```text
nums = [-1, 0, 3, 5, 9, 12], target = 9  →  4
nums = [-1, 0, 3, 5, 9, 12], target = 2  →  -1
```

## 💡 Approach

Because the array is **sorted**, we can throw away half of the remaining elements after every comparison.

1. Keep two pointers, `left = 0` and `right = len(nums) - 1`. They mark the part of the array where the target could still be.
2. While `left <= right`, look at the middle element:

   ```python
   mid = (left + right) // 2
   ```

3. If `nums[mid] == target`, we found it, so return `mid`.
4. If `nums[mid] < target`, the target must be to the right, so move `left = mid + 1`.
5. Otherwise the target must be to the left, so move `right = mid - 1`.
6. If the pointers cross (`left > right`), no candidates are left, so return `-1`.

## 🔎 Why Use Binary Search?

A linear scan would check every element in `O(n)`.

Sorted order gives us extra information: comparing with the middle value tells us **which half can be ignored**. Halving the search space each step means we need only about `log₂(n)` steps. For 10,000 elements that is roughly 14 comparisons instead of 10,000.

## ⏱️ Complexity

**Time:** `O(log n)`

The search range is cut in half on every iteration.

**Space:** `O(1)`

We only store the `left`, `right` and `mid` indices.

## 🔑 Key Takeaway

Whenever the data is **sorted** (or has a monotonic yes/no property), binary search can find an answer by repeatedly discarding half of the options.

The details that matter are the loop condition `left <= right` and moving the pointers to `mid + 1` / `mid - 1` so the range always shrinks.

> **Look at the middle → decide which half can't contain the answer → discard it → repeat.**
