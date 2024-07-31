#!/usr/bin/python3
"""
Module for the canUnlockAll function.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    :param boxes: A list of lists where each inner list contains keys to other boxes.
    :return: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = set([0])  # Set to keep track of unlocked boxes
    keys = set(boxes[0])  # Set of available keys, starting with keys in the first box
    
    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])
    
    return len(unlocked) == n

# Test cases (main_0.py)
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
