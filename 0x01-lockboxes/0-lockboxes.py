#!/usr/bin/python3
"""Module that contains the canUnlockAll function"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing lockboxes and keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True  
    queue = [0]  

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if not unlocked[key] and key < num_boxes:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)  

