
# Problem 1: Square Root of an Integer

## Design

If the number is `0` or `1`, return it immediately since the square root is itself. Otherwise, set `low` to `0` and `high` to the number. Take the midpoint and check if its square equals the number — if so return it. If the square is **less than** the number, store `mid` as a candidate floor value and move `low` up. If the square is **greater**, move `high` down. Repeat until the search space is exhausted and return the last stored candidate.

## Big O Space Complexity

A fixed number of variables (`low`, `high`, `mid`, `result`) with no extra data structures: **O(1)**

## Big O Time Complexity

Halves the search space on every iteration: **O(log n)** with `n` being the input number.