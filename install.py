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

# install git config
git_config_files = [
    '.gitconfig',
]
target_path = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
print('git config directory: ' + target_path)
for file_name in git_config_files:
    print('install: ' + file_name)
    shutil.copy('./' + file_name, targetPath + file_name)

input('press any key to exit.')
