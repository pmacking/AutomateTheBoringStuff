#! python3

# Usage: testing on directory management, and printing from os.walk

import os
from pathlib import Path

p = Path.cwd()
# os.makedirs(p / 'testing/folder/management/')
# os.makedirs(p / 'testing/folder2/management2/')
# os.makedirs(p / 'testing/folder2/management3/')

for folderName, subfolders, filenames in os.walk(p):
    print(f'Current folder: {folderName}')
    for subfolder in subfolders:
        print(f'Subfolder of {folderName}: {subfolder}')
    for filename in filenames:
        print(f'Filename in {folderName}: {filename}')
    print("\n")
