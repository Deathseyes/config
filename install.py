#!/usr/bin/env python
# conding=utf-8

import os
import shutil

fileList = [
    'wubi86.dict.yaml',
    'wubi86.custom.yaml',
    'default.custom.yaml',
]

targetPath = os.environ['APPDATA'] + os.sep + 'Rime' + os.sep
print('rime config directory: ' + targetPath)

for fileName in fileList:
    print('install: ' + fileName)
    shutil.copy('./' + fileName, targetPath + fileName)

input('press any key to exit.')
