"""
Problem:
    Intersection of Two Linked Lists

Pattern:
    Linked List + Two Pointers

Approach:
    Use two pointers: pointerA and pointerB.
    Each pointer starts at the head of its own linked list.

    Both pointers move one step at a time.

    When a pointer reaches the end of its list,
    move it to the head of the other list.

    This makes both pointers travel the same total
    distance:

        Length of A + Length of B

    Therefore, if the two lists intersect, the pointers
    will eventually meet at the intersection node.

    If the lists do not intersect, both pointers will
    eventually become None at the same time.

Time Complexity:
    O(n + m)

Space Complexity:
    O(1)
"""


def get_intersection_node(headA, headB):
    # If either list is empty, there can be no intersection.
    if not headA or not headB:
        return None

    # Start each pointer at the head of its own list.
    pointerA = headA
    pointerB = headB

    # Continue until both pointers point to the same node.
    while pointerA != pointerB:

        # Move pointerA to the next node.
        # If it reaches the end, switch it to headB.
        if pointerA:
            pointerA = pointerA.next
        else:
            pointerA = headB

        # Move pointerB to the next node.
        # If it reaches the end, switch it to headA.
        if pointerB:
            pointerB = pointerB.next
        else:
            pointerB = headA

    # pointerA and pointerB are either:
    # 1. The intersection node, or
    # 2. None if there is no intersection.
    return pointerA