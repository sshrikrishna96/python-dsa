"""
Problem:
    Valid Parentheses

Pattern:
    Stack

Approach:
    Use a stack to keep track of opening brackets.

    When an opening bracket is found, push it onto the stack.

    When a closing bracket is found, check whether the top of the
    stack contains its matching opening bracket.

    If they match, remove the opening bracket from the stack.
    If they do not match, the string is invalid.

    At the end, the stack must be empty for the parentheses
    to be valid.

Time Complexity:
    O(n)

Space Complexity:
    O(n)
"""


def is_valid(s):
    # Stack stores opening brackets.
    st = []

    # Process every character in the string.
    for c in s:

        # Opening brackets are pushed onto the stack.
        if c == '(' or c == '[' or c == '{':
            st.append(c)

        else:
            # A closing bracket cannot be valid if there is
            # no opening bracket available to match it.
            if not st:
                return False

            # Get the most recently added opening bracket.
            top = st[-1]

            # Check whether the closing bracket matches the top.
            if (c == ')' and top == '(') or \
               (c == ']' and top == '[') or \
               (c == '}' and top == '{'):

                # Matching pair found, so remove the opening bracket.
                st.pop()

            else:
                # Closing bracket does not match the opening bracket.
                return False

    # The string is valid only when all opening brackets
    # have been matched and removed.
    return not st