#!/usr/bin/python3
"""Module that contains the canUnlockAll function"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    :param boxes: list of lists representing the boxes and their keys
    :return: True if all boxes can be unlocked, False otherwise
    """
    if not boxes or len(boxes) == 0:
        return False
    
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]
    
    for key in keys:
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])
    
    return all(unlocked)
