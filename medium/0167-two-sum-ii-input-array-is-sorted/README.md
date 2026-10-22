# 167. Two Sum II - Input Array Is Sorted

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Two Pointers (Sorted Array)**

## 📌 Problem

Given a **sorted** array `numbers` and an integer `target`, find the two different positions whose values add up to `target`.

Return those positions as a **1-indexed** pair `[index1, index2]`.

The solution must use only **constant extra space**.

For example:

```text
numbers = [2, 7, 11, 15]
target  = 9
```

`2 + 7 = 9`, so the answer is `[1, 2]`.

## 💡 Approach

In Two Sum we used a hash map. Here that would cost `O(n)` extra space, which the problem forbids. But the array is **sorted**, and that lets us use two pointers instead.

1. Put `left` at the start of the array and `right` at the end.
2. Add the two values: `total = numbers[left] + numbers[right]`.
3. If `total == target`, we are done. Return `[left + 1, right + 1]` (the `+ 1` is because the answer is 1-indexed).
4. If `total < target`, the sum is too small. Move `left` one step right to get a larger value.
5. If `total > target`, the sum is too big. Move `right` one step left to get a smaller value.
6. Repeat while `left < right`.

For `[2, 7, 11, 15]` and `target = 9`:

```text
2 + 15 = 17  → too big, move right
2 + 11 = 13  → too big, move right
2 +  7 =  9  → found → [1, 2]
```

## 🔎 Why Use Two Pointers?

Because the array is sorted, every move tells us something for certain:

- Moving `left` right can only **increase** the sum.
- Moving `right` left can only **decrease** the sum.

When the sum is too big, the current `right` value can never work with *any* remaining `left` value (they are all at least as large as the current one), so we can safely discard it. The same reasoning applies to `left` when the sum is too small.

Each step throws away one candidate for good, so we never need to check every pair.

## ⏱️ Complexity

**Time:** `O(n)`

Each pointer only moves in one direction, so together they move at most `n` times.

**Space:** `O(1)`

We only store two indices and the current sum.

## 🔑 Key Takeaway

When an array is **already sorted** and you are searching for a pair, two pointers from both ends can replace both brute force (`O(n²)`) and a hash map (`O(n)` space).

Compare with the earlier problem in this repo:

- **Two Sum:** unsorted → hash map (`value → index`), `O(n)` space
- **Two Sum II:** sorted → two pointers, `O(1)` space

> **Sorted + looking for a pair → compare the sum to the target → move the pointer that fixes it.**
