#!/usr/bin/env python

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

args = sys.argv

if len(args) == 2:
    # List keywords.
    if args[1].lower() == 'list':
        for i in range(len(mcbShelf)):
            print("%d. %s" % (i + 1, list(mcbShelf.keys())[i]))
    elif args[1].lower() == 'delete':
        answer = input("Do you really want to delete all of the keys?\nY/n\n")
        if answer == 'Y':
            for i in mcbShelf:
                del mcbShelf[i]
    else:
        try:
            pyperclip.copy(mcbShelf[args[1]])
        except:
            print("\"%s\" keyword does not exist." % args[1])
elif len(args) == 3:
    if args[1].lower() == 'delete':
        del mcbShelf[args[2]]
    # Save clipboard content.
    elif args[1].lower() == 'save':
        mcbShelf[args[2]] = pyperclip.paste()
else:
    print('''
+--------------------------------------------------------------------------+
|        mcb.pyw - Saves and loads pieces of text to the clipboard.        |
+--------------------------------------------------------------------------+
|                            USAGE:                                        |
+--------------------------------------------------------------------------+
|        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.            |
|        py.exe mcb.pyw list - Loads all keywords to clipboard.            |
|        py.exe mcb.pyw delete <keyword> - remove keyword from the shelve. |
+--------------------------------------------------------------------------+
        ''')

mcbShelf.close()
