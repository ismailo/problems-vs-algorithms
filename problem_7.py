"""
Problem 7: Request Routing in a Web Server with a Trie

This module implements an HTTPRouter using a Trie data structure.

The HTTPRouter takes a URL path like "/", "/about", or 
"/blog/2019-01-15/my-awesome-blog-post" and determines the appropriate handler 
to return. The Trie is used to efficiently store and retrieve handlers based on 
the parts of the path separated by slashes ("/").

The RouteTrie stores handlers under path parts, and the Router delegates adding 
and looking up handlers to the RouteTrie. The Router also includes a not found 
handler for paths that are not found in the Trie and handles trailing slashes 
to ensure requests for '/about' and '/about/' are treated the same.

You sould implement the function bodies the function signatures. Use the test 
cases provided below to verify that your algorithm is correct. If necessary, 
add additional test cases to verify that your algorithm works correctly.
"""

from typing import Optional

class RouteTrieNode:
    """
    A node in the RouteTrie, representing a part of a route.

    Attributes:
    children (dict): A dictionary mapping part of the route to the corresponding RouteTrieNode.
    handler (Optional[str]): The handler associated with this node, if any.
    """
    def __init__(self):
        """
        Initialize a RouteTrieNode with an empty dictionary for children and no handler.
        """
        self.children = {}
        self.handler = None

class RouteTrie:
    """
    A trie (prefix tree) for storing routes and their handlers.

    Attributes:
    root (RouteTrieNode): The root node of the trie.
    """
    def __init__(self, root_handler: str):
        """
        Initialize the RouteTrie with a root handler.

        Args:
        root_handler (str): The handler for the root node.
        """
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts: list[str], handler: str) -> None:
        """
        Insert a route and its handler into the trie.

        Args:
        path_parts (list[str]): A list of parts of the route.
        handler (str): The handler for the route.
        """
        node = self.root
        for part in path_parts:
            if part not in node.children:
                node.children[part] = RouteTrieNode()
            node = node.children[part]
        # Assign the handler only to the leaf (deepest) node of this path
        node.handler = handler

    def find(self, path_parts: list[str]) ->  Optional[str]:
        """
        Find the handler for a given route.

        Args:
        path_parts (list[str]): A list of parts of the route.

        Returns:
        str or None: The handler for the route if found, otherwise None.
        """
        node = self.root
        for part in path_parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler

class Router:
    """
    A router to manage routes and their handlers using a RouteTrie.

    Attributes:
    route_trie (RouteTrie): The trie used to store routes and handlers.
    not_found_handler (str): The handler to return when a route is not found.
    """
    def __init__(self, root_handler: str, not_found_handler: str):
        """
        Initialize the Router with a root handler and a not-found handler.

        Args:
        root_handler (str): The handler for the root route.
        not_found_handler (str): The handler for routes that are not found.
        """
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path: str, handler: str) -> None:
        """
        Add a handler for a route.

        Args:
        path (str): The route path.
        handler (str): The handler for the route.
        """
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path: str) -> str:
        """
        Look up a route and return the associated handler.

        Args:
        path (str): The route path.

        Returns:
        str: The handler for the route if found, otherwise the not-found handler.
        """
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_parts = self.split_path(path)

        # Empty path (e.g. "") — not the root, return not found
        if path == "":
            return self.not_found_handler

        # Root path "/" maps to the root handler directly
        if len(path_parts) == 0:
            return self.route_trie.root.handler

        handler = self.route_trie.find(path_parts)
        return handler if handler is not None else self.not_found_handler

    def split_path(self, path: str) -> list[str]:
        """
        Split the path into parts and remove empty parts to handle trailing slashes.

        Args:
            path (str): The path to split.

        Returns:
            List[str]: A list of parts of the path.
        """
        # Filter out empty strings that result from leading/trailing slashes
        return [part for part in path.split("/") if part]

if __name__ == '__main__':
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    # Edge case: Empty path
    print(router.lookup(""))
    # Expected output: 'not found handler'

    # Normal case: Path not found
    print(router.lookup("/home/contact"))
    # Expected output: 'not found handler'

    # Normal case: Path with multiple segments
    print(router.lookup("/home/about/me"))
    # Expected output: 'not found handler'

    # Normal case: Path with exact match
    print(router.lookup("/home/about"))
    # Expected output: 'about handler'

    # Bonus: Trailing slash handled
    print(router.lookup("/home/about/"))
    # Expected output: 'about handler'

    # Root path
    print(router.lookup("/"))
    # Expected output: 'root handler'