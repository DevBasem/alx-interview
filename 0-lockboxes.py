#!/usr/bin/python3
"""
Solution to the lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.

    Args:
        boxes (list): A list of lists representing locked boxes
        and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    # Initialize a set to keep track of opened boxes
    opened_boxes = {0}

    # Initialize a queue for BFS
    queue = [0]

    # BFS traversal
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                queue.append(key)

    # Check if all boxes can be opened
    return len(opened_boxes) == len(boxes)
