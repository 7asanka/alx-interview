#!/usr/bin/python3
"""
A module for working with lockboxes.
"""

def canUnlockAll(boxes):
    """ a method that determines if all the boxes can be opened."""

    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    opened = set([0])
    stack = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if 0 <= key < n and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == n
