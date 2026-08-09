"""
Problem:
    Validate Binary Search Tree

Pattern:
    DFS + Recursion + Range Checking

Approach:
    Every node must fall within a valid range determined by
    its ancestors.

Time Complexity:
    O(n)

Space Complexity:
    O(h)
"""


def is_valid_bst(root):
    def validate(node, low, high):
        # An empty subtree is valid.
        if node is None:
            return True

        # The current value must remain inside the allowed range.
        if not (low < node.val < high):
            return False

        # Left values must be smaller and right values must be larger.
        return (
            validate(node.left, low, node.val)
            and validate(node.right, node.val, high)
        )

    return validate(root, float("-inf"), float("inf"))