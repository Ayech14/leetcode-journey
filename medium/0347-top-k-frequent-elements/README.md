# 347. Top K Frequent Elements

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Hash Map + Bucket Sort**

## 📌 Problem

Given an integer array `nums` and an integer `k`, return the `k` values that appear **most often**. The answer may be returned in any order.

For example:

```text
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

`1` appears 3 times, `2` appears 2 times and `3` appears once, so the answer is `[1, 2]`.

The follow-up asks for a solution that is faster than `O(n log n)`, so simply sorting by frequency is not enough.

## 💡 Approach

1. Count how often each value appears with a dictionary:

```text
value → frequency
```

For the example above:

```text
{1: 3, 2: 2, 3: 1}
```

2. Create a list of buckets where the **index is a frequency**. A value that appears `f` times goes into `buckets[f]`. The list has `len(nums) + 1` buckets because no value can appear more than `len(nums)` times:

```text
buckets[1] = [3]
buckets[2] = [2]
buckets[3] = [1]
```

3. Walk the buckets from the highest frequency down to `1`, adding values to the result. As soon as the result holds `k` values, return it.

Because we visit the most frequent buckets first, the first `k` values we collect are exactly the `k` most frequent ones.

## 🔎 Why Use Bucket Sort?

Sorting the frequencies would cost `O(n log n)`. But frequencies are small whole numbers between `1` and `n`, so we can use them **directly as list indices** instead of comparing them.

Placing each value in its bucket is `O(1)`, and scanning the buckets is `O(n)`, so no comparison sort is needed.

## ⏱️ Complexity

**Time:** `O(n)`

Counting touches each element once, filling the buckets touches each distinct value once, and scanning the buckets visits at most `n + 1` buckets plus the distinct values.

**Space:** `O(n)`

The dictionary holds up to `n` distinct values, and the bucket list has `n + 1` entries.

## 🔑 Key Takeaway

When you need the "top k" by frequency and the frequencies are bounded by the input size, **use the frequency as an index** instead of sorting.

The general pattern is:

> **Count occurrences → group values by their count → read the groups from most frequent to least.**

This builds directly on the frequency counting from **Valid Anagram** (`character → frequency`) and the grouping idea from **Group Anagrams**, where values that share a property are collected together.
