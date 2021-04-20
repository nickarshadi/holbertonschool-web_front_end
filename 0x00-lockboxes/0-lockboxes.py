#!/usr/bin/python3

def canUnlockAll(boxes):
    i = 0
    check = 0
    for i in range(len(boxes)):
        if i < 1:
            continue
        for keys in boxes:
            for key in keys:
                if i == int(key):
                    print(key)
                    check = 1
        if check == 0:
            return False
        check = 0
    return True
