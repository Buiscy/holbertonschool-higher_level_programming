#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def pad (t):    #takes in a tuple, and pads out each of the two indexs if they dont exist
        i = t[0] if len(t) > 0 else 0
        j = t[1] if len(t) > 1 else 0
        return (i, j) # returns each index
    a = pad(tuple_a)
    b = pad(tuple_b)
    
    return (a[0] + b[0], a[1] + b[1])
