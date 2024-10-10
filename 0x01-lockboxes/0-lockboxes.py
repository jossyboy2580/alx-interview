#!/usr/bin/python3
"""
A Lockboxes puzzle solver using a greedy algorithm
"""


def canUnlockAll(boxes):
    """
    This function takes a list of list

    where each item(list) is a collection of keys to other boxes, the
    first one is opened by default
    """

    if len(boxes) < 2:
        return True

    keys = boxes[0][:]
    visited = {0}

    i = 0
    for key in keys:
        if key not in visited:
            visited.add(key)
            keys.extend(boxes[key])
    if visited == set(range(len(boxes))):
        return True
    return False
