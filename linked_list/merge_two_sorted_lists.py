"""
Problem:
    Merge Two Sorted Lists

Pattern:
    Linked List + Two Pointers

Approach:
    Use a dummy node to build the merged linked list.
    Compare the values of both lists and attach the smaller node
    to the merged list.
    Move forward in the list from which the node was selected.
    Once one list is exhausted, attach the remaining nodes
    from the other list.

Time Complexity:
    O(n + m)

Space Complexity:
    O(1)
"""


def merge_two_lists(list1, list2):
    # Dummy node acts as the starting point of the merged list.
    dummy = ListNode(0)

    # curr keeps track of the last node in the merged list.
    curr = dummy

    while list1 and list2:
        # Select the smaller value and attach it to the merged list.
        if list1.val < list2.val:
            curr.next = list1

            # Move curr to the node we just added.
            curr = list1

            # Move list1 to its next node.
            list1 = list1.next

        else:
            curr.next = list2

            # Move curr to the node we just added.
            curr = list2

            # Move list2 to its next node.
            list2 = list2.next

    # Attach whichever list still has remaining nodes.
    curr.next = list1 if list1 else list2

    # dummy.next is the actual head of the merged list.
    return dummy.next