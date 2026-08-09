"""
Problem:
    Binary Tree Level Order Traversal

Pattern:
    BFS + Queue

Approach:
    Process nodes level by level using a queue.

Time Complexity:
    O(n)

Space Complexity:
    O(n)
"""

from collections import deque


def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:

        # Process all nodes currently present at this level.
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()

            current_level.append(node.val)

            # Add children so they can be processed at the next level.
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result