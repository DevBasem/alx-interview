#!/usr/bin/python3
"""
Method that determines if all the boxes can be opened.
"""
def canUnlockAll(boxes):
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
