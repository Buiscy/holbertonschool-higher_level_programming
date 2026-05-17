#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        # makes a copy
        new_in_list = my_list.copy()
        # modifies the element at index (idx) of the copied list
        new_in_list[idx] = element
        # returns the copy
        return (new_in_list)
