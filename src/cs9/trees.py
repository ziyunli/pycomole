from dataclasses import dataclass
from typing import Optional


@dataclass(eq=True, frozen=True)
class Node:
    """A node in a rooted binary tree with a pointer to its parent"""

    parent: Optional["Node"]
    value: str


def has_common_non_root_ancestor(
    root: Optional[Node], a: Optional[Node], b: Optional[Node]
) -> bool:
    """
    Determines whether the two nodes have a common ancestor besides \
        the root.

    Examples:
    ```
           root
          /    \\
         a       b
       /   \\    /  \\
      c     d  e    f
    ```

    Args:
        root: The root of a binary tree
        a: node 1 in the same binary tree
        b: node 2 in the same binary tree

    Returns:
        A boolean indicating if the two nodes have a common ancestor \
            besides the root

    Notes:
        - Clarify if a node counts as its own ancestor, e.g. \
            has_common_non_root_ancestor(root, a, c). \
                Here we assume (a, c) share an ancestor a.
        - Using hash is easier but takes a bit extra memory space.
    """
    if not (root and a and b):
        return False

    ancestors = set()
    while a is not None and a != root:
        ancestors.add(a)
        a = a.parent

    while b is not None and b != root:
        if b in ancestors:
            return True
        b = b.parent

    return False
