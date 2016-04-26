#!/usr/bin/env python

#import sys
#print(sys.version)

name = ''
while not name:
    name = input('Enter your name:    ')
print("Your name is %s." % (name))

numOfGuests = int(input('How many guests?    '))
if numOfGuests:
    print("Don't forget to order %d tickets." % (numOfGuests))

print('Done!')
exit()


while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break

print('Access granted.')
