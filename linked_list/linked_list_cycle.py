"""
Problem:
    Linked List Cycle

Pattern:
    Linked List + Fast & Slow Pointers

Approach:
    Use two pointers: slow and fast.
    The slow pointer moves one step at a time,
    while the fast pointer moves two steps at a time.
    
    If there is a cycle, both pointers will eventually
    meet at the same node.
    If there is no cycle, fast will reach the end of the list.

Time Complexity:
    O(n)

Space Complexity:
    O(1)
"""


def has_cycle(head):
    # Both pointers start from the head.
    slow = head
    fast = head

    # Continue while fast can move forward.
    while fast and fast.next:
        # Slow moves one step.
        slow = slow.next

        # Fast moves two steps.
        fast = fast.next.next

        # If both pointers meet, a cycle exists.
        if slow == fast:
            return True

    # Fast reached the end, so there is no cycle.
    return False