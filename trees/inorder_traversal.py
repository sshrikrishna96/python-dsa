"""
Problem:
    Binary Tree Inorder Traversal

Pattern:
    DFS + Recursion

Traversal:
    Left → Root → Right

Time Complexity:
    O(n)

Space Complexity:
    O(h), where h is the height of the tree.
"""


def inorder_traversal(root):
    result = []

    def dfs(node):
        # Stop when there is no node to process.
        if node is None:
            return

        # Visit the left subtree first.
        dfs(node.left)

        # Process the current node after its left subtree.
        result.append(node.val)

        # Finally, visit the right subtree.
        dfs(node.right)

    dfs(root)

    return result