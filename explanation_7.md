# Problem 7: Request Routing in a Web Server with a Trie

## Reasoning

An HTTP router needs to map URL paths like `/home/about` to handler functions quickly and correctly. There are several possible approaches — regular expressions, hash maps, linear string matching — but a **Trie (prefix tree)** is particularly well-suited because:

- URL paths are naturally **hierarchical** and **prefix-structured**
- Many routes share common prefixes (e.g., `/api/users` and `/api/posts` both start with `/api`)
- Lookup time depends only on **path depth**, not the total number of routes stored

## Design Decisions

### Splitting on `/` instead of characters

Unlike a word autocomplete trie that splits on characters, we split paths on the `/` separator. Each trie node represents one **path segment** (e.g., `"home"`, `"about"`), not a single character. This keeps the trie shallow and avoids creating an enormous number of nodes for long paths.

```
/home/about  →  ["home", "about"]
root → "home" → "about" (handler assigned here)
```

### Handler only on leaf nodes

A handler is assigned **only to the final node** of an inserted path. Intermediate nodes (like the `"home"` node when only `/home/about` is registered) correctly have `None` as their handler, which naturally causes a `not found` response for unregistered intermediate paths.

### `split_path` as a shared utility

Both `add_handler` and `lookup` need to convert a raw path string into a list of segments. Centralizing this in `split_path` — which filters out empty strings from the `split("/")` result — ensures that **trailing slashes are handled consistently** in one place:

```python
[part for part in path.split("/") if part]
# "/home/about/"  →  ["home", "about"]
# "/home/about"   →  ["home", "about"]
```

### Root path edge case

The root path `"/"` splits into an empty list `[]`. Rather than inserting a special node, the root handler is assigned directly to `self.root` during `RouteTrie.__init__`. The `lookup` method checks for this case and returns the root node's handler directly.

The empty string `""` is treated as a separate edge case that returns `not_found_handler`, since an empty path is not a valid URL request.

## Complexity

Let $d$ = depth of the path (number of segments, e.g., `/home/about` has depth 2) and $R$ = total number of routes stored.

| Operation | Time | Space |
|---|---|---|
| **add_handler** | $O(d)$ — traverse/create $d$ nodes | — |
| **lookup** | $O(d)$ — traverse at most $d$ nodes | — |
| **Trie storage** | — | $O(R \cdot d)$ — proportional to total path segments across all routes |

A key advantage of the Trie over a hash map is that lookup cost is **independent of $R$** (the total number of routes). A hash map lookup is $O(1)$ average but requires hashing the full path string and handling collisions. The Trie trades that for a clean $O(d)$ worst-case guarantee with no collision risk.