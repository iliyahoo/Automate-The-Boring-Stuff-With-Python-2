#!/usr/bin/env python

import sys
#print(sys.version)

allGuests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
    }

def totalBrought(guests, goods):
    items = 0
    for guest, item in guests.items():
        items += item.get(goods, 0)
    return items


def printPicnic(items, left, right):
    print('PICNIC ITEMS'.center(left + right, '-'))
    for k, v in items.items():
        print(k.ljust(left, '.') + str(v).rjust(right))


spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('aSmp'))
sys.exit()


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
print()
printPicnic(picnicItems, 20, 6)


print('Number of things being brought:')
print(" - Apple Pies     %d" % totalBrought(allGuests, 'apple pies'))
print(" - apples     %d" % totalBrought(allGuests, 'apples'))
print(" - pretzels     %d" % totalBrought(allGuests, 'pretzels'))
print(" - ham sandwiches     %d" % totalBrought(allGuests, 'ham sandwiches'))
print(" - cups     %d" % totalBrought(allGuests, 'cups'))
print(" - cakes     %d" % totalBrought(allGuests, 'cakes'))
