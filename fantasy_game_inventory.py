#!/usr/bin/env python

#import sys
#print(sys.version)


def displayInventory(goods):
    print("Inventory:")
    total = 0
    for k, v in goods.items():
        print("%d    %s" % (v, k))
        total += v
    print("Total number of items: %d" % total)



def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory[i] = inventory.get(i, 0) + 1
    return inventory


if __name__ == '__main__':
#    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)


a = '''
    Hello there!
How are you doing?

I'm fine.
'''
print(a)


"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com
This program was designed for Python 3, not Python 2.
"""
def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')
help(spam)
help(__name__)
