#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return(0)
    
    big = my_list[0] 
    for current in my_list:               
        if current > big:
            big = current
    return (big)

