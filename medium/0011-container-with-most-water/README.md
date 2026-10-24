# 11. Container With Most Water

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Array + Two Pointers**

## 📌 Problem

Given an array `height`, each value is the height of a vertical line at that index. Pick two lines that, together with the x-axis, form a container holding the most water.

The water level is limited by the **shorter** of the two lines, and the width is the distance between their indices.

```text
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

The lines with heights `8` (index 1) and `7` (index 8) give:

```text
width = 8 - 1 = 7
area  = 7 * min(8, 7) = 49
```

## 💡 Approach

Checking every pair of lines works but takes `O(n²)`. Instead, start with the **widest** container and shrink it smartly.

1. Put `left` at the first index and `right` at the last index, and set `best = 0`.
2. While `left < right`:
   - Compute `width = right - left`.
   - Compute the area `width * min(height[left], height[right])` and update `best`.
   - Move the pointer that points at the **shorter** line inward.
3. Return `best`.

Why move the shorter line? The area is capped by the shorter line. If we moved the taller one instead, the width would shrink while the cap stays the same or gets lower, so the area could never improve. Moving the shorter line is the only move that might find a taller wall.

```python
if height[left] < height[right]:
    left += 1
else:
    right -= 1
```

## 🔎 Why Use Two Pointers?

The pointers start at the extremes, where the width is largest. Every step reduces the width by exactly `1`, so the only way to do better is to find a taller shorter-side.

Each step safely rules out every container that uses the shorter line with any narrower partner, so we never skip the best answer while looking at each index only once.

## ⏱️ Complexity

**Time:** `O(n)`

The two pointers move toward each other and each step moves one of them, so we make at most `n - 1` steps.

**Space:** `O(1)`

We only store a few integer variables.

## 🔑 Key Takeaway

When you search for the best pair in an array, start with the widest pair and use a **greedy rule** to decide which pointer to move. Discarding the side that cannot lead to a better answer turns an `O(n²)` search into `O(n)`.

This builds on **Two Sum II** and **Valid Palindrome**, where pointers also walk inward from both ends, but here the decision is based on which line is limiting the area.

> **Start wide → measure the area → move the limiting (shorter) side inward.**
