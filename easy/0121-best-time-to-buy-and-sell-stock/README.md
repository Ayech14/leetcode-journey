# 121. Best Time to Buy and Sell Stock

## 🟢 Difficulty

**Easy**

## 🧠 Pattern

**Array + Sliding Window (Two Pointers)**

## 📌 Problem

Given an array `prices` where `prices[i]` is the price of a stock on day `i`, choose one day to buy and a **later** day to sell so that the profit is as large as possible.

If no profit is possible, return `0`.

```text
prices = [7, 1, 5, 3, 6, 4]
```

Buying at `1` and selling at `6` gives a profit of `5`.

```text
prices = [7, 6, 4, 3, 1]
```

The price only falls, so the best choice is not to trade: the answer is `0`.

## 💡 Approach

Think of a **window** with two pointers:

- `buy` is the left edge: the day we would buy.
- `sell` is the right edge: the day we would sell.

We start with `buy = 0` and `best = 0`, then move `sell` from day `1` to the end:

1. If `prices[sell] < prices[buy]`, today is a **cheaper day to buy**. Nothing can be gained by selling today, so move the left edge: `buy = sell`.
2. Otherwise, compute the profit `prices[sell] - prices[buy]` and keep it if it beats `best`.

```python
if prices[sell] < prices[buy]:
    buy = sell
else:
    best = max(best, prices[sell] - prices[buy])
```

Because `buy` always points at the cheapest price seen so far, every `sell` day is compared with the best possible buy day before it. At the end, `best` holds the maximum profit (or `0` if it never improved).

## ⏱️ Complexity

**Time:** `O(n)`

The `sell` pointer walks through the array exactly once.

**Space:** `O(1)`

We only store two indices and the best profit, no matter how large the input is.

## 🔑 Key Takeaway

A brute-force solution tries every buy/sell pair in `O(n²)`. The window lets us skip that: whenever we find a lower price, the old buy day can never be better again, so we **drop it and restart the window there**.

This is the first Sliding Window problem: two pointers define the window, the right one explores, and the left one jumps forward when a better start appears. It also echoes Two Sum, where we remember what we have seen so far to avoid re-checking everything.

> **Track the best starting point so far → test every later day against it → move the start when a better one appears.**
