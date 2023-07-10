#!/usr/bin/python3
"""
0-lockboxes.py
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """ 
    a method that determines if all the boxes can be opened.
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
