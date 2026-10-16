# 49. Group Anagrams

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Hash Map + Frequency Counting (grouping by a canonical key)**

## 📌 Problem

Given a list of strings, group together the strings that are anagrams of each other. The groups can be returned in any order.

For example:

```text
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

produces:

```text
[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

because `"eat"`, `"tea"` and `"ate"` use the same letters, `"tan"` and `"nat"` use the same letters, and `"bat"` is on its own.

## 💡 Approach

Two words are anagrams exactly when they have the **same letter frequencies**. So if we turn each word into its frequency "fingerprint", all anagrams share the same fingerprint.

For each word:

1. Create a list of 26 zeros, one slot per letter (`a` → index `0`, `b` → index `1`, ...).
2. Walk through the word and add `1` to the slot of each character:

```python
count[ord(char) - ord("a")] += 1
```

3. Convert the list to a `tuple`, because lists cannot be dictionary keys but tuples can.
4. Use that tuple as the key in a dictionary `groups`, and append the word to the list stored under that key (creating the list the first time the key appears).

For example, `"eat"`, `"tea"` and `"ate"` all produce the same counts:

```text
a → 1, e → 1, t → 1  (everything else 0)
```

so they end up in the same group.

At the end, the dictionary values are exactly the groups, so we return `list(groups.values())`.

## 🔎 Why Use a Hash Map?

We need to **collect items that share a property**, and a dictionary does that naturally:

```text
fingerprint → list of words
```

Looking up or inserting a key is `O(1)` on average, so we never have to compare words against each other.

Sorting each word (`"eat"` → `"aet"`) is another valid fingerprint, but it costs `O(k log k)` per word. Counting letters costs only `O(k)`, which is why this solution uses counts.

## ⏱️ Complexity

**Time:** `O(n * k)`

where `n` is the number of strings and `k` is the maximum string length. Each word is scanned once to build its counts, and building and hashing a 26-length tuple is constant work.

**Space:** `O(n * k)`

The dictionary stores every word (up to `n * k` characters in total) plus one 26-length key per group.

## 🔑 Key Takeaway

When items must be grouped by "being the same in some way", find a **canonical form** that is identical for every item in a group, and use it as a dictionary key:

```text
canonical form → list of items
```

This builds on earlier problems in this repo:

- **Two Sum:** `value → index`
- **Valid Anagram:** `character → frequency`
- **Group Anagrams:** `frequency fingerprint → group of words`

> **Reduce each item to a fingerprint → use it as the key → collect everything that shares it.**
