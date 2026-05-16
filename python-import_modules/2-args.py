#!/usr/bin/python3
#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    if (argc == 0):
        print(f"{argc} arguments.")
    elif (argc == 1):
        print(f"{argc} argument:")
    else:
        print(f"{argc} arguments:")
    for arg in range(1, argc + 1):
        print(f"{arg}: {argv[arg]}")





#from sys import argv
#if __name__ == '__main__':
#    i = len(argv)
#    print('Arguments:{}'.format(i - 1))
#    for i in range(1, len(argv)):
#        print("{:d}: {}".format(i, argv[i]))