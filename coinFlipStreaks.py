import random

runs = 10000
numberOfStreaks = 0
flipsPerRun = 100
streakLength = 6

for i in range(runs):
    #Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for _ in range(flipsPerRun):
        if random.randint(0, 1) == 0:
            flips.append('heads')
        else:
            flips.append('tails')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    currentStreak = 0
    previousFlip = None
    for flip in flips:
        if flip == previousFlip:
            currentStreak += 1
            if currentStreak == streakLength:
                numberOfStreaks += 1
                break
            else:
                currentStreak = 0
            previousFlip = flip

print('Chance of streak: %s%%' % (numberOfStreaks / 100))