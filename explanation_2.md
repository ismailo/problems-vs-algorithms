# Problem 2: Search in a Rotated Sorted Array

## Design

If the list is empty return `-1`. Set `low` and `high` to the start and end of the list. Take the midpoint and check if it matches the target — if so return the index. Then determine which half of the array is **fully sorted** by comparing the leftmost value to `mid`. If the left half is sorted and the target falls within its range, move `high` down into it; otherwise move `low` up into the right half. Apply the same logic in reverse if the right half is sorted instead. Repeat until found or the search space is empty.

## Big O Space Complexity

Only pointer variables are used, no extra data structures: **O(1)**

## Big O Time Complexity

Halves the search space on every iteration: **O(log n)** with `n` being the number of elements in the list.