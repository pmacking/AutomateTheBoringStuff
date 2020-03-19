#! python3

with open('withContextManager.txt', 'w') as outFile:
    outFile.write('Hello, ')

with open('withContextManager.txt', 'a') as outFile:
    outFile.write('World!')
