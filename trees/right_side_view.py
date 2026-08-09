"""
Problem:
    Binary Tree Right Side View

Pattern:
    BFS + Queue

Approach:
    Perform level-order traversal.
    The last node processed at each level is visible from the right side.

Time Complexity:
    O(n)

Space Complexity:
    O(n)
"""

from collections import deque


def right_side_view(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # The last node of each level is visible from the right side.
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result