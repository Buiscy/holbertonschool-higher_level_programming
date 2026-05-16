#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    i = len(argv)
    print('Arguments:{}'.format(i - 1))
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))

#for i in range(1, sys.argv):
#   print(i, sys.argv[i])