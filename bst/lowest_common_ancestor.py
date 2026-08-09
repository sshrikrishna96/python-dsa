"""
Problem:
    Lowest Common Ancestor of a Binary Search Tree

Pattern:
    BST Property

Approach:
    If both target nodes are smaller than the current node,
    move left. If both are larger, move right.
    Otherwise, the current node is their lowest common ancestor.

Time Complexity:
    O(h)

Space Complexity:
    O(1)
"""


def lowest_common_ancestor(root, p, q):
    current = root

    while current:

        # Both nodes are smaller, so the ancestor must be on the left.
        if p.val < current.val and q.val < current.val:
            current = current.left

        # Both nodes are larger, so the ancestor must be on the right.
        elif p.val > current.val and q.val > current.val:
            current = current.right

        else:
            # The paths split here, making this the lowest common ancestor.
            return current

    return None