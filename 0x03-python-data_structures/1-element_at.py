#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    elif idx < 0 or idx >= len(my_list):
        return None
