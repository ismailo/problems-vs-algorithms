# Problem 3: Rearrange Array Digits

## Design

If the list is empty return `(0, 0)`. If it has one element return that element paired with `0`. Sort the list in **descending order** using merge sort since built-in sorting is not allowed. Walk through the sorted list and alternate each digit — even-indexed digits build the first number, odd-indexed digits build the second. This ensures the largest digits land in the highest place values and both numbers stay roughly the same length.

## Big O Space Complexity

Merge sort creates auxiliary arrays during the merge step proportional to the input: **O(n)**

## Big O Time Complexity

Dominated by merge sort which divides and merges repeatedly: **O(n log n)** with `n` being the number of elements in the list.