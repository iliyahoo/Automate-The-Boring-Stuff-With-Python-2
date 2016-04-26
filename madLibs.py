#!/usr/bin/env  python

import sys, os, re

adjectiveRegex = re.compile(r'ADJECTIVE')
nounRegex = re.compile(r'NOUN')
verbRegex = re.compile(r'VERB')

with open('madLibs.txt', 'r') as file:
    with open('madLibs_upd.txt', 'w') as file_upd:
        for line in file:
            line_upd = ''
            for word in line.split():
                if re.search(adjectiveRegex, word):
                    sub = input("Enter an adjective:    ")
                    word = re.sub(adjectiveRegex, sub, word)
                elif re.search(nounRegex, word):
                    sub = input("Enter a noun:    ")
                    word = re.sub(nounRegex, sub, word)
                elif re.search(verbRegex, word):
                    sub = input("Enter a verb:    ")
                    word = re.sub(verbRegex, sub, word)
                line_upd += word + " "
            print(line_upd)
            file_upd.write(line_upd)
