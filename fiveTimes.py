#!/usr/bin/env python

#import sys
#print(sys.version)

n = 0
total = 0
while n <= 100:
    total += n
    n += 1
print(total)

raise(SystemExit)


total = 0
for n in range(100 + 1):
    total += n
print(total)


print("What's your name?")
for i in range(5):
    if i == 3:
        continue
    print('Jimmy Five Times (%d)' % (i))
