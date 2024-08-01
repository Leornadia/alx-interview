#!/usr/bin/python3
"""
0x01. Lockboxes

This module contains a function that determines if all boxes can be opened.

You have n number of boxes, numbered from 0 to n-1. Each box has a key inside.
You can assume that all keys are unique. Each key can open a box with a
corresponding number.
For example, if the key inside box 1 is 3, then it can open box 3.
You are given an array of integers, where the ith element represents the
number of the key inside the ith box.

Determine if you can open all the boxes.

Example:
boxes = [1, 4, 3, 2, 5]
Output: True

Explanation:
Box 0 has key 1.
Box 1 has key 4.
Box 2 has key 3.
Box 3 has key 2.
Box 4 has key 5.

We can open box 0, then box 1, then box 4, then box 5, and finally box 2.

Example:
boxes = [0, 1, 1, 2]
Output: False

Explanation:
Box 0 has key 0.
Box 1 has key 1.
Box 2 has key 1.
Box 3 has key 2.

We can only open box 0, then box 1, and we're stuck. We can't open box 2 or 3.

"""


def canUnlockAllBoxes(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes: A list of integers representing the keys inside the boxes.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    n = len(boxes)
    opened_boxes = set([0])  
    available_keys = set([0])

    while len(available_keys) > 0:
        key = available_keys.pop()
        for box_num in range(n):
            if box_num not in opened_boxes and boxes[box_num] == key:
                opened_boxes.add(box_num)
                available_keys.add(box_num)

    return len(opened_boxes) == n

