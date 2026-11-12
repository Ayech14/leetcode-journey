# 853. Car Fleet

## 🟡 Difficulty

**Medium**

## 🧠 Pattern

**Sorting + Monotonic Stack**

## 📌 Problem

There are `n` cars driving toward the same `target` mile. Each car has a starting position and a speed.

A car can never pass the car in front of it. If it catches up, it slows down and drives together with that car as one **fleet**.

Return the number of fleets that arrive at the target.

```text
target = 12
position = [10, 8, 0, 5, 3]
speed    = [ 2, 4, 1, 1, 3]
```

The cars at `10` and `8` meet at the target, the cars at `5` and `3` merge on the way, and the car at `0` is alone, so the answer is `3`.

## 💡 Approach

The key idea is to look at **how long each car needs to reach the target** if nothing were in front of it:

```text
time = (target - position) / speed
```

1. Pair each position with its speed and sort the cars by position, starting with the car **closest to the target**.
2. Go through the cars in that order and compute each car's arrival time.
3. Keep a stack of arrival times, one entry per fleet.
4. If the current car's time is **less than or equal to** the time on top of the stack, it catches up to the fleet ahead (it can't pass), so it joins that fleet and we add nothing.
5. Otherwise it is slower than the fleet ahead and never catches it, so it starts a new fleet: push its time.
6. The answer is the size of the stack.

Because a car that catches up takes on the speed of the fleet ahead, the fleet's arrival time is the time already on the stack, so merged cars never need to be pushed.

## 🔎 Why Use a Stack?

Each fleet is represented by the arrival time of its **leading car**. Every new car is only compared with the most recent fleet, which is the top of the stack.

The pushed times are strictly increasing from bottom to top, which is a **monotonic stack**.

## ⏱️ Complexity

**Time:** `O(n log n)`

Sorting the cars dominates. The loop that follows visits each car once with `O(1)` work.

**Space:** `O(n)`

We store the sorted pairs, and in the worst case the stack holds one time per car.

## 🔑 Key Takeaway

When objects move in one direction and cannot pass each other, process them **from the front** and compare each one only with the group directly ahead. Converting each car to a single number (its arrival time) makes the comparison trivial.

This is a close cousin of **Daily Temperatures**: both keep a monotonic stack and compare each new value with the top of it.

> **Sort by position → compute arrival times → a slower car starts a new fleet, a faster one merges into the fleet ahead.**
