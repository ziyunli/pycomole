from cs9.trees import Node, has_common_non_root_ancestor


def test_has_common_non_root_ancestor() -> None:
    # Build a tree
    #       root
    #      /    \
    #     a       b
    #   /   \    /  \
    #  c     d  e    f
    root = Node(parent=None, value="root")
    a = Node(parent=root, value="a")
    b = Node(parent=root, value="b")
    c = Node(parent=a, value="c")
    d = Node(parent=a, value="d")
    e = Node(parent=b, value="e")
    f = Node(parent=b, value="f")

    assert has_common_non_root_ancestor(root, c, d)
    assert has_common_non_root_ancestor(root, e, f)
    assert has_common_non_root_ancestor(root, a, c)
    assert has_common_non_root_ancestor(root, f, b)
    assert not has_common_non_root_ancestor(None, a, b)
    assert not has_common_non_root_ancestor(root, None, b)
    assert not has_common_non_root_ancestor(root, a, None)
    assert not has_common_non_root_ancestor(root, a, b)
