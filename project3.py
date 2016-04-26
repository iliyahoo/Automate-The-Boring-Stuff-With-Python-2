#!/usr/bin/env python

import sys
#print(sys.version)


def collatz(num):
    try:
        num = int(num)
    except ValueError:
        print("It's impossible to convert \"%s\" into integer." % (num))
        sys.exit()

    while True:
        even = num % 2 == 0
        if even:
            num = num // 2
        else:
            num = 3 * num + 1

        print(num)

        if num == 1:
            break


if __name__ == '__main__':
    collatz(input("Enter integer number:    "))

