#! python3
# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4, logging
logging.basicConfig(filename='searchpypi.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s -  %(message)s')

logging.debug('Start of Program.')
print('Searching...')  # display text while donwloading the search result page.
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
logging.debug(f'res: {res}')
res.raise_for_status()
logging.debug(f'len of res.text: {len(res.text)}')

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')  # res.text passes in pg text
logging.debug(f'Type soup: {type(soup)}')

# Open a browser tab for reach result.
linkElems = soup.select('.package-snippet')
logging.debug(f'linkElems: {linkElems} Tags: {list(linkElems)}')
numOpen = min(5, len(linkElems))  # number tabs to open is either 5 or len of list: whichever is SMALLER
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')  # gets the href attribute value, which is a relative path from pypi.org page
    print('Opening', urlToOpen)
    logging.debug(f'fullUrl: {urlToOpen}')
    webbrowser.open(urlToOpen)
logging.debug('End of Program.')
