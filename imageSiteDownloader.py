#! python3

# imageSiteDownloader.py goes to a photo-sharing site , searches for a category
# of photos based on sys.argv[1:], and downloads all the images to downloadPath

from pathlib import Path
import sys, logging, os, requests, bs4

logging.basicConfig(filename='imageSiteDownloader.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug(f'START OF PROGRAM')


def siteDownloader(searchText, maxResults, downloadPath):
    """
    Args:
        searchText (str): search query from sys.argv[1:]
        maxResults (int): max number of images to save to downloadPath
        downloadPath (str): path to download files into
    Returns:
        None
    """
    searchText = ' '.join(searchText).lower()

    # Create Response object for imgur site via requests module
    res = requests.get(f'https://imgur.com/search?q=' + searchText)
    res.raise_for_status
    try:                        # confirm response 200 OK
        res.raise_for_status()
    except Exception as exc:
        print(f'There was a problem: {exc}')
    logging.debug(len(res.text))

    # Parse res.text with bs4 to imageElems
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    logging.debug(f'Length of soup: {len(soup)}')
    imageElems = soup.select('.image-list-link img')[0:maxResults]  # finds image elements on page, and limits to maxResults images

    # Create folder from downloadPath arg
    print('Making directory from downloadPath pos arg string')
    os.makedirs(downloadPath, exist_ok=True)

    # Download images into new local folder
    if imageElems == []:
        logging.debug(f"Could not find any images for '{searchText}'")
    else:
        print(f'Downloading images for: {searchText}')
        for i in range(len(imageElems)):
            print('https:' + imageElems[i].get('src'))
            imageUrl = 'https:' + imageElems[i].get('src')
            res2 = requests.get(imageUrl)
            try:
                res2.raise_for_status()
            except Exception as exc:
                print(f'There was a problem {exc}')

            # download image to imageSiteDownloader/<image basename>/
            with open(Path(downloadPath) / os.path.basename(imageUrl), 'wb') as imageFile:
                for chunk in res2.iter_content(100000):
                    imageFile.write(chunk)

    logging.debug('END OF PROGRAM')


if __name__ == "__main__":
    siteDownloader(sys.argv[1:], 5, 'imageSiteDownloader/')
