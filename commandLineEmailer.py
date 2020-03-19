#! python3
# commandLineEmailer takes toEmail address, one-word toSubject as subject
# line, and string of email text as toMessage on the command line, logs
# in to email account (auth already) & sends toMessage string to the address.
# Stopped due to Gmail login automation limitation

import sys, logging, time
from selenium import webdriver

logging.basicConfig(filename='commandLineEmailer.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of commandLineEmailer.py')
# Get email address, subject, and email text from command line with sys
toEmail = sys.argv[1]
logging.debug(f'toEmail: {toEmail}')
toSubject = sys.argv[2]
logging.debug(f'toSubject: {toSubject}')
toMessage = ' '.join(sys.argv[3:])
logging.debug(f'toMessage: {toMessage}')

# Get myEmail and myPassword from environment variables

# TODO: open browser to Gmail and login with myEmail and myPassword
browser = webdriver.Chrome()
browser.get('https://accounts.google.com')
userElem = browser.find_element_by_name('identifier').send_keys(myEmail)
userNext = browser.find_element_by_css_selector('#identifierNext > span > span')
userNext.click()

browser.implicitly_wait(4)

passwordElem = browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
passwordElem.send_keys(myPassword)
passwordNext = browser.find_element_by_css_selector('#passwordNext > span > span').click()

# TODO: click to create new email message

# TODO: Input toEmail address

# TODO: input toSubject line

# TODO: input toMessage email body

# TODO: submit or click send

logging.debug('End of commandLineEmailer.py')
