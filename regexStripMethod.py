import re

#Write a function that takes a string and does the same thing as the strip() string method.
#If no other arguments are passed other than the string to strip,
#then whitespace characters will be removed from the beginning and end of the string.
#Otherwise, the characters specified in the second argument to the function will be removed from the string.

def strip(s, char=None):
    if char is None:
        stripRegex=re.compile(r'(\s*)(\w*)(\s*)')
    else:
        stripRegex=re.compile(r'^([char]*)(\w*?)([char]*)$')
    return stripRegex.search(s).group(2)

print(strip(' asdf '))
print(strip('aaateststringaaa', 'a'))