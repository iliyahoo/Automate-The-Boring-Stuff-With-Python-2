#!/usr/bin/env python

def eggs(someList):
    someList.append("Hello")

spam = [1, 2, 3]
#eggs(spam)
#print(spam)


import copy
spam = ['A', 'B', 'C', 'D']
copy_spam = copy.copy(spam)
copy_spam[1] = 'xxx'
print(spam)
print(copy_spam)
