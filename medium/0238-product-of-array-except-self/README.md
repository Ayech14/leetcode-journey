# 238. Product of Array Except Self

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Array + Prefix/Suffix Products**

## 📌 Problem

Given an integer array `nums`, return an array `answer` where `answer[i]` is the product of **every element except `nums[i]`**.

The catch: it must run in `O(n)` time and **without using division**.

For example:

```text
nums   = [1, 2, 3, 4]
answer = [24, 12, 8, 6]
```

because `answer[0] = 2 * 3 * 4 = 24`, `answer[1] = 1 * 3 * 4 = 12`, and so on.

## 💡 Approach

The product of everything except `nums[i]` is really two pieces multiplied together:

```text
answer[i] = (product of elements left of i) * (product of elements right of i)
```

We can build both pieces with two simple passes, reusing the output array so we need no extra arrays.

1. Create `answer = [1] * n`.
2. **Left to right:** keep a running `prefix` (starting at `1`). For each index `i`, store `answer[i] = prefix`, then multiply `prefix` by `nums[i]`. Now `answer[i]` holds the product of everything to the left of `i`.
3. **Right to left:** keep a running `suffix` (starting at `1`). For each index `i`, multiply `answer[i]` by `suffix`, then multiply `suffix` by `nums[i]`. Now `answer[i]` also includes everything to the right of `i`.
4. Return `answer`.

For `[1, 2, 3, 4]`:

```text
after left pass:   [1, 1, 2, 6]
after right pass:  [24, 12, 8, 6]
```

Notice that `nums[i]` itself is never multiplied into `answer[i]`, because we store the running product *before* including the current element. Zeros need no special handling either.

## 🔎 Why Use Prefix and Suffix Products?

Division would be the obvious shortcut (total product divided by `nums[i]`), but it breaks when the array contains zeros and the problem forbids it anyway.

Prefix and suffix products give us the same information without division: each one is built incrementally in `O(1)` per step, so we never recompute a product from scratch.

## ⏱️ Complexity

**Time:** `O(n)`

We make two passes over the array, and each step is a constant-time multiplication.

**Space:** `O(1)`

Not counting the output array, we only use the two variables `prefix` and `suffix`.

## 🔑 Key Takeaway

When the answer for each position depends on **"everything before" and "everything after"**, precompute those two sides with running values from each direction and combine them.

The general pattern is:

> **Sweep from the left to collect what is before → sweep from the right to collect what is after → combine both.**

Compared to earlier Arrays & Hashing problems, this one needs no hash map at all: the trick is carrying information along the array in a running variable instead of looking it up.
