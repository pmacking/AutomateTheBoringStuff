#! python3

import logging
import random
logging.basicConfig(filename='debuggingCoinTossLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

guessOptions = ('heads', 'tails')

logging.debug('Start of program.')
guess = ''
while guess not in guessOptions:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
assert guess in guessOptions, 'Guess is not heads or tails.'
logging.debug(f'First guess made was {guess}')

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug(f'Toss randint value is {toss}')
if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'
logging.debug(f'Toss string value is {toss}')

if toss == guess:
    print('You got it!')
else:
    guess2 = ''
    while guess2 not in guessOptions:
        print('Nope! Guess again! Enter heads or tails:')
        guess2 = input()
    logging.debug(f'Second guess made was {guess2}')
    assert guess2 in guessOptions, 'Guess is not heads or tails.'
    if toss == guess2:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program.')
