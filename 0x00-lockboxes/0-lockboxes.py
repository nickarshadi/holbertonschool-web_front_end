#!/usr/bin/python3
"""Unlock all boxes Module."""


def canUnlockAll(boxes):
    """Open all boxes."""
    keys = {0}
    allkeys = {0}
    i = 0
    v = 0
    while i < 100:
        for key in boxes[v]:
            keys.add(key)
            allkeys.add(key)
        if len(allkeys) >= len(boxes):
            return True
        if keys:
            v = keys.pop()
        else:
            return False
        print("Added box {}".format(v))
        i += 1
    return False
