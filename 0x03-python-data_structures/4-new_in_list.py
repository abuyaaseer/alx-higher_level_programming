#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    lenth = len(my_list)

    if idx > lenth - 1:
        return my_list

    new_list = my_list[:]
    new_list[idx] = element

    return new_list
