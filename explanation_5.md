# Problem 5: Autocomplete with Tries


## Design

Each `TrieNode` holds a dictionary of children keyed by character and a flag marking whether it ends a word. Three operations are supported:

- **Insert** — walk character by character creating nodes as needed and set the end flag on the last node
- **Find** — walk the same way and return the node at the end of the prefix, or `None` if any character is missing
- **Suffixes** — recurse depth-first from the prefix node, accumulating characters as you go and recording the result whenever a word-ending node is reached

## Big O Space Complexity

The trie stores every character of every inserted word as its own node: **O(n)** with `n` being the total number of characters across all words.

## Big O Time Complexity

Insert and find each walk one node per character in the word or prefix: **O(m)** with `m` being the length of the word or prefix. Collecting suffixes visits every node below the prefix node: **O(s * k)** with `s` being the number of matching words and `k` being their average length.