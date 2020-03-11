#! python3
# Usage: walks through a folder tree and searches for files or folders > 100MB

import os
from pathlib import Path


def getLarge(source):
    '''find files larger than 100MB'''

    for folderName, subfolders, filenames, in os.walk(source):
        print(f'searching for files > 100MB within {folderName}...')
        for filename in filenames:
            if os.path.getsize(Path(folderName) / filename) > 100000:
                print(f'{folderName}')
                print(f'LARGE: {filename}: {os.path.getsize(Path(folderName) / filename)}')
        print('\n')
    print('...search complete')


# getLarge() - add source path to init search
