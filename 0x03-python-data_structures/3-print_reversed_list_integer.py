#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ prints all integers of a list, in reverse order."""
    if my_list:
        for i in reversed(range(len(my_list))):
            print("{:d}".format(my_list[i]))
    else:
        return
