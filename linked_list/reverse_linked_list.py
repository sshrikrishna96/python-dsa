"""
Problem:
    Reverse Linked List

Pattern:
    Linked List + Iteration

Approach:
    Reverse the direction of each node's pointer.
    Keep track of the previous node and the current node.
    Store the next node before changing the current node's pointer.
    Finally, return prev as the new head of the reversed list.

Time Complexity:
    O(n)

Space Complexity:
    O(1)
"""


def reverse_list(head):
    # prev stores the previous node.
    # Initially, there is no node before the head.
    prev = None

    # curr starts from the head of the linked list.
    curr = head

    while curr:
        # Store the next node before changing curr.next.
        nxt = curr.next

        # Reverse the current node's pointer.
        curr.next = prev

        # Move prev one step forward.
        prev = curr

        # Move curr one step forward using the saved next node.
        curr = nxt

    # prev is now the new head of the reversed linked list.
    return prev