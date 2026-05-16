#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    result = 0
    if len(argv) < 2:
        print('invalid operations')
        exit(1)
    try:
        total = sum(int(x) for x in argv[1:])
        print('{}'.format(total))
    except:
        print('error: require valid ints')

    #for index in range(1, len(argv)):
    #    result += int(argv[index])
    #print('{:d}'.format(result))