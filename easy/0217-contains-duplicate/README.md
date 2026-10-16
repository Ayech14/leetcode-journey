# 217. Contains Duplicate

## 🟢 Difficulty

**Easy**

## 🧠 Pattern

**Array + Hash Set**

## 📌 Problem

Given an integer array `nums`, return `true` if any value appears at least twice in the array. Otherwise, return `false`.

## 💡 Approach

We iterate through the array while maintaining a **set** containing the values we have already encountered.

For each number:

1. Check whether the number is already in the set.
2. If it is, we have found a duplicate, so return `true`.
3. If it is not, add the number to the set.
4. If we finish the entire array without finding a duplicate, return `false`.

A set is used because we only need to know whether a value has appeared before. We do not need to store an index or any additional information about the value.

Sets are implemented using a hash-table-based structure, which provides **O(1) average-case membership lookup**.

## 🔎 Why Use a Set?

A list can also solve this problem:

```python
if num in seen:
    return True

seen.append(num)
```

The result is correct, but checking `num in seen` on a **list** has to look at the elements one by one, which costs `O(n)` for every check. Over the whole array that becomes `O(n²)`.

A **set** answers the same question in `O(1)` on average, so the whole solution drops to `O(n)`.

## ⏱️ Complexity

**Time:** `O(n)`

We traverse the array once, and each set lookup and insertion is `O(1)` on average.

**Space:** `O(n)`

In the worst case, every value is different and the set stores all `n` of them.

## 🔑 Key Takeaway

When a problem asks whether something has been seen before, a **hash set** gives constant-time membership checks.

Compared with Two Sum, which stored `value → index` in a dictionary, here we only need to know that a value exists, so a set is enough.

> **Check whether you've seen it → if yes, you're done → if not, remember it.**
