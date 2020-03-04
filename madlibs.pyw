#! python3

# madlibs.pyw - reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, VERB appears in text file.
# Usage: py.exe madlibs.pyw <file> - opens madlibs file, lets user
#       replace words based on prompts, prints file contents and writes new
#       file as '<file[-'.txt']>MadLibbed.txt'

import sys, re


file = open(f'{sys.argv[1]}')
text = file.read()
file.close()

regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

for i in regex.findall(text):
    reg = re.compile(r'{}'.format(i))
    inp_text = input('Enter the substitute for %s: ' %i)
    text = reg.sub(inp_text, text, 1)

print(text)

file = open(f'{sys.argv[1][:-4]}MadLibbed.txt', 'w')
file.write(text)
file.close()
