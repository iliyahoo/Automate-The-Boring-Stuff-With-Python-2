#!/usr/bin/env python

myPets = ['Zophie', 'Pooka', 'Fat-tail']

name = input("Enter pet name:    ")

if name not in myPets:
    print("I do not have %s pet." % name)
else:
    print("%s is my pet." % name)
