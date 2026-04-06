# Problem 6: Unsorted Integer Array

## Reasoning

Finding the minimum and maximum of an unsorted list fundamentally requires examining every element at least once — you cannot skip any element without risking missing the true min or max. This means $O(n)$ is both the required and the theoretical lower bound for this problem.

The straightforward approach is a **single traversal** that maintains two running variables:

- `current_min` — the smallest value seen so far
- `current_max` — the largest value seen so far

Both are initialized to `ints[0]` (the first element), then updated as we scan the rest of the list. This satisfies the bonus challenge of finding both values in a single pass.

```python
current_min = ints[0]
current_max = ints[0]

for num in ints[1:]:
    if num < current_min:
        current_min = num
    if num > current_max:
        current_max = num
```

## Why Not Sort First?

Sorting would place the minimum at index 0 and the maximum at index -1, but any comparison-based sort costs at least $O(n \log n)$. Since we only need two values and not a fully ordered list, sorting is wasteful. The single-pass approach gives us what we need at $O(n)$.

## Why Not Python's `min()` / `max()`?

The problem explicitly prohibits built-in functions. Even if they were allowed, calling `min()` and `max()` separately would result in **two traversals** of the list. The single-pass approach is strictly more efficient in practice (half the iterations), even though both approaches are formally $O(n)$.

## Edge Case

An empty list has no meaningful min or max, so the function returns `None` — which is the correct and Pythonic way to signal "no result" without raising an exception.

## Complexity

| | Complexity |
|---|---|
| **Time** | $O(n)$ — exactly one pass through the list |
| **Space** | $O(1)$ — only two tracking variables regardless of input size |