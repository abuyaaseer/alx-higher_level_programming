#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if not my_list:
        pass

    else:
        my_list.reverse()
        lenth = len(my_list)

        for i in range(lenth):
            print("{:d}".format(my_list[i]))
