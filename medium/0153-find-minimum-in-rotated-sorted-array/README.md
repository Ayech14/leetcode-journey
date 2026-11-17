# 153. Find Minimum in Rotated Sorted Array

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Binary Search on a Rotated Array**

## 📌 Problem

A sorted array of unique numbers has been rotated, so some suffix was moved to the front. Find the **minimum element** in `O(log n)` time.

```text
nums = [4, 5, 6, 7, 0, 1, 2]
```

The original array was `[0, 1, 2, 4, 5, 6, 7]`, so the answer is `0`.

## 💡 Approach

A rotated sorted array is made of two sorted pieces, and the minimum is the **start of the second piece** (the point where the values drop).

```text
[4, 5, 6, 7 | 0, 1, 2]
```

We compare the middle element with the **rightmost** element of the current range to learn which piece `mid` is in.

1. Set `left = 0` and `right = len(nums) - 1`.
2. While `left < right`, take `mid = (left + right) // 2`.
3. If `nums[mid] > nums[right]`, then `mid` is in the left (larger) piece and the drop is somewhere to its right. The minimum must be after `mid`, so `left = mid + 1`.
4. Otherwise `nums[mid] < nums[right]`, so everything from `mid` to `right` is sorted. The minimum is `mid` or something to its left, so `right = mid` (we keep `mid` because it might be the answer).
5. When `left == right`, that index holds the minimum, so return `nums[left]`.

Since all values are unique, `nums[mid] == nums[right]` only happens when `mid == right`, which the `left < right` loop never allows.

## 🔎 Why Compare with the Right End?

The left end is not a reliable reference: if the array was not really rotated, `nums[mid] > nums[left]` is true yet the minimum is on the left.

The right end works in every case, because the minimum is always **at or before** the right end of any range that contains it:

```text
nums[mid] > nums[right]  ->  the drop is between mid and right  ->  go right
nums[mid] < nums[right]  ->  mid..right is sorted               ->  go left (keep mid)
```

## ⏱️ Complexity

**Time:** `O(log n)`

Each step discards half of the remaining range.

**Space:** `O(1)`

We only keep the `left`, `right` and `mid` integers.

## 🔑 Key Takeaway

Binary search does not need a fully sorted array. It only needs a check that tells you **which half cannot contain the answer**. Here, comparing `nums[mid]` with `nums[right]` gives that check.

This builds on **Binary Search** and **Koko Eating Bananas**: the same `left` / `right` / `mid` loop with `right = mid` to keep a possible answer, instead of looking for an exact match.

> **Compare the middle with the right end → move toward the drop → stop when the range is one element.**
