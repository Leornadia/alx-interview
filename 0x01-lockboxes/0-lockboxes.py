#!/usr/bin/python3
"""Module that contains the canUnlockAll function"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked using depth-first search.
    
    :param boxes: list of lists representing the boxes and their keys
    :return: True if all boxes can be unlocked, False otherwise
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    def dfs(box):
        for key in boxes[box]:
            if isinstance(key, int) and 0 <= key < n and not visited[key]:
                visited[key] = True
                dfs(key)

    dfs(0)
    return all(visited)
