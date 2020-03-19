#! python3
# mapIt.py - Launches a map browser using an address from the CLI or clipbard

import webbrowser, sys, pyperclip
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -  %(message)s')

logging.debug('Start of program.')
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    logging.debug(f'Address from sys.argv: {address}')
else:
    # Get address from clipboard
    address = pyperclip.paste()
    logging.debug(f'Address from pyperclip: {address}')

webbrowser.open('https://www.google.com/maps/place/' + address)
logging.debug('Opened browser to address.')

