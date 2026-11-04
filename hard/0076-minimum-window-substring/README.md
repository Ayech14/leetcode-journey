# 76. Minimum Window Substring

## 🔴 Difficulty

**Hard**

## 🧠 Pattern

**Sliding Window + Hash Map (Frequency Counting)**

## 📌 Problem

Given two strings `s` and `t`, find the **shortest substring of `s`** that contains every character of `t`, including duplicates.

If no such substring exists, return an empty string.

For example:

```text
s = "ADOBECODEBANC"
t = "ABC"
```

The shortest window containing `A`, `B` and `C` is:

```text
"BANC"
```

and for `s = "a"`, `t = "aa"` the answer is `""`, because `s` only has one `a`.

## 💡 Approach

We keep a **window** `s[left..right]` and a frequency map `need` built from `t`:

```text
need = Counter(t)      # character → how many we still need
missing = len(t)       # total characters still missing from the window
```

A count in `need` can go **negative**, which simply means the window holds extra copies of that character.

1. Move `right` one character at a time to expand the window.
2. If `need[char] > 0`, this character was really needed, so `missing -= 1`. Then always do `need[char] -= 1`.
3. When `missing == 0`, the window contains all of `t`. Record it if it is the shortest so far.
4. Now **shrink from the left**: put `s[left]` back with `need[s[left]] += 1`. If that count becomes positive, we just removed a needed character, so `missing += 1` and the window is no longer valid.
5. Keep shrinking while the window stays valid, then continue expanding `right`.
6. At the end, return the best window, or `""` if none was found.

Tracking a single `missing` counter means we never have to compare the whole map on every step.

## 🔎 Why Use a Sliding Window?

A brute force approach checks every substring, which is far too slow for `10^5` characters.

But validity is **monotonic**: if a window is valid, making it bigger keeps it valid, and if it is invalid, making it smaller keeps it invalid. This means we never have to go backwards: `right` only moves forward, `left` only moves forward, and each character is added once and removed once.

## ⏱️ Complexity

**Time:** `O(m + n)`

Building the counter costs `O(n)`. Both `left` and `right` move across `s` at most once, so the scan costs `O(m)`.

**Space:** `O(k)`

where `k` is the number of distinct characters in `t` (plus any others seen in `s`). With only uppercase and lowercase letters this is at most 52, so it is effectively `O(1)` auxiliary space.

## 🔑 Key Takeaway

When a problem asks for the **shortest (or longest) contiguous piece that satisfies a condition**, use a sliding window: expand until the condition holds, then shrink while it still holds.

The frequency-counting idea is the same one used in **Valid Anagram** and **Permutation in String**, but here the window size is not fixed, so the window grows and shrinks as needed.

> **Expand until valid → shrink while valid → remember the best window.**
