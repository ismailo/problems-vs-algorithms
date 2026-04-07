# Problem 4: Dutch National Flag Problem

## Design

If the list is empty return it as-is. Set three pointers: `low` at the start, `mid` at the start, and `high` at the end. Walk `mid` through the list:

- If the current element is `0`, swap it with the element at `low` and advance both `low` and `mid`
- If it is `1`, advance `mid` only since it is already in the right region
- If it is `2`, swap it with the element at `high` and shrink `high` — do **not** advance `mid` since the swapped element still needs to be checked

Stop when `mid` passes `high`.

## Big O Space Complexity

Sorting is done in-place with only three pointer variables: **O(1)**

## Big O Time Complexity

Makes one pass through the list with each element visited at most twice: **O(n)** with `n` being the number of elements in the list.