#!/usr/bin/python3
if __name__ == "__main__": #Stop it from actioning on load
    import hidden_4 #imports hidden_4. do note that 4-hidden_discovery.py/Task-4 is in tmp, and Hidden_4 in the task is downloaded. Likely task has both files in tmp as it downloads
    names = dir(hidden_4) #names is the variable. dir() returns all the modules in the file. E.G dir(hidden_4) here returns any modules inside that file.
    for name in sorted(names): #sorted function sorts by default alphabetically
        if not name.startswith("__"): #filtering out any modules that start with __. startswith() is a function that checks the start of a file name
            print(name)#