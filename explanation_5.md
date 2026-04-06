# Problem 5: Autocomplete with Tries

## Reasoning

The autocomplete problem requires two operations:
1. Given a prefix, quickly find if it exists in our word collection
2. From that prefix node, collect all words that complete it (suffixes)

A **Trie (prefix tree)** is the ideal data structure for this because it organizes words by their shared prefixes. Every path from root to a marked node spells out a word, and all words sharing a prefix share the same path up to that prefix node — making prefix lookup extremely efficient.

## Data Structure Design

Each `TrieNode` holds:
- `children` — a dictionary mapping a character to its child `TrieNode`. A dictionary gives $O(1)$ average-case lookup per character, which is more space-efficient than a fixed-size array when the alphabet is large or sparse.
- `is_end_of_word` — a boolean flag marking whether this node completes a valid word.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
```

## Insert

We walk character by character, creating new nodes as needed, and set `is_end_of_word = True` on the final node. This costs $O(m)$ where $m$ is the length of the word being inserted.

## Find (Prefix Lookup)

We walk the trie following each character of the prefix. If any character is missing, the prefix doesn't exist and we return `None`. Otherwise we return the node at the end of the prefix. This is also $O(m)$.

## Suffixes (Autocomplete)

Starting from the prefix node, we recurse depth-first through all descendants. Whenever we reach a node with `is_end_of_word = True`, we record the accumulated suffix. This is a clean recursive approach:

```python
def suffixes(self, suffix=''):
    results = []
    if self.is_end_of_word and suffix != '':
        results.append(suffix)
    for char, child_node in self.children.items():
        results.extend(child_node.suffixes(suffix + char))
    return results
```

The guard `suffix != ''` prevents the prefix itself (the empty string at the starting node) from being returned as a suffix when it is a complete word.

## Complexity

Let $n$ = total number of characters across all inserted words, $m$ = prefix length, $s$ = number of matching suffixes, $k$ = average suffix length.

| Operation | Time | Space |
|---|---|---|
| **Insert** | $O(m)$ per word | $O(n)$ total for the trie |
| **Find** | $O(m)$ | $O(1)$ |
| **Suffixes** | $O(s \cdot k)$ — visits every node below the prefix | $O(s \cdot k)$ for the result list |