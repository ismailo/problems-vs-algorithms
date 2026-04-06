# Problem 2: Search in a Rotated Sorted Array

## Reasoning

A straightforward linear scan would find the target in $O(n)$, but the problem requires $O(\log n)$. This rules out scanning and points directly to **binary search**.

The challenge is that the array has been rotated, so a standard binary search — which assumes the entire array is sorted — would fail. The key observation is:

> Even after a rotation, **at least one half of the array is always fully sorted**.

This is the invariant that makes the algorithm work. At each step, after computing `mid`, we check which half is sorted:

- If `input_list[low] <= input_list[mid]`, the **left half** is sorted
- Otherwise, the **right half** is sorted

Once we know which half is sorted, we can determine in $O(1)$ whether the target falls inside that sorted half (a simple range check), and eliminate the other half entirely.

```python
if input_list[low] <= input_list[mid]:      # left half is sorted
    if input_list[low] <= number < input_list[mid]:
        high = mid - 1                       # target is in the left half
    else:
        low = mid + 1                        # target must be in the right half
else:                                        # right half is sorted
    if input_list[mid] < number <= input_list[high]:
        low = mid + 1                        # target is in the right half
    else:
        high = mid - 1                       # target must be in the left half
```

This preserves the $O(\log n)$ property of binary search despite the rotation.

## Why Not a Modified Linear Search?

A linear scan would always work but at $O(n)$ cost. The structure of a rotated sorted array guarantees the "one sorted half" property at every level of the binary search, so we never need to abandon the logarithmic approach.

## Complexity

| | Complexity |
|---|---|
| **Time** | $O(\log n)$ — search space halves at every step |
| **Space** | $O(1)$ — no additional data structures needed |