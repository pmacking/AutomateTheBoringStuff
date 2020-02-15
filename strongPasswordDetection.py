import re

# A strong password is defined as one that is at least eight characters long,
# contains both uppercase and lowercase characters,
# has at least one digit.
# You may need to test the string against multiple regex patterns to validate its strength.

password='Asdfasd8'

passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8}$')

def checkPassword(text):
    return bool(passwordRegex.search(password))

assert checkPassword(password) is True