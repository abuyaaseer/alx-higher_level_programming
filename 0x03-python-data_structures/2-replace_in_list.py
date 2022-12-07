#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None

    lenth = len(my_list)

    if idx > (lenth - 1):
        return None

    my_list[idx] = element

    return (my_list)
