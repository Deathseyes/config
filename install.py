#!/usr/bin/env python
# conding=utf-8

import os
import shutil

fileList = [
    'wubi86.dict.yaml',
    'wubi86.custom.yaml',
]

targetPath = os.environ['APPDATA'] + os.sep + 'Rime' + os.sep
for fileName in fileList:
    shutil.copy('./' + fileName, targetPath + fileName)

input('press any key to exit.')
