#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4, logging
logging.basicConfig(filename='downloadXkcd.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Program Start')
url = 'https://xkcd.com'    # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

while not url.endswith('#'):
    # Download the page.
    print(f'Downloading page {url}...')
    logging.debug(f'Downloading page {url}')
    res = requests.get(url)
    logging.debug(f'res: {res}')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    logging.debug(f'Length of soup: {len(soup)}')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')  # arg could be 'div #comic'
    if comicElem == []:  # if element not found in div
        print(f'Could not find comic image @ {url}')
        logging.debug(f'Could not find comic image @ {url}')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')  # gets image src path and appends to https: prefix
        logging.debug(f'str(comicElem[0]): {str(comicElem[0])}')

        # Download the image
        print(f'Downloading image {comicUrl}...')
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel = "prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
    logging.debug(f'While loop end.')

print('Done.')
logging.debug('Program End.')
