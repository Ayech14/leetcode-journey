# 150. Evaluate Reverse Polish Notation

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Stack**

## 📌 Problem

Given an array of strings `tokens` that represents an arithmetic expression in **Reverse Polish Notation** (also called postfix notation), evaluate it and return the integer result.

In this notation, the operator comes **after** its two operands. Valid operators are `+`, `-`, `*` and `/`, and division always **truncates toward zero**.

For example:

```text
tokens = ["4", "13", "5", "/", "+"]
```

means:

```text
4 + (13 / 5) = 4 + 2 = 6
```

## 💡 Approach

Use a stack that holds the operands we have seen but not yet used.

Go through the tokens from left to right:

1. If the token is a number, convert it with `int(token)` and push it onto the stack.
2. If the token is an operator, pop the top two values. The first one popped is the **right** operand and the second is the **left** operand:

```python
right = stack.pop()
left = stack.pop()
```

3. Apply the operator as `left <op> right` and push the result back onto the stack.
4. After the last token, the stack holds exactly one value: the answer.

The order matters for `-` and `/`. For `["3", "5", "-"]` we compute `3 - 5`, not `5 - 3`.

For division we use `int(left / right)` instead of `left // right`. Python's `//` rounds **down** (so `-7 // 2` is `-4`), but the problem wants truncation toward zero (`-7 / 2` becomes `-3`), and `int()` does exactly that.

Example walkthrough with `["2", "1", "+", "3", "*"]`:

```text
push 2          stack: [2]
push 1          stack: [2, 1]
"+"  -> 2 + 1   stack: [3]
push 3          stack: [3, 3]
"*"  -> 3 * 3   stack: [9]
```

## 🔎 Why Use a Stack?

An operator always applies to the **two most recent values** that have not been used yet. That is exactly what a stack gives us: the last value pushed is the first one popped.

Nested expressions resolve themselves naturally. An inner result is pushed back and immediately becomes an operand for the next operator, so we never need parentheses or precedence rules.

## ⏱️ Complexity

**Time:** `O(n)`

Each token is processed once, and every push and pop is `O(1)`.

**Space:** `O(n)`

In the worst case, all the numbers come before the operators, so the stack holds about `n / 2` values.

## 🔑 Key Takeaway

When the most recently seen items are the ones that must be combined or resolved first, a **stack** is the right tool. Postfix notation is the clearest case: operands wait on the stack until their operator arrives.

This builds on **Valid Parentheses** and **Min Stack**: there we stored things to match or look up later, and here we store operands until an operator consumes them.

> **Push operands → on an operator pop two → compute → push the result back.**
