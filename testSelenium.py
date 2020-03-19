#! python3

from selenium import webdriver
import time
# this import from SENDING SPECIAL KEYS below is to reduce code length
from selenium.webdriver.common.keys import Keys

# CLICKING THE PAGE
browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read Online for Free')
linkElem.click()  # follows the "Read Online for Free" link
browser.back()  # Clicks the back button on the browser
time.sleep(2)
browser.forward()  # Clicks the Forward button
time.sleep(2)
browser.refresh()  # Clicks the Refresh/Reload button
time.sleep(2)
browser.quit()

# FILLING OUT AND SUBMITTING FORMS
browser = webdriver.Chrome()
browser.get('https://login.metafilter.com')  # gets url page
userElem = browser.find_element_by_id('user_name')  # finds user_name field
userElem.clear()  # clears potential text in the user_name field
time.sleep(1)
userElem.send_keys('Fine_user')  # inputs Fine_user into user field
passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('Hell_ya_thats_my_password')  # inputs password
passwordElem.clear()  # clears potential text in the field
time.sleep(1)

passwordElem.submit()  # submit() method on any element in a form submits form
browser.quit()  # quits the browser session

# SENDING SPECIAL KEYS
browser = webdriver.Chrome()
browser.get('https://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')  # finds the WHOLE page
htmlElem.send_keys(Keys.END)     # scrolls to bottom of page
time.sleep(4)
htmlElem.send_keys(Keys.HOME)    # scrolls to top of page
time.sleep(4)
browser.quit()
