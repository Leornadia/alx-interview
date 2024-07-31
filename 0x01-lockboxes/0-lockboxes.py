#!/usr/bin/python3
"""Module that contains the canUnlockAll function"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    :param boxes: list of lists representing the boxes and their keys
    :return: True if all boxes can be unlocked, False otherwise
    """
    if not boxes:
        return False
    
    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])
    
    while keys:
        new_key = keys.pop()
        if new_key not in unlocked:
            if 0 <= new_key < n:
                unlocked.add(new_key)
                keys.update(set(boxes[new_key]) - unlocked)
    
    return len(unlocked) == n
