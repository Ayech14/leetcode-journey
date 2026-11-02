# 567. Permutation in String

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Sliding Window + Frequency Counting**

## 📌 Problem

Given two strings `s1` and `s2`, return `True` if `s2` contains a **permutation** of `s1` as a substring.

A permutation uses the **same characters with the same frequencies**, in any order.

For example:

```text
s1 = "ab"
s2 = "eidbaooo"
```

`s2` contains `"ba"`, which is a permutation of `"ab"`, so the answer is `True`.

```text
s1 = "ab"
s2 = "eidboaoo"
```

No substring of length 2 uses exactly one `a` and one `b`, so the answer is `False`.

## 💡 Approach

A permutation of `s1` always has the **same length as `s1`**, so we only need to look at windows of that exact length inside `s2`.

Two strings are permutations of each other exactly when their character counts match (just like in Valid Anagram). Since the strings contain only lowercase letters, we use arrays of size 26 as frequency tables.

1. If `s1` is longer than `s2`, return `False`.
2. Build `need`, the letter counts of `s1`.
3. Slide a window across `s2`. For each `right` index, add `s2[right]` to `window`.
4. Once the window has grown past `len(s1)` characters, remove the character that just left it, `s2[right - len(s1)]`.
5. If `window == need`, the current window is a permutation of `s1`, so return `True`.
6. If we reach the end without a match, return `False`.

```python
window[ord(s2[right]) - ord("a")] += 1
if right >= len(s1):
    window[ord(s2[right - len(s1)]) - ord("a")] -= 1
if window == need:
    return True
```

Instead of recounting every substring from scratch, we **update the counts by one character in and one character out**.

## 🔎 Why Use a Fixed-Size Window?

We know exactly how long a matching substring must be, so the window never needs to grow or shrink freely. It simply **moves one step at a time**, and each step changes the counts in `O(1)`.

Comparing two arrays of 26 numbers is also `O(1)`, because 26 is a constant.

## ⏱️ Complexity

**Time:** `O(n + m)`

where `n = len(s1)` and `m = len(s2)`. We count `s1` once, then move across `s2` once. Each step updates two counters and compares two arrays of length 26, which is constant work.

**Space:** `O(1)`

We only keep two arrays of 26 integers, no matter how long the strings are.

## 🔑 Key Takeaway

When a problem asks whether a substring has **the same character makeup** as another string, combine frequency counting with a fixed-size sliding window:

- **Valid Anagram:** compare the counts of two whole strings
- **Permutation in String:** compare the counts of `s1` with every window of `s2`

> **Fix the window size → add the new character, remove the old one → compare the counts.**
