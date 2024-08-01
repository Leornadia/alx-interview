#!/usr/bin/python3
"""Module that contains the canUnlockAll function"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    :param boxes: list of lists
    :return: True if all boxes can be opened, else False
    """
    n = len(boxes)
    unlocked_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked_boxes:
            unlocked_boxes.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked_boxes) == n
