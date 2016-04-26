#!/usr/bin/env python

#import sys
#print(sys.version)

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def printTable(data):
    colWidth = []
    table = [ [], [], [], [] ]

    for line in range(len(data)):
        colWidth.append(0)

        for col in range(len(data[line])):
            length = len(data[line][col])

            if colWidth[line] < length:
                colWidth[line] = length

            str = data[line][col]
            table[col].append(str)

    for line in table:
        str = ''
        for col in range(len(line)):
            str += line[col].rjust(colWidth[col]) + ' '
        print(str.rstrip())


printTable(tableData)
