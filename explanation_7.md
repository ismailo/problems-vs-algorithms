# Problem 7: Request Routing in a Web Server with a Trie

## Design

Create a `RouteTrie` with a root node that holds the root handler. Each node stores a dictionary of children keyed by **path segment** and a handler value. Three operations drive the router:

- **`split_path`** — splits the path on `"/"` and filters out empty strings, handling leading and trailing slashes in one place
- **`add_handler`** — walks the trie using the split path, creating nodes as needed, and assigns the handler only to the **last node**
- **`lookup`** — walks the trie the same way and returns the handler if found, the not-found handler if any segment is missing, or the root handler if the path resolves to `"/"`

An empty string `""` returns the not-found handler since it is not a valid path.

## Big O Space Complexity

The trie stores one node per unique path segment across all routes: **O(R * d)** with `R` being the number of routes and `d` being the average number of segments per route.

## Big O Time Complexity

Both insert and lookup walk one node per segment in the path: **O(d)** with `d` being the number of segments in the path being added or looked up.