# 33. Search in Rotated Sorted Array

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Binary Search on a Rotated Array**

## 📌 Problem

We are given a sorted array of **distinct** values that may have been rotated at an unknown position, and a `target`. Return the index of `target`, or `-1` if it is not there. The solution must run in `O(log n)`.

For example:

```text
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

The answer is `4`.

## 💡 Approach

A rotated sorted array is no longer sorted as a whole, but it has a useful property: **if we split it at any middle index, at least one of the two halves is still sorted.**

We run a normal binary search with `left`, `right` and `mid`, and at every step:

1. If `nums[mid] == target`, return `mid`.
2. Find out which half is sorted:
   - If `nums[left] <= nums[mid]`, the **left half** is sorted.
   - Otherwise, the **right half** is sorted.
3. Check whether the target lies inside the sorted half's range:
   - Left half sorted: if `nums[left] <= target < nums[mid]`, search left (`right = mid - 1`), otherwise search right (`left = mid + 1`).
   - Right half sorted: if `nums[mid] < target <= nums[right]`, search right (`left = mid + 1`), otherwise search left (`right = mid - 1`).
4. If the loop ends without finding the target, return `-1`.

The sorted half is the only one where a simple range check can be trusted, so we use it to decide which half can be thrown away.

## ⏱️ Complexity

**Time:** `O(log n)`

Every iteration discards half of the remaining search range.

**Space:** `O(1)`

We only keep three index variables.

## 🔑 Key Takeaway

Binary search does not need the whole array to be sorted. It only needs a way to **safely discard half of the search space**. Here, the sorted half gives us that guarantee.

This builds on **Find Minimum in Rotated Sorted Array**, where we compared `nums[mid]` with `nums[right]` to locate the rotation point. Here we use the same structure to decide which side is ordered.

> **Find the sorted half → check if the target is inside it → otherwise search the other half.**
