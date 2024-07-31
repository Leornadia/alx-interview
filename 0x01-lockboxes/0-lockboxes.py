#!/usr/bin/python3
"""Module that contains the canUnlockAll function"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    :param boxes: list of lists representing the boxes and their keys
    :return: True if all boxes can be unlocked, False otherwise
    """
    n = len(boxes)
    unlocked = [1] + [0] * (n - 1)
    keys = [0]

    for key in keys:
        for new_key in boxes[key]:
            if new_key < n and not unlocked[new_key]:
                unlocked[new_key] = 1
                keys.append(new_key)

    return sum(unlocked) == n

