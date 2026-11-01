# 424. Longest Repeating Character Replacement

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Sliding Window + Hash Map**

## 📌 Problem

Given a string `s` of uppercase letters and an integer `k`, you may change at most `k` characters to any other letter.

Return the length of the **longest substring that can be made of one repeated letter**.

For example:

```text
s = "AABABBA"
k = 1
```

Changing the middle `A` to `B` gives `"AABBBBA"`, which contains `"BBBB"` of length `4`.

## 💡 Approach

The key observation is about any window (substring) of `s`:

```text
replacements needed = window size - count of the most common letter
```

Keep the most common letter and replace everything else. The window is valid when this number is at most `k`.

So we slide a window `[left, right]` across the string:

1. Move `right` forward one character at a time and add `s[right]` to a frequency dictionary `count`.
2. Update `max_freq`, the highest frequency we have seen in any window so far.
3. If the window needs more than `k` replacements, shrink it from the left:

```python
while (right - left + 1) - max_freq > k:
    count[s[left]] -= 1
    left += 1
```

4. After the window is valid, update `best` with its size.

`max_freq` is never decreased when the window shrinks. That is fine: the window only matters when it grows beyond the best size so far, and that can only happen when a new, higher `max_freq` is reached. A stale `max_freq` can never make us record a window larger than a real answer.

## 🔎 Why Use a Sliding Window?

We are looking for the best **contiguous** substring, and validity depends only on the window's letter counts.

Instead of checking every substring (`O(n²)` windows), we extend the right edge and only move the left edge forward when the window becomes invalid. Each index enters and leaves the window at most once.

## ⏱️ Complexity

**Time:** `O(n)`

Both `left` and `right` only move forward, so each character is added once and removed at most once.

**Space:** `O(k)`

where `k` is the number of distinct letters. Since the input is uppercase English letters, this is at most 26, so it is `O(1)` auxiliary space.

## 🔑 Key Takeaway

When a problem asks for the longest substring that satisfies a condition you can measure from counts, use a **sliding window with a frequency map**: expand the right side, and shrink the left side when the condition breaks.

The condition here is a small formula:

```text
window size - most frequent count <= k
```

This builds on **Longest Substring Without Repeating Characters**, where the window was kept valid by removing duplicates. Here the window is kept valid by limiting how many characters are "wrong".

> **Expand the window → check whether it is still valid → otherwise shrink it from the left.**
