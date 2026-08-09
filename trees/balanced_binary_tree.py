"""
Problem:
    Balanced Binary Tree

Pattern:
    DFS + Recursion

Approach:
    Calculate the height of each subtree.
    If the height difference between the left and right subtree
    is greater than one, the tree is unbalanced.

Time Complexity:
    O(n)

Space Complexity:
    O(h)
"""


def is_balanced(root):

    def height(node):
        # An empty subtree has height zero.
        if node is None:
            return 0

        left_height = height(node.left)

        # A negative value indicates that the left subtree is unbalanced.
        if left_height == -1:
            return -1

        right_height = height(node.right)

        # A negative value indicates that the right subtree is unbalanced.
        if right_height == -1:
            return -1

        # The height difference must not exceed one.
        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    # A negative result means at least one subtree is unbalanced.
    return height(root) != -1