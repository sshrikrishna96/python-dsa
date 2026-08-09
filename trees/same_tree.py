"""
Problem:
    Same Tree

Pattern:
    DFS + Recursion

Approach:
    Compare two trees node by node.
    Two trees are identical if their corresponding nodes have
    the same values and their left and right subtrees are also identical.

Time Complexity:
    O(n)

Space Complexity:
    O(h)
"""


def is_same_tree(p, q):
    # If both nodes are empty, they are identical at this position.
    if p is None and q is None:
        return True

    # If only one node is empty, the tree structures are different.
    if p is None or q is None:
        return False

    # Current values must match before comparing child subtrees.
    if p.val != q.val:
        return False

    # Both left and right subtrees must be identical.
    return (
        is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )