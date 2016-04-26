#!/usr/bin/env  python

import re, os, sys, mimetypes

try:
    path, regex = sys.argv[1:]
except:
    print('''
Usage:
python %s <path> <regex>
        ''' % os.path.basename(sys.argv[0]))
    sys.exit()

regex = re.compile(r'%s' % regex)

if not path.startswith("/"):
    path = os.getcwd() + "/" + path

for root, dirs, files in os.walk(path):
    for file in files:
        file = os.path.join(root, file)
        with open(file, "r") as f:
            try:
                for line in f:
                    if re.search(regex, line):
                        print("%s    %s" % (file, line))
            except:
                continue
