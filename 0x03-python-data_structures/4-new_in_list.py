#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        # Return a copy of the original list if idx is out of range
        return my_list[:]
    else:
        # Create a new list with the modified element
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
