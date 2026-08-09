"""
Problem:
    Invert Binary Tree

Pattern:
    DFS + Recursion

Approach:
    For every node, swap its left and right children.
    Recursively perform the same operation on both subtrees.

Time Complexity:
    O(n)

Space Complexity:
    O(h)
"""


def invert_tree(root):
    # Nothing needs to be inverted in an empty tree.
    if root is None:
        return None

    # Swap the left and right children of the current node.
    root.left, root.right = root.right, root.left

    # Continue the inversion for both subtrees.
    invert_tree(root.left)
    invert_tree(root.right)

    return root