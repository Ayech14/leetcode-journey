# 239. Sliding Window Maximum

## 🔴 Difficulty

**Hard**

## 🧠 Pattern

**Sliding Window + Monotonic Deque**

## 📌 Problem

Given an integer array `nums` and a window size `k`, slide a window of size `k` from the left of the array to the right, one position at a time.

Return the **maximum value inside the window** at every position.

```text
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

[1  3  -1] -3  5  3  6  7   → 3
 1 [3  -1  -3] 5  3  6  7   → 3
 1  3 [-1  -3  5] 3  6  7   → 5
 1  3  -1 [-3  5  3] 6  7   → 5
 1  3  -1  -3 [5  3  6] 7   → 6
 1  3  -1  -3  5 [3  6  7]  → 7
```

The answer is `[3, 3, 5, 5, 6, 7]`.

## 💡 Approach

Scanning every window to find its maximum costs `O(n * k)`. Instead, we keep a **deque of indices** whose values are in **decreasing order**. The index at the front always points to the maximum of the current window.

For each index `i` and value `num = nums[i]`:

1. **Remove smaller values from the back.** While the last index in the deque has a value `<= num`, pop it. Those values are older *and* smaller than `num`, so they can never be the maximum of any window that contains `num`.
2. **Add the current index** to the back of the deque.
3. **Remove the front if it left the window.** If the front index is `<= i - k`, it is no longer inside the window, so pop it from the left. Only one index can expire per step.
4. **Record the answer.** Once `i >= k - 1`, the first full window exists, so append `nums[window[0]]` to the result.

We store **indices instead of values** so we can tell when the front has slid out of the window.

For example, with `[1, 3, -1]` the deque of values goes:

```text
add 1   → [1]
add 3   → pop 1, then [3]
add -1  → [3, -1]       window is full, max = 3
```

## 🔎 Why Use a Monotonic Deque?

We need to **add new values at one end** and **remove expired or useless values from both ends**.

A `deque` supports `append`, `pop` and `popleft` in `O(1)`, which a list cannot do at the front.

Keeping the deque in decreasing order means the maximum is always sitting at the front, ready to read in `O(1)`.

## ⏱️ Complexity

**Time:** `O(n)`

Each index is appended to the deque once and removed at most once, so the total work over the whole array is linear, even though there is a `while` loop inside the `for` loop.

**Space:** `O(k)`

The deque holds at most `k` indices (the ones inside the current window). The result list needs `O(n - k + 1)` space for the output itself.

## 🔑 Key Takeaway

When a sliding window needs its **maximum (or minimum) at every step**, a monotonic deque lets you discard values that can never be the answer again and keep the best candidate at the front.

This builds on the earlier Sliding Window problems, which only needed counts or a pair of pointers. Here the window also needs to remember **which candidates are still useful**.

> **Pop weaker candidates from the back → pop expired ones from the front → read the max from the front.**
