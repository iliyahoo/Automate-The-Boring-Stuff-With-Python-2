#!/usr/bin/env python
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import sys, pyperclip

#print(sys.version)
text = pyperclip.paste()
text_a = text.splitlines()

#sys.exit()

for i in range(len(text_a)):
    text_a[i] = "* " + text_a[i].strip()
text = "\n".join(text_a)
pyperclip.copy(text)
