#!/usr/bin/env python
# conding=utf-8

import os
import shutil

def copy_files(target_path, file_lists):
    for file_name in file_lists:
        print('install: ' + file_name)
        shutil.copy('./' + file_name, target_path + file_name)


rime_config_files = [
    'wubi86.dict.yaml',
    'wubi86.custom.yaml',
    'default.custom.yaml',
    'kaomoji.dict.yaml',
    'kaomoji.schema.yaml',
]

target_path = os.environ['APPDATA'] + os.sep + 'Rime' + os.sep
print('rime config directory: ' + target_path)
copy_files(target_path, rime_config_files)

# install git config
git_config_files = [
    '.gitconfig',
]
target_path = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'] + '\\'
print('git config directory: ' + target_path)
copy_files(target_path, git_config_files)

# git bash config
git_bash_config_files = [
    'aliases.sh',
]
target_path = 'D:\\Program Files\\Git\\etc\\profile.d'
print('git bash config directory: ' + target_path)
copy_files(target_path, git_bash_config_files)

input('press any key to exit.')
