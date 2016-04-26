#!/usr/bin/env python

import os, re, shutil


dir = "/Users/iliyas/repository/AutomateTheBorringStuffWithPython/test"


usDateRegex = re.compile(r'''
    ^(.*?)?                         # preffix
    ((?:[0][1-9])|(?:[1][0-2]))     # month
    -                               # separator
    ((?:[0-2][0-9])|(?:[3][01]))    # day
    -                               # separator
    ([12][0-9][0-9][0-9])           # year
    ((?:.*?)?\.txt)$                # suffix
    ''', re.I|re.VERBOSE)


euDateRegex = r'\1\3-\2-\4\5'


for folder, subfolder, files in os.walk(dir):
    for file in files:
        euDate = re.sub(usDateRegex, euDateRegex, file)
        if euDate == file:
            continue
        print("- %s" % file)
        print("+ %s" % euDate)
        accept = input("Y/n:    ")
        if accept == "Y":
            shutil.move(os.path.join(folder, file), os.path.join(folder, euDate))
