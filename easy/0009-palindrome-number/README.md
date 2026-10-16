# 9. Palindrome Number

## 🟢 Difficulty

**Easy**

## 🧠 Pattern

**Math + Digit Manipulation**

## 📌 Problem

Given an integer `x`, determine whether it is a **palindrome**.

A palindrome reads the same from left to right and right to left.

For example:

```text
121 → palindrome
123 → not a palindrome
```

## 💡 Approach

We rebuild the number backwards, one digit at a time, and then compare it with the original.

First, two cases can be rejected immediately:

1. **Negative numbers** are never palindromes, because the minus sign only appears on the left (`-121` reads as `121-` backwards).
2. **Numbers that end in `0`** (except `0` itself) are never palindromes, because the reversed number would have to start with `0` (`10` → `01`).

For every other number:

1. Take the last digit with `number % 10`.
2. Append it to the reversed number with `reverse = reverse * 10 + digit`.
3. Remove the last digit from `number` with `number // 10`.
4. Repeat until no digits are left.
5. Return whether the reversed number equals the original `x`.

For example, with `x = 121`:

```text
digit = 1 → reverse = 1    number = 12
digit = 2 → reverse = 12   number = 1
digit = 1 → reverse = 121  number = 0   → stop
121 == 121 → palindrome
```

Python integers do not overflow, so the reversed number is always safe to build.

## ⏱️ Complexity

**Time:** `O(log x)`

We process one digit per loop iteration, and a number `x` has about `log10(x)` digits.

**Space:** `O(1)`

We only keep a few integer variables, no matter how large `x` is.

## 🔑 Key Takeaway

`% 10` reads the last digit and `// 10` removes it. Together they let you take a number apart, and `reverse * 10 + digit` puts it back together in the opposite order, without converting it to a string.

> **Peel digits off with `% 10` and `// 10` → rebuild with `* 10 + digit` → compare.**
