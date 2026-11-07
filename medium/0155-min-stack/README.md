# 155. Min Stack

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Stack + Auxiliary Stack (Design)**

## 📌 Problem

Design a stack that supports `push`, `pop`, `top` and `getMin`, where **every operation runs in `O(1)` time**.

The tricky one is `getMin`: after popping, the minimum may change, and we can't afford to scan the stack to find the new one.

```text
push(-2), push(0), push(-3)
getMin() -> -3
pop()
top()    -> 0
getMin() -> -2
```

## 💡 Approach

Keep **two stacks** that always have the same size:

- `stack` holds the values themselves.
- `min_stack` holds, at each position, **the minimum of everything at or below that position**.

1. `push(value)`: append `value` to `stack`. Then append `min(value, min_stack[-1])` to `min_stack` (or just `value` if it is empty).
2. `pop()`: pop from both stacks, so they stay in sync.
3. `top()`: return `stack[-1]`.
4. `getMin()`: return `min_stack[-1]`.

For the example:

```text
stack:      [-2, 0, -3]
min_stack:  [-2, -2, -3]
```

After one `pop()` both lose their last item, and `min_stack[-1]` is `-2` again, which is exactly the minimum of `[-2, 0]`.

## 🔎 Why Use a Second Stack?

The minimum only changes when we push or pop, and both of those happen at the top. So the minimum "so far" at each height never changes once it has been recorded.

Storing it alongside each element means popping simply **reveals the previous answer** instead of recomputing it.

## ⏱️ Complexity

**Time:** `O(1)`

Every method does a constant number of list `append`, `pop` or index operations.

**Space:** `O(n)`

Both stacks hold one entry per pushed element, so we use about twice the memory of a plain stack.

## 🔑 Key Takeaway

When you need a running aggregate (like the minimum) that must survive undoing the latest operation, **store the aggregate together with each element** so that undoing is just popping.

This builds on **Valid Parentheses**, where a stack remembers what is still open; here a stack also remembers what the minimum *was*.

> **Remember the answer at every level → pushing extends it → popping restores it.**
