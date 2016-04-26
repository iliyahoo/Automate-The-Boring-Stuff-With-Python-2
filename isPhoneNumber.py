#!/usr/bin/env python

import sys, re
#print(sys.version)


# have to be done !!!!!!!!!!!!!!!!!!
str = '1234'
str = '42'
str = '12,34,567'
str = '6,368,745'
str = '1,234'

num = re.compile(r'''
    ^
    \d{1,3}
    (?:,\d{3})*
    $
    ''', re.VERBOSE)

mo = re.findall(num, str)
print(mo)

#    (?:\d{1,3})
sys.exit()

def custom_strip(string, char=""):
    print(string)
    stringRegex = re.compile(r'(%s*)(?:.*)(%s*)' % (char, char))
    match = re.sub(stringRegex, "", string, count=0)
    print(match)

if __name__ == '__main__':
    string = "XXHello,XXXXX Dolly!XXX"
    char = "X"
    custom_strip(string, char)


def password(pw):
    len_error = len(pw) < 8
    uppercase_error = re.search('[A-Z]', pw) is None
    downcase_error = re.search('[a-z]', pw) is None
    digit_error = re.search('[0-9]', pw) is None
    pass_ok = not (len_error or uppercase_error or downcase_error or digit_error)
    return {
        "pass_ok" : pass_ok,
        "len_error" : len_error,
        "uppercase_error" : uppercase_error,
        "downcase_error" : downcase_error,
        "digit_error" : digit_error
    }
pw = "Qwerty12345"
print(password(pw))


names = '''
    Satoshi Nakamoto    Alice Nakamoto    RoboCop Nakamoto but not the following:
   satoshi Nakamoto (where the first name is not capitalized)
   Mr. Nakamoto (where the preceding word has a nonletter character)
   Nakamoto (which has no first name)
   Satoshi nakamoto (where Nakamoto is not capitalized)
'''

fullNames = re.compile(r'''
    [A-Z][A-Za-z]+     # first name
    \s+             # separator
    Nakamoto
    ''', re.VERBOSE|re.DOTALL)

mo = re.findall(fullNames, names)

print(mo)


text = '''
    Alice eats apples.
    Bob pets cats.
    Carol throws baseballs.
    Alice throws Apples.
    BOB EATS CATS.
    Robo op eats apples.
    ALICE THROWS FOOTBALLS.
    Carol eats 7 cats.
'''

sent = re.compile(r'''
    (?:Alice|Bob|Carol)               # first word
    \s
    (?:eats|pets|throws)              # second word
    \s
    (?:apples|cats|baseballs)         # third word
    \.                              # ends with a period
    ''', re.I|re.VERBOSE|re.DOTALL)

mo = re.findall(sent, text)
for i in mo:
    print(i)


str = "fgsgferge: iliya@strakovich.com gdfgdfg  gdfg"

emailRegex = re.compile(r'''
    ([a-zA-Z0-9-%+.]+)
    @
    ([a-zA-Z0-9]+)
    (\.\w{2,3})
    ''', re.VERBOSE)

mo = re.findall(emailRegex,str)
print(mo)


#phoneNumRegex = re.compile(r'(\d{3}-){2}(\d{4})')
#message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
#mo = re.search(phoneNumRegex, message)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo)


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    if text[3] + text[7] != '--':
        return False
    for i in list(range(0, 3)) + list(range(4, 7)) + list(range(8, 12)):
        if not text[i].isdecimal():
            return False
    return True


for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: %s" % chunk)

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
