#!/usr/bin/python3
def element_at(list, idx):
    if idx < 0 or idx > len(list):
        return None
    else:
        print("Element at index {:d} is {}".format(idx, list[idx]))
