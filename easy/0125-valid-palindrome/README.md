# 125. Valid Palindrome

## 🟢 Difficulty

**Easy**

## 🧠 Pattern

**Two Pointers + String**

## 📌 Problem

Given a string `s`, decide whether it is a palindrome after we **ignore everything that is not a letter or digit** and **ignore letter case**.

For example:

```text
s = "A man, a plan, a canal: Panama"
```

becomes:

```text
"amanaplanacanalpanama"
```

which reads the same forwards and backwards, so the answer is `True`.

However:

```text
s = "race a car"
```

becomes `"raceacar"`, which is not a palindrome, so the answer is `False`.

## 💡 Approach

Instead of building a cleaned copy of the string, we compare characters **in place** using two pointers:

1. Put `left` at the start of the string and `right` at the end.
2. While `left < right`:
   - If `s[left]` is not alphanumeric, move `left` forward and continue.
   - Else if `s[right]` is not alphanumeric, move `right` backward and continue.
   - Otherwise both characters matter, so compare them in lowercase:

```python
if s[left].lower() != s[right].lower():
    return False
```

3. If they match, move both pointers inward (`left += 1`, `right -= 1`).
4. If the pointers meet or cross without finding a mismatch, the string is a palindrome, so return `True`.

A string that contains no letters or digits at all (like `" "`) never reaches a comparison, so it correctly returns `True`.

## 🔎 Why Use Two Pointers?

A palindrome is symmetric: the first character must match the last, the second must match the second-to-last, and so on.

Two pointers walking toward each other check exactly those pairs, and they let us **skip irrelevant characters on the fly** without creating a new string.

## ⏱️ Complexity

**Time:** `O(n)`

Each pointer only moves in one direction, so every character is visited at most once.

**Space:** `O(1)`

We only store two integer indices. No cleaned copy of the string is created.

## 🔑 Key Takeaway

When a problem is about **symmetry or comparing both ends of a sequence**, start one pointer at each end and move them toward the middle.

This is the first **Two Pointers** problem in the roadmap. Earlier problems like Two Sum used a hash map to remember what we had seen; here we need no extra memory at all, because the structure of the problem tells us exactly which two positions to compare.

> **Pointers at both ends → skip what doesn't matter → compare → move inward.**
