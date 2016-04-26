#!/usr/bin/env python

import sys
#print(sys.version)

def bounded_min(first, *args, lo=float("-inf"), hi=float("inf")):
    res = hi

    for arg in (first, ) + args:
        if arg < res and lo < arg < hi:
            res = arg
    return(max(lo, res))


result = bounded_min(-3, 0, 4, 6, 345, lo=0, hi=10)
print(result)
