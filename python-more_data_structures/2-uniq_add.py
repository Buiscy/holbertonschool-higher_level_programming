#!/usr/bin/python3
def uniq_add(my_list=[]):
    done_list = []
    total = 0
    for i in my_list:
        if i not in done_list:
            done_list.append(i)
    for num in done_list:
        total += num
    return(total)
