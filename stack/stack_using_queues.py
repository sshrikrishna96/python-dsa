"""
Problem:
    Implement Stack Using Queue

Pattern:
    Stack + Queue

Approach:
    A Stack follows LIFO (Last In, First Out),
    while a Queue normally follows FIFO (First In, First Out).

    To make the Queue behave like a Stack, whenever a new
    element is pushed, move all the previous elements behind it.

    Example:

    Before push(3):
        [1, 2]

    After adding 3:
        [1, 2, 3]

    Rotate the previous elements:
        [2, 3, 1]
        [3, 1, 2]

    Final:
        [3, 1, 2]

    Now the newest element is at the front,
    so pop() can simply remove the front element.

Time Complexity:
    push() → O(n)
    pop()  → O(1)
    top()  → O(1)
    empty() → O(1)

Space Complexity:
    O(n)
"""


from collections import deque


class MyStack:

    def __init__(self):
        # Queue used to implement the Stack.
        self.q = deque()

    def push(self, x: int) -> None:
        # Add the new element to the back of the queue.
        self.q.append(x)

        # Move all previous elements behind the new element.
        # This makes the newest element come to the front.
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # The newest element is now at the front,
        # so removing the front behaves like Stack pop().
        return self.q.popleft()

    def top(self) -> int:
        # The newest element is at the front,
        # so it represents the top of the Stack.
        return self.q[0]

    def empty(self) -> bool:
        # Return True if the queue contains no elements.
        return len(self.q) == 0