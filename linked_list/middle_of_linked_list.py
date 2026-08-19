"""
Problem:
    Middle of the Linked List

Pattern:
    Linked List + Fast & Slow Pointers

Approach:
    Use two pointers: slow and fast.
    The slow pointer moves one step at a time,
    while the fast pointer moves two steps at a time.

    When fast reaches the end of the list,
    slow will be pointing to the middle node.

    For an even-length linked list, this returns
    the second middle node.

Time Complexity:
    O(n)

Space Complexity:
    O(1)
"""


def middle_node(head):
    # Both pointers start from the head.
    slow = head
    fast = head

    # Continue while fast can move two steps.
    while fast and fast.next:
        # Slow moves one step.
        slow = slow.next

        # Fast moves two steps.
        fast = fast.next.next

    # Slow is now pointing to the middle node.
    return slow