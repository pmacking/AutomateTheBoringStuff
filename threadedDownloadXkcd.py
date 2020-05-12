#! python3
# threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)  # makes dir ./xkcd.


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print(f'Downloading page https://xkcd.com/{urlNumber}')
        res = requests.get(f'https://xkcd.com/{urlNumber}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')

            # Download the image.
            print(f'Downloading image {comicUrl}')
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            with open(os.path.join(
                     'xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)

            # Create and start the Thread objects.
            downloadThreads = []  # a list of all the Thread objects
            for i in range(0, 140, 10):  # loops 14 times, creates 14 threads
                start = i
                end = i + 9
                if start == 0:
                    start = 1  # There is no comic 0, so set it to 1.
                downloadThread = threading.Thread(target=downloadXkcd,
                                                  args=(start, end))
                downloadThreads.append(downloadThread)
                downloadThread.start()

            # Wait for all threads to end.
            for downloadThread in downloadThreads:
                downloadThread.join()
            print('Done.')
