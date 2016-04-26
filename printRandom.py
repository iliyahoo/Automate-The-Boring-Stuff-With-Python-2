#!/usr/bin/env python

import sys
#print(sys.version)

n = ''

if n == True:
    print('false')

sys.exit()


a = round(310.0123456, 5)
b = abs(a)
print(b)


n = 0
while n < 10:
    print(n + 1)
    n += 1


for i in range(10):
    print(i + 1)

from random import randint

for i in range(5):
    print(randint(1, 10))
