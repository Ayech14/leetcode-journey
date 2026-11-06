# 20. Valid Parentheses

## 🟢 Difficulty

**Easy**

## 🧠 Pattern

**Stack**

## 📌 Problem

Given a string `s` made only of the characters `()[]{}`, determine whether it is **valid**.

A string is valid when:

1. Every open bracket is closed by the **same type** of bracket.
2. Brackets are closed in the **correct order**.

For example:

```text
s = "([])"   → true
s = "([)]"   → false
```

In the second string, `]` tries to close `[` while `(` is still waiting to be closed.

## 💡 Approach

The most recently opened bracket must always be the first one closed. That is exactly how a **stack** behaves (last in, first out).

First, create a map from each closing bracket to its opening bracket:

```python
pairs = {")": "(", "]": "[", "}": "{"}
```

Then scan the string from left to right:

1. If the character is an **open** bracket, push it onto the stack.
2. If the character is a **closing** bracket, pop the top of the stack and compare it with the expected opening bracket.
3. If the stack is empty (nothing to close) or the popped bracket does not match, return `False`.

After the scan, every open bracket must have been closed, so the stack has to be empty:

```python
return not stack
```

## 🔎 Why Use a Stack?

Nested brackets are resolved from the **inside out**:

```text
( [ { } ] )
        ↑ closes first
```

The innermost open bracket is the one pushed last, and it is also the one that must be closed first. A stack keeps the open brackets in exactly that order, so the top is always the bracket we are waiting to close.

## ⏱️ Complexity

**Time:** `O(n)`

We visit each character once, and each push, pop and dictionary lookup is `O(1)`.

**Space:** `O(n)`

In the worst case (for example `"((((("`) every character is an open bracket and sits on the stack.

## 🔑 Key Takeaway

When the **most recent unfinished item** must be handled first, such as nested or matching structures, use a stack.

> **Push what you open → pop to match what you close → a valid string leaves nothing behind.**

This is a different kind of "remember what you've seen" from the hash map problems: **Two Sum** stores values so they can be looked up in any order, while here the stack only ever gives access to the latest one, and that restriction is the point.
