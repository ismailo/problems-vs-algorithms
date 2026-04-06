# Problem 4: Dutch National Flag Problem

## Reasoning

The problem asks us to sort an array containing only `0`, `1`, and `2` in a **single traversal** without using Python's built-in sort. Because there are only three distinct values, we do not need a general-purpose sorting algorithm.

The ideal approach is the **Dutch National Flag algorithm**, invented by Edsger Dijkstra. The idea is to partition the array into three regions using three pointers:

| Pointer | Role |
|---|---|
| `low` | Right boundary of the `0` region |
| `mid` | Current element being examined |
| `high` | Left boundary of the `2` region |

At every step we inspect `input_list[mid]` and take one of three actions:

- **0** → swap with `input_list[low]`, advance both `low` and `mid`
- **1** → already in the correct middle region, advance `mid` only
- **2** → swap with `input_list[high]`, shrink `high` but **do not advance `mid`** (the swapped element is unknown and must be re-examined)

```
[  0s  |  1s  |  ???  |  2s  ]
        ^low   ^mid    ^high
```

The loop terminates when `mid > high`, at which point every element has been placed in its correct region — in a single pass.

## Why Not Count-and-Overwrite?

An alternative is to count occurrences of each value and overwrite the array. This is also $O(n)$ but requires **two traversals**: one to count, one to write. The Dutch National Flag algorithm achieves the same result in a **single traversal**, which is a stricter requirement here.

## Why Not a General Sort?

General comparison sorts like merge sort or quicksort are $O(n \log n)$. Since we know the domain is exactly `{0, 1, 2}`, we can exploit that structure for a linear-time solution.

## Complexity

| | Complexity |
|---|---|
| **Time** | $O(n)$ — each element is visited at most twice (once by `mid`, once by a swap) |
| **Space** | $O(1)$ — sorting is done in-place with only three pointer variables |