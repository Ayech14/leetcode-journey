# 42. Trapping Rain Water

## 🔴 Difficulty

**Hard**

## 🧠 Pattern

**Array + Two Pointers**

## 📌 Problem

Given an array `height` where each value is the height of a bar of width `1`, compute how much rain water is trapped between the bars.

For example:

```text
height = [4, 2, 0, 3, 2, 5]
```

traps `9` units of water.

## 💡 Approach

The water above a single bar depends on the tallest wall on its left and the tallest wall on its right:

```text
water above i = min(left_max, right_max) - height[i]
```

Instead of precomputing both maximums for every position, we use **two pointers** that move towards each other, keeping a running maximum for each side:

1. Start with `left = 0` and `right = len(height) - 1`, and set `left_max`, `right_max` and `water` to `0`.
2. While `left < right`, compare `height[left]` and `height[right]`.
3. If `height[left]` is smaller, the left side is the limiting wall. Everything to the right of `left` has a wall at least as tall as `height[right]`, so only `left_max` matters:
   - update `left_max`
   - add `left_max - height[left]` to `water`
   - move `left` one step right
4. Otherwise do the same on the right side: update `right_max`, add `right_max - height[right]`, and move `right` one step left.
5. Return `water`.

## 🔎 Why Use Two Pointers?

The **shorter** of the two outer walls is always the bottleneck. If `height[left]` is smaller than `height[right]`, we already know a wall at least that tall exists on the right, so the water at `left` is fully determined by `left_max`.

That means we never need to look at the far side's exact maximum, and one pass is enough.

## ⏱️ Complexity

**Time:** `O(n)`

Each step moves one pointer inward, so the pointers cross after at most `n` steps.

**Space:** `O(1)`

We only store a few integers: two pointers, two running maximums and the total.

## 🔑 Key Takeaway

When the answer for each position depends on the best value **on its left and on its right**, two pointers can replace two extra arrays. Always process the side with the smaller wall, because that side is the one whose water level is already known.

This is the same idea as **Container With Most Water**: move the pointer at the shorter wall, because the shorter wall limits the result.

> **Move the pointer at the shorter wall → its water level is already decided.**
