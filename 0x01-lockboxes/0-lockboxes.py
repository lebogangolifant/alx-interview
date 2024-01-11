#!/usr/bin/python3
"""
Lockboxes Algorithm
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (list of lists): Each box contains a list of keys.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    keys = set(boxes[0])
    opened = {0}

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in opened and key < n:
                stack.append(key)
                opened.add(key)
                keys.add(key)

    return len(opened) == n
