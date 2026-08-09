"""
Problem:
    Maximum Depth of Binary Tree

Pattern:
    DFS + Recursion

Approach:
    Recursively calculate the depth of the left and right
    subtrees. The depth of the current node is one more
    than the deeper of its two subtrees.

Time Complexity:
    O(n)

Space Complexity:
    O(h), where h is the height of the tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    # An empty tree has depth 0.
    if root is None:
        return 0

    # Recursively calculate the depth of both subtrees.
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # The current node contributes one level.
    return 1 + max(left_depth, right_depth)