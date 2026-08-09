"""
Problem:
    Binary Tree Postorder Traversal

Pattern:
    DFS + Recursion

Traversal:
    Left → Right → Root

Time Complexity:
    O(n)

Space Complexity:
    O(h)
"""


def postorder_traversal(root):
    result = []

    def dfs(node):
        if node is None:
            return

        # Visit both children before processing the current node.
        dfs(node.left)
        dfs(node.right)

        result.append(node.val)

    dfs(root)

    return result