#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        # Return the original list unchanged if idx is out of range
        return my_list
    else:
        # Replace the element at idx with the new element
        my_list[idx] = element
        return my_list
