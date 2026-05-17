#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # the three -1's are, in order: Start point, stop point, incriment by.
    for index in range(len(my_list) - 1, - 1, - 1):
        print('{:d}'.format(my_list[index]))
