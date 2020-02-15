#! python3
# phoneAndEmail.py - Finds phone numbers and emails on the clipboard

import pyperclip, re

phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # area code (matching one or zero via ?)
    (\s|-|\.)?          # separator (letter, dash, or period; matching one or zero)
    (\d{3})             # first 3 digits
    (\s|-|\.)           # separator (letter, dash, or period)
    (\d{4})             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (any number of spaces, ext,x,ext., any number of spaces, and 2to5 digits; matching one or zero)
    )''',re.VERBOSE)

# Create email regex.

emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username (letters, capital letters, number 0to9, ., _, %, +; matches one or more of preceding chars)
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name (matches one or more of preceding char)
    (\.[a-zA-Z]{2,4})    # dot-something (., letters, capitals, of length between 2to4 of preceding characters)
    )''',re.VERBOSE)

# Find matches in clipboard text.
text=str(pyperclip.paste())

matches=[]
for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phoneNum+=' x'+groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard with pyperclip
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')