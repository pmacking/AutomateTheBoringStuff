def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argumet.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))