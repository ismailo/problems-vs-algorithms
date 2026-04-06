
# Problem 1: Square Root of an Integer

## Reasoning

The naive approach would be to iterate from 0 up to `number` and find the largest integer whose square is ≤ `number`. This works but runs in $O(n)$ time, which is too slow for large inputs.

Instead, I recognized that the sequence of integers $[0, 1, 2, \dots, n]$ is **sorted**, which makes it a perfect candidate for **binary search**. The idea is to search for the largest integer `mid` such that $mid^2 \leq number$.

At every step we cut the search space in half:

- If $mid^2 = number$ → exact square root found, return `mid`
- If $mid^2 < number$ → `mid` is a valid floor candidate; record it and search the right half
- If $mid^2 > number$ → search the left half

The key insight is storing the last valid candidate in `result` before moving `low` upward. When the loop ends, `result` holds the **floor** of the square root.

```python
low, high = 0, number
result = 0

while low <= high:
    mid = (low + high) // 2
    if mid * mid == number:
        return mid
    elif mid * mid < number:
        result = mid      # best floor candidate so far
        low = mid + 1
    else:
        high = mid - 1

return result
```

## Why Binary Search?

The problem requires $O(\log n)$ time. Binary search is the canonical $O(\log n)$ technique for searching over a monotonically ordered domain — and the integers from 0 to `number` are exactly that.

## Complexity

| | Complexity |
|---|---|
| **Time** | $O(\log n)$ — search space halves each iteration |
| **Space** | $O(1)$ — only a fixed number of variables used |