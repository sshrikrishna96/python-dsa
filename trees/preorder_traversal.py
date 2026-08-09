"""
Problem:
    Binary Tree Preorder Traversal

Pattern:
    DFS + Recursion

Traversal:
    Root → Left → Right

Time Complexity:
    O(n)

Space Complexity:
    O(h)
"""


def preorder_traversal(root):
    result = []

    def dfs(node):
        if node is None:
            return

        # Process the root before visiting its children.
        result.append(node.val)

        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return result