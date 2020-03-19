#!python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(filename="2048.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

gameUrl = 'https://play2048.co/'


def playGame():
    """
    Args: None
    Returns: None
    """
    logging.debug('START OF playGame')
    # open browser to 2048 game with selenium webdriver via chromedriver
    print(f'Opening Chrome to {gameUrl}')
    browser = webdriver.Chrome()
    browser.get(gameUrl)

    # find entire html tag in order to pass Keys to the full page
    htmlElem = browser.find_element_by_tag_name('html')
    # send up, right, down, left keys to htmlElem Webelement object
    while True:
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)


if __name__ == "__main__":
    playGame()
