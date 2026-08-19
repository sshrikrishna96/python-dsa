"""
Problem:
    Remove Nth Node From End of Linked List

Pattern:
    Linked List + Fast & Slow Pointers + Dummy Node

Approach:
    Use two pointers: slow and fast.
    Both pointers start from a dummy node placed
    before the head.

    Move fast n + 1 steps ahead so that there is
    a gap of n nodes between slow and fast.

    Then move both pointers together until fast
    reaches the end of the list.

    At this point, slow will be pointing to the
    node just before the node that needs to be removed.

    Remove the node using:
        slow.next = slow.next.next

    Finally, return dummy.next because the head
    itself may have been removed.

Time Complexity:
    O(n)

Space Complexity:
    O(1)
"""


def remove_nth_from_end(head, n):
    # Create a dummy node before the head.
    # This makes removing the first node easier.
    dummy = ListNode(0)
    dummy.next = head

    # Both pointers start from the dummy node.
    slow = dummy
    fast = dummy

    # Move fast n + 1 steps ahead.
    # This creates a gap of n nodes between slow and fast.
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches the end.
    while fast is not None:
        # Fast moves one step.
        fast = fast.next

        # Slow moves one step.
        slow = slow.next

    # Slow is now at the node before the one
    # that needs to be removed.
    slow.next = slow.next.next

    # Return the new head.
    return dummy.next