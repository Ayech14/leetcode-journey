# 242. Valid Anagram

## 🟢 Difficulty

**Easy**

## 🧠 Pattern

**Hash Map + Frequency Counting**

## 📌 Problem

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

Two strings are anagrams if they contain the **same characters with the same frequencies**.

For example:

```text
s = "anagram"
t = "nagaram"
```

Both strings contain:

```text
a → 3
n → 1
g → 1
r → 1
m → 1
```

so they are anagrams.

However:

```text
s = "aab"
t = "abb"
```

are not anagrams because their character frequencies differ.

## 💡 Approach

First, compare the lengths of the two strings.

If their lengths are different, they cannot be anagrams:

```python
if len(s) != len(t):
    return False
```

Next, create a dictionary to store the frequency of each character in `s`.

The dictionary uses:

```text
character → frequency
```

For example:

```text
"aab"
```

produces:

```text
{
    "a": 2,
    "b": 1
}
```

We then iterate through `t` and subtract `1` from the corresponding character count.

If a character in `t` does not exist in the dictionary, the strings cannot be anagrams.

After processing both strings, every frequency should be exactly `0`.

If any value is not `0`, the character frequencies are different, so we return `False`.

Otherwise, the strings are anagrams.

## 🔎 Why Use a Hash Map?

We need to keep track of **how many times each character appears**.

A dictionary is useful because it lets us associate each character with its frequency:

```text
character → number of occurrences
```

For example:

```python
count["a"] = 3
```

means that we have seen `"a"` three times.

The dictionary provides **O(1) average-case lookup and update**, allowing us to efficiently maintain these counts.

This is a common **frequency counting** pattern that appears frequently in algorithm problems.

## ⏱️ Complexity

**Time:** `O(n)`

We iterate through the strings a constant number of times. Each dictionary lookup/update is `O(1)` on average.

**Space:** `O(k)`

where `k` is the number of distinct characters.

Because the problem specifies lowercase English letters, `k` is at most 26, so this can also be considered `O(1)` auxiliary space under the given constraints.

## 🔑 Key Takeaway

When a problem requires comparing **how frequently values occur**, a hash map can be used to store:

```text
value → frequency
```

The important pattern is:

> **Count occurrences → compare frequencies → determine whether they match.**

This problem also demonstrates another use of dictionaries:

- **Two Sum:** `value → index`
- **Valid Anagram:** `character → frequency`