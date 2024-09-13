import os
from rich.panel import Panel
from rich import print
user = os.getlogin()

def addToGitIgnore(filename):
    with open('.gitignore', 'r') as file:
        # check if file is already in gitignore
        file.seek(0)
        lines = file.readlines()
    for line in lines:
        if line == filename:
            return
    with open('.gitignore', 'a') as file:
        file.write(filename + '\n')

def encryptFiles():
    # read file for each line
    if os.path.isfile('.gpgrc'):
        with open('.gpgrc', 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                print(Panel(f'[blue]encrypt line: {line}'))
                print(not os.path.exists(line))
                file_without_gpg = line.replace('.gpg', '')
                os.system(f'git rm --cached {file_without_gpg}')
                addToGitIgnore(file_without_gpg)
                if not os.path.isfile(line):
                    file_without_gpg = line.replace('.gpg', '')
                    os.system(f'gpg -e -r {user} {file_without_gpg}')
