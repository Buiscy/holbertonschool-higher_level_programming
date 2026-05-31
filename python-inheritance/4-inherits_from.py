#!/usr/bin/python3
'''So this tests if things are same class'''
def inherits_from(obj, a_class):
    '''So this tests if things are same class'''
    return True if isinstance(obj, a_class) and type(obj) is not a_class else False