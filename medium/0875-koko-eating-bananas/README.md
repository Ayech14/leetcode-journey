# 875. Koko Eating Bananas

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Binary Search on the Answer**

## 📌 Problem

Koko has several piles of bananas and `h` hours before the guards return. Each hour she picks one pile and eats up to `k` bananas from it. If the pile has fewer than `k` bananas, she finishes it and wastes the rest of that hour.

Find the **minimum speed `k`** that lets her eat every banana within `h` hours.

```text
piles = [3, 6, 7, 11], h = 8
```

At `k = 4` the piles take `1 + 2 + 2 + 3 = 8` hours, so `4` works. At `k = 3` they take `1 + 2 + 3 + 4 = 10` hours, which is too slow.

## 💡 Approach

We are not searching through the array. We are searching through the **possible speeds**.

- The slowest sensible speed is `1`.
- The fastest speed we would ever need is `max(piles)`, because eating the biggest pile in one hour means every pile takes exactly one hour.

The speeds are ordered, and the check "can Koko finish in `h` hours at speed `k`?" is **monotonic**: if a speed works, every faster speed works too. So we can binary search for the first speed that works.

1. Set `left = 1` and `right = max(piles)`.
2. While `left < right`, take `mid = (left + right) // 2`.
3. Count the hours needed at speed `mid`. Each pile takes a ceiling division:

```python
hours = sum((pile + mid - 1) // mid for pile in piles)
```

4. If `hours <= h`, `mid` is fast enough, but a slower speed might work too, so keep it as a candidate: `right = mid`.
5. Otherwise `mid` is too slow, so the answer must be larger: `left = mid + 1`.
6. When `left == right`, that is the minimum valid speed.

## 🔎 Why Binary Search on the Answer?

Trying every speed from `1` to `max(piles)` could mean up to `10^9` checks, which is far too slow.

Because the feasibility check flips from "too slow" to "fast enough" exactly once, we can halve the search range each step:

```text
speed:   1  2  3  4  5  6 ...
result:  ✗  ✗  ✗  ✓  ✓  ✓ ...
```

We are looking for the **first ✓**.

## ⏱️ Complexity

**Time:** `O(n * log m)`

where `n` is the number of piles and `m` is `max(piles)`. The binary search takes `O(log m)` steps, and each step sums the hours over all `n` piles.

**Space:** `O(1)`

We only keep a few integer variables.

## 🔑 Key Takeaway

Sometimes the thing to binary search is not an index in the input, but the **answer itself**. If you can write a quick check like "does this value work?" and the check is monotonic, you can binary search the range of possible answers.

This builds on **Binary Search** and **Search a 2D Matrix**: the same `left` / `right` / `mid` loop, but here the search space is a range of speeds instead of an array.

> **Define the range of answers → check the middle → discard the half that cannot contain the minimum.**
