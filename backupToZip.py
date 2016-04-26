#!/usr/bin/env python
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os, sys

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)   # make sure folder is absolute
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = "%s_%d.zip" % (os.path.basename(folder), number)
        if not os.path.exists(os.path.join(folder, zipFilename)):
            break
        number += 1
    # TODO: Create the ZIP file.
    zip = zipfile.ZipFile(zipFilename, 'w')
    # TODO: Walk the entire folder tree and compress the files in each folder.
    for folder, subfolders, files in os.walk(folder):
        for file in files:
            zip.write(os.path.join(folder, file))
    print('Done.')

backupToZip('.')
