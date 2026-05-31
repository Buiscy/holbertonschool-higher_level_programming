#!/usr/bin/python3
'''behold, its actually got something!'''
class BaseGeometry:
    '''Its got some furniture now'''
    def area(self):
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError ("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError ("{} must be greater than 0".format(name))