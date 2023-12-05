#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()

    if 0 <= idx < len(my_list):
        copied_list[idx] = element
        return copied_list
    else:
        return my_list
