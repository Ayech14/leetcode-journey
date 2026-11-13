# 84. Largest Rectangle in Histogram

## 🔴 Difficulty

**Hard**

## 🧠 Pattern

**Array + Monotonic Stack**

## 📌 Problem

Given an array `heights` where each value is the height of a histogram bar (every bar has width `1`), return the **area of the largest rectangle** that fits inside the histogram.

For example:

```text
heights = [2, 1, 5, 6, 2, 3]
```

The largest rectangle uses the bars with heights `5` and `6`. It is `5` tall and `2` wide, so its area is:

```text
5 × 2 = 10
```

## 💡 Approach

Every maximal rectangle is limited by its **shortest bar**. So for each bar, we want to know how far it can stretch to the left and to the right before meeting a shorter bar.

We keep a stack of `(start index, height)` pairs, where the heights are **strictly increasing** from bottom to top. Each pair means: "a rectangle of this height could start at this index and is still growing."

For each bar `h` at index `i`:

1. Set `start = i`.
2. While the top of the stack is **taller than or equal to** `h`, pop it. That bar can't grow past index `i`, so its rectangle is finished:

```text
area = height * (i - index)
```

3. Because the current bar is at least as short as the popped bar, it can reach back to where the popped bar started, so set `start = index`.
4. Push `(start, h)`.

After the loop, the bars still on the stack were never blocked by a shorter bar on the right, so they extend to the end of the histogram:

```text
area = height * (len(heights) - index)
```

The answer is the largest area seen.

Walking through `[2, 1, 5, 6, 2, 3]`:

```text
i=0  push (0, 2)
i=1  h=1: pop (0, 2) → area 2×1 = 2, push (0, 1)
i=2  push (2, 5)
i=3  push (3, 6)
i=4  h=2: pop (3, 6) → area 6×1 = 6
          pop (2, 5) → area 5×2 = 10, push (2, 2)
i=5  push (5, 3)
end  (0,1) → 1×6 = 6, (2,2) → 2×4 = 8, (5,3) → 3×1 = 3
```

The best area is `10`.

## 🔎 Why Use a Monotonic Stack?

The question for each bar is "where is the **nearest shorter bar** on each side?"

A brute force would scan outwards from every bar, which is `O(n²)`.

A stack that keeps heights in increasing order answers this for us. A bar stays on the stack until a shorter bar shows up, and that moment is exactly when its right edge is found. Its left edge is the start index we saved when it was pushed.

## ⏱️ Complexity

**Time:** `O(n)`

Every bar is pushed onto the stack once and popped at most once, so the total work is linear.

**Space:** `O(n)`

In the worst case (strictly increasing heights), every bar stays on the stack.

## 🔑 Key Takeaway

When a problem asks for the **nearest smaller (or greater) element** on either side, a **monotonic stack** finds all of them in a single pass.

This builds on earlier stack problems in this repo:

- **Daily Temperatures:** the stack holds days waiting for a warmer day.
- **Car Fleet:** the stack holds fleets, and a new car either merges or starts a new one.
- **Largest Rectangle in Histogram:** the stack holds bars waiting for a shorter bar, and the start index lets a new bar inherit the width of the bars it popped.

> **Keep the stack ordered → when the order breaks, finish what was popped → let the new bar inherit the popped start.**
