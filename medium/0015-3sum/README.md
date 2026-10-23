# 15. 3Sum

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Sorting + Two Pointers**

## 📌 Problem

Given an integer array `nums`, return all **unique triplets** `[a, b, c]` taken from different positions in the array such that:

```text
a + b + c == 0
```

The answer must not contain duplicate triplets, but the order of the triplets does not matter.

For example:

```text
nums = [-1, 0, 1, 2, -1, -4]
```

produces:

```text
[[-1, -1, 2], [-1, 0, 1]]
```

## 💡 Approach

The idea is to turn 3Sum into many small **Two Sum II** problems on a sorted array.

1. Sort `nums`.
2. Fix the first value `nums[i]`, one index at a time.
3. Place two pointers on the rest of the array: `left = i + 1` and `right = len(nums) - 1`.
4. Look at the sum of the three values:

```text
total = nums[i] + nums[left] + nums[right]
```

- If `total < 0`, the sum is too small, so move `left` right to get a larger value.
- If `total > 0`, the sum is too big, so move `right` left to get a smaller value.
- If `total == 0`, save the triplet, then move both pointers inward.

Because the array is sorted, we can avoid duplicates easily:

- If `nums[i]` is the same as `nums[i - 1]`, skip it. We already tried that first value.
- After saving a triplet, move `left` forward while it points to the same value as before. (Skipping `right` is not needed, because once `left` moves to a new value, the sum can no longer be `0` with the old `right`, and the pointers keep adjusting.)

We can also stop early once `nums[i] > 0`. The array is sorted, so every value after it is positive too, and the sum can never be `0`.

## 🔎 Why Use Sorting + Two Pointers?

A brute-force solution checks every triplet in `O(n³)` time, which is too slow for `3000` elements.

Sorting gives the array an **order we can reason about**:

```text
sum too small → we need a bigger number → move left
sum too big   → we need a smaller number → move right
```

That lets the two pointers find all pairs for a fixed first value in one pass instead of trying every pair. Sorting also puts equal values next to each other, which makes skipping duplicates a simple comparison with the neighbour.

## ⏱️ Complexity

**Time:** `O(n²)`

Sorting costs `O(n log n)`. For each of the `n` choices of the first value, the two pointers walk through the rest of the array once, which is `O(n)`. The `O(n²)` part dominates.

**Space:** `O(1)` extra

Apart from the output list, we only store a few variables. (Sorting is done in place; Python's sort may use up to `O(n)` temporary space internally.)

## 🔑 Key Takeaway

When a problem asks for several numbers that add up to a target, **sort the array, fix one number, and reduce the rest to a two-pointer search**.

This builds directly on earlier problems:

- **Two Sum:** hash map on an unsorted array.
- **Two Sum II:** two pointers on a sorted array.
- **3Sum:** fix one value, then run Two Sum II on what remains.

> **Sort the array → fix one value → squeeze the rest with two pointers → skip duplicates.**
