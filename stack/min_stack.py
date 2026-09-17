"""
Problem:
    Min Stack

Pattern:
    Stack + Auxiliary Stack

Approach:
    Use two stacks:

    1. stack:
       Stores all the elements normally.

    2. min_stack:
       Stores the minimum value seen so far.

    When pushing a value, add it to the normal stack.
    If min_stack is empty or the new value is smaller than or
    equal to the current minimum, also add it to min_stack.

    When popping, remove the value from stack.
    If the popped value is also the current minimum, remove it
    from min_stack.

    This allows getMin() to return the minimum element in O(1) time.

Time Complexity:
    O(1) for push, pop, top, and getMin

Space Complexity:
    O(n)
"""


class MinStack:

    def __init__(self):
        # Stores all elements of the stack.
        self.stack = []

        # Stores the minimum elements.
        self.min_stack = []

    def push(self, value: int) -> None:
        # Add the value to the main stack.
        self.stack.append(value)

        # If min_stack is empty or the new value is
        # smaller than or equal to the current minimum,
        # add it to min_stack.
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        # Remove the top element from the main stack.
        popped_value = self.stack.pop()

        # If the removed value was the current minimum,
        # remove it from min_stack as well.
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element without removing it.
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the current minimum element.
        return self.min_stack[-1]