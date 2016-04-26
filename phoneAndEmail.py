#!/usr/bin/env python

import re, pyperclip

text = pyperclip.paste()
#text = "Cell: (415).555-9999 Work: 555 0000  Test: 112-234-5678 ext 34"
#email = "Iliya: iliya@strakovich.com; Viorika:viorika@strakovich.com Evgeniy-erRor.1+0-%@terst.ru"


emailRegex = re.compile(r'''
    \W                                  # separator
    ([\w|\.|%|\+|-]+)                   # user
    @                                   # at sign
    (\w+\.\w{2,3})                      # domain
    \W?                                 # separator
    ''', re.VERBOSE)

phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?                  # country code
    (?:\s|-|\.)?                        # separator
    (\d{3})                             # first 3 digits
    (?:\s|-|\.)                         # separator
    (\d{4})                             # last 4 digits
    (?:\s*(?:ext|x|ext.)\s*(\d{2,5}))?  # extension
    ''', re.VERBOSE)


phone = re.findall(phoneRegex, text)
email = re.findall(emailRegex, text)
matches = []

for groups in phone:
    code = groups[0].strip('()')
    phoneNum = "-".join([ code, groups[1], groups[2] ])
    if groups[3] != '':
        phoneNum += ' x' + groups[3]
    matches.append(phoneNum.lstrip('-'))


for groups in email:
    mail = "@".join([ groups[0], groups[1] ])
    matches.append(mail)

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")
