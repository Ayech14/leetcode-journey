# 3. Longest Substring Without Repeating Characters

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Sliding Window + Hash Map**

## 📌 Problem

Given a string `s`, find the length of the longest **substring** (a continuous part of the string) that has no repeated characters.

For example:

```text
s = "abcabcbb"
```

The longest substring without repeats is `"abc"`, so the answer is `3`.

```text
s = "pwwkew"
```

The answer is `3` (`"wke"`). Note that `"pwke"` is not valid because it is a subsequence, not a substring.

## 💡 Approach

We keep a **window** `[left, right]` that always contains unique characters, and we grow it one character at a time.

We also keep a dictionary that remembers the **last index** where each character was seen:

```text
character → last index
```

For each character at position `right`:

1. Check whether the character was seen before **and** that position is inside the current window (`last_seen[char] >= left`).
2. If so, move `left` to just after that previous occurrence, so the duplicate leaves the window:

```python
left = last_seen[char] + 1
```

3. Record the current index in `last_seen`.
4. The window length is `right - left + 1`; update the best answer if it is larger.

The check `last_seen[char] >= left` matters: a character may have been seen long ago, before the window started. That old occurrence is already outside the window, so it must not move `left` backwards.

Example with `"abba"`:

```text
right=0 'a' → window "a"    → best 1
right=1 'b' → window "ab"   → best 2
right=2 'b' → left jumps to 2, window "b"
right=3 'a' → old 'a' is at 0, outside the window, so left stays 2 → window "ba"
```

## 🔎 Why Use a Sliding Window?

Checking every substring would take `O(n²)` or worse. But when the window is valid and we add one character, we only need to fix the window if that **one new character** creates a duplicate.

Remembering the last index of each character lets us jump `left` forward in a single step instead of shrinking one character at a time. Neither pointer ever moves backwards, so the work stays linear.

## ⏱️ Complexity

**Time:** `O(n)`

`right` visits each character once, and `left` only moves forward. Dictionary lookups and updates are `O(1)` on average.

**Space:** `O(k)`

where `k` is the number of distinct characters in the string. The dictionary stores one entry per distinct character, which is bounded by the character set size.

## 🔑 Key Takeaway

When a problem asks for the best **continuous** section of an array or string that satisfies a rule, keep a window and expand it with a right pointer. When the rule breaks, move the left pointer just far enough to repair it.

The general pattern is:

> **Expand the window → if the rule breaks, move the left edge → track the best window seen.**

This builds on the hash map idea from **Two Sum** and **Valid Anagram**: here the map stores `character → last index`, and it is what lets the window fix itself instantly. It is also a step beyond **Best Time to Buy and Sell Stock**, where one pointer tracked a running minimum, towards windows that grow and shrink.
