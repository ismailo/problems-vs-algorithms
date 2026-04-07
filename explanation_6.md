# Problem 6: Unsorted Integer Array

## Design

If the list is empty return `None`. Set both `current_min` and `current_max` to the **first element** as a starting point. Walk through the rest of the list one element at a time:

- If the current element is **less than** `current_min`, update `current_min`
- If it is **greater than** `current_max`, update `current_max`

Return the two values as a tuple when done.

## Big O Space Complexity

Two variables to hold min and max, no copy of the list is made: **O(1)**

## Big O Time Complexity

Makes one pass through the list examining each element one time: **O(n)** with `n` being the number of elements in the list.