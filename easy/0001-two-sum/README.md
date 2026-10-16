# 1. Two Sum

## 🟢 Difficulty

**Easy**

## 🧠 Pattern

**Array + Hash Map**

## 📌 Problem

Given an integer array `nums` and an integer `target`, find two different indices whose corresponding values add up to `target`.

Return the two indices.

## 💡 Approach

For each element in the array, calculate its **complement**:

```text
complement = target - current_value
```

The complement is the value we need to find in order for the current value to reach the target.

We store previously visited values and their indices in a hash map (`dict`).

For each element:

1. Calculate the complement.
2. Check whether the complement is already in the hash map.
3. If it is, we found the required pair and return both indices.
4. If it is not, store the current value and its index in the hash map.

This allows us to find the required pair without checking every possible combination.

## ⏱️ Complexity

**Time:** `O(n)`

We traverse the array once, and dictionary lookup is `O(1)` on average.

**Space:** `O(n)`

In the worst case, we store every element in the hash map.

## 🔑 Key Takeaway

When a problem asks us to find a value that complements the current value to reach a target, a **hash map can provide fast lookup** and reduce a brute-force `O(n²)` solution to `O(n)`.

The general pattern is:

> **Calculate what you need → check whether you've seen it → otherwise remember what you have.**
