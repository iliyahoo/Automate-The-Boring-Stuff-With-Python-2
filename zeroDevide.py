#!/usr/bin/env python

import sys
print(sys.version)


def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)

sys.exit()


def divide(first, second):
    return(first / second)

try:
    print(divide(42, 42))
    print(divide(42, 1))
    print(divide(42, 0))
    print(divide(42, 10))
except(ZeroDivisionError):
    print("division by %s" % ("zero"))

print("end of program")
