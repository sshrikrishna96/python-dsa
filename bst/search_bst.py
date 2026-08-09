"""
Problem:
    Search in a Binary Search Tree

Pattern:
    BST

Approach:
    Use the BST property to eliminate half of the search space
    at every step in a balanced tree.

Time Complexity:
    O(h)

Space Complexity:
    O(1)
"""


def search_bst(root, val):
    current = root

    while current:
        # The target has been found.
        if current.val == val:
            return current

        # Smaller values can only exist in the left subtree.
        if val < current.val:
            current = current.left

        # Larger values can only exist in the right subtree.
        else:
            current = current.right

    # The target does not exist in the tree.
    return None