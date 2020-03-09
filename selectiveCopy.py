#! python3
# Usage - selectiveCopy.py walks through a folder tree and searches for
# files with a file extension .pdf into a new folder

import os, shutil
from pathlib import Path


def copyPDF(source, destination):
    '''copy PDFs in tree to single destination directory'''
    for foldername, subfolders, filenames in os.walk(source):
        for filename in filenames:
            if filename.endswith('.pdf'):
                # print((Path(foldername) / filename), destination)
                shutil.copy((Path(foldername) / filename), destination)


copyPDF('/Users/taya/Repos/PythonResources/AutomateTheBoringStuff/folderTesting', '/Users/taya/Repos/PythonResources/AutomateTheBoringStuff/pdfFolder')
