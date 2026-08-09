"""
Problem:
    Symmetric Tree

Pattern:
    DFS + Recursion

Approach:
    Compare the left subtree with the right subtree in mirror order.
    The outer and inner nodes must have matching values.

Time Complexity:
    O(n)

Space Complexity:
    O(h)
"""


def is_symmetric(root):
    if root is None:
        return True

    def is_mirror(left, right):
        # Both nodes being empty means this part is symmetric.
        if left is None and right is None:
            return True

        # Only one node being empty means symmetry is broken.
        if left is None or right is None:
            return False

        # Values must match at mirrored positions.
        if left.val != right.val:
            return False

        # Compare outer nodes and inner nodes recursively.
        return (
            is_mirror(left.left, right.right)
            and is_mirror(left.right, right.left)
        )

    return is_mirror(root.left, root.right)