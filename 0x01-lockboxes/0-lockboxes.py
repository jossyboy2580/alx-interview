#!/usr/bin/python3
"""
A Lockboxes puzzle solver using a greedy algorithm
"""


def openbox(box, key, opened):
    """ open a box"""
    if key in opened:
        return
    opened.add(key)
    for n_key in box[key]:
        openbox(box, n_key, opened)
    return


def canUnlockAll(boxes):
    """
    This function takes a list of list

    where each item(list) is a collection of keys to other boxes, the
    first one is opened by default
    """

    if len(boxes) < 2:
        return True
    opened = set()
    openbox(boxes, 0, opened)
    if set(range(len(boxes))).issubset(opened):
        return True
    return False
