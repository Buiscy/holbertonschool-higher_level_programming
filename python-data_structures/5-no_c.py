#!/usr/bin/python3
def no_c(my_string):
    text = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            text += char
    return (text)