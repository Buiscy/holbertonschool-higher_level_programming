#!/usr/bin/python3
'''A class that can hold the value '''

class Square:
    '''A class with the value value inside it'''

    def __init__(self, size=0, position =(0,0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)


    @property
    def size(self):
        return self.__size

    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            any(not isinstance(x, int)for x in value) or
            len(value) != 2 or
            any(x < 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

 