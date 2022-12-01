#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argc = len(sys.argv)
    sum = 0
    for i in range(1, argc):
        num = int(sys.argv[i])
        sum += num
    print(sum)
