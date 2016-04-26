#!/usr/bin/env python

import sys
#print(sys.version)

print('Hello', ',', ' ', 'Dolly' , '!', sep='', end='n')
print('Hello', ',', ' ', 'Dolly' , '!', sep='', end='n')
sys.exit()

while True:
    action = input("Enter 'exit' to exit:    ")
    if action == 'exit':
        sys.exit()
    print("You've entered %s" % (action))
