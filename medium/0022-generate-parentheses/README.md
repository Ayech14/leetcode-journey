# 22. Generate Parentheses

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Stack + Backtracking**

## 📌 Problem

Given `n` pairs of parentheses, generate **all combinations of well-formed parentheses**.

A string is well-formed when every `(` is closed by a matching `)` and no `)` appears before its `(`.

For example:

```text
n = 3
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

## 💡 Approach

Instead of generating every string of length `2n` and filtering the invalid ones, we **only build valid strings**.

We keep:

- `stack` — the parentheses chosen so far
- `opened` — how many `(` are in the stack
- `closed` — how many `)` are in the stack

The recursive function `build(opened, closed)` follows two rules:

1. **Add `(` only if `opened < n`.** We still have pairs left to open.
2. **Add `)` only if `closed < opened`.** There must be an unmatched `(` to close.

Each choice is made with the same three moves:

```python
stack.append("(")
build(opened + 1, closed)
stack.pop()
```

The `pop()` undoes the choice (this is the **backtracking** part) so the next branch starts from the same state.

When `closed == n`, the stack holds a complete, valid string. We join it and add it to `result`.

For `n = 2` the choices look like this:

```text
(            -> ((  -> (()  -> (())
                    -> ()  -> ()()
```

## 🔎 Why Use a Stack?

Well-formed parentheses behave like a stack: the most recent `(` must be the first one closed.

The two counters capture exactly that rule. `closed < opened` means the stack of unmatched `(` is not empty, so closing is allowed.

## ⏱️ Complexity

**Time:** `O(4^n / sqrt(n))`

The number of valid strings is the n-th Catalan number, which grows like `4^n / n^(3/2)`. Each string takes `O(n)` to build and join, giving about `4^n / sqrt(n)` overall.

**Space:** `O(n)`

Not counting the output, the recursion depth and the stack are at most `2n`.

## 🔑 Key Takeaway

When a problem asks for **all valid combinations**, don't generate everything and filter. Make a choice, check a simple rule, recurse, then undo the choice.

The rule here is just two counters, which keeps invalid prefixes from ever being built.

This extends **Valid Parentheses**, where we used a stack to *check* a string. Here we use the same balance idea to *generate* strings.

> **Choose → check the rule → recurse → undo the choice.**
