#!/usr/bin/python3
'''Behold a simple class that just prints a list'''
class MyList(list):
    '''it just prints and thats it'''
    def print_sorted(self):
        '''it does print in ascending order too'''
        print(sorted(self))