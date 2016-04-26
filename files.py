#!/usr/bin/env python

import sys, os, shelve


shelveFile = shelve.open("stam")
key = "XYU"
shelveFile[key] = key
print(shelveFile[key])
shelveFile.close()
sys.exit()

file = os.path.join(os.getcwd(), "hello.txt")
if os.path.exists(file):
    file_obj = open(file, 'r')
    text = file_obj.read()
    print(text)
