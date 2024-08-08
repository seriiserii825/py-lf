import os
from rich.panel import Panel
from rich import print
user = os.getlogin()
def encryptFiles():
    # read file for each line
    with open('.gpgrc', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n', '')
            print(Panel(f'[blue]encrypt line: {line}'))
            print(not os.path.exists(line))
            if not os.path.isfile(line):
                file_without_gpg = line.replace('.gpg', '')
                os.system(f'gpg -e -r {user} {file_without_gpg}')
                os.system(f'rm {file_without_gpg}')

