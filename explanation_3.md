# Problem 3: Rearrange Array Digits

## Reasoning

The goal is to form two numbers from the digits of the input list such that their **sum is maximized**. The core insight is:

> To maximize the sum of two numbers, place the **largest digits in the highest place values** and distribute them **evenly** between the two numbers.

For example, given `[1, 2, 3, 4, 5]`, sorting descending gives `[5, 4, 3, 2, 1]`. Alternating digits:

- Number 1 gets digits at even indices: 5, 3, 1 → **531**
- Number 2 gets digits at odd indices: 4, 2 → **42**

Sum = 573, which is the maximum achievable.

## Why Merge Sort?

The problem explicitly prohibits using Python's built-in sorting functions, and requires $O(n \log n)$ time. **Merge sort** is the natural fit: it is a comparison-based, divide-and-conquer sort with a guaranteed $O(n \log n)$ time complexity in all cases. I implemented it to sort in **descending order** so the largest digits are picked first.

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:   # descending order
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    ...
```

## Why Alternating Assignment?

Alternating ensures the digit counts between the two numbers **differ by at most 1**, satisfying the constraint. It also guarantees that both numbers receive the highest-value digits in their most significant positions.

## Complexity

| | Complexity |
|---|---|
| **Time** | $O(n \log n)$ — dominated by merge sort |
| **Space** | $O(n)$ — merge sort requires auxiliary space proportional to input size |