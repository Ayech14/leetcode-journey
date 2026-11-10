# 739. Daily Temperatures

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Array + Monotonic Stack**

## 📌 Problem

Given an array `temperatures`, return an array `answer` where `answer[i]` is the number of days you must wait after day `i` to get a **warmer** temperature. If no warmer day ever comes, `answer[i]` is `0`.

```text
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer       = [ 1,  1,  4,  2,  1,  1,  0,  0]
```

Day `2` (75) has to wait 4 days until day `6` (76), so `answer[2] = 4`.

## 💡 Approach

Checking every later day for each day would be `O(n²)`. Instead, we walk through the days once and keep a **stack of indices of days that are still waiting for a warmer day**.

The temperatures of the days on the stack are always **decreasing** from bottom to top (this is why it is called a *monotonic* stack). If a day were warmer than the one below it, that lower day would already have been answered.

1. Create `answer` filled with `0` (the default when no warmer day exists) and an empty `stack`.
2. For each day `i` with temperature `temp`:
   1. While the stack is not empty and the day on top is **colder** than `temp`, pop it as `prev`. Today is its first warmer day, so set `answer[prev] = i - prev`.
   2. Push `i` onto the stack, because today is now waiting for a warmer day.
3. Any index left on the stack never found a warmer day, so its answer stays `0`.

```text
temps = [73, 74, 75, 71, 69, 72, 76, 73]

i=0 push 0              stack: [0]
i=1 74 > 73 -> ans[0]=1 stack: [1]
i=2 75 > 74 -> ans[1]=1 stack: [2]
i=3 71          push    stack: [2, 3]
i=4 69          push    stack: [2, 3, 4]
i=5 72 > 69 -> ans[4]=1, 72 > 71 -> ans[3]=2   stack: [2, 5]
i=6 76 > 72 -> ans[5]=1, 76 > 75 -> ans[2]=4   stack: [6]
i=7 73          push    stack: [6, 7]
```

## 🔎 Why Use a Stack?

The days waiting for an answer are resolved in **reverse order of arrival**: the most recent (and coldest) waiting day is the first one a warmer temperature can satisfy. That last-in, first-out behaviour is exactly what a stack gives us.

Storing **indices** instead of temperatures lets us both look up the temperature (`temperatures[index]`) and compute the number of days waited (`i - prev`).

## ⏱️ Complexity

**Time:** `O(n)`

Each day is pushed onto the stack once and popped at most once, so the total work across the loop is linear even though there is a `while` inside the `for`.

**Space:** `O(n)`

In the worst case (strictly decreasing temperatures) every index stays on the stack, and the `answer` array also holds `n` values.

## 🔑 Key Takeaway

When a problem asks, for each element, for the **next greater (or smaller) element**, use a **monotonic stack**: keep unresolved elements on the stack and resolve them as soon as a qualifying element arrives.

It is a step up from earlier stack problems like **Valid Parentheses** and **Min Stack**: there the stack only remembered things, here it also decides *when* an earlier element gets its answer.

> **Keep unanswered items on a stack → when a new item beats them, pop and answer them → push the new item.**
