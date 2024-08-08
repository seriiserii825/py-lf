import os
from rich import print
from rich.panel import Panel
user = os.getlogin()
def decryptFiles():
    with open('.gpgrc', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n', '')
            print(Panel(f'[blue]decrypt line: {line}'))
            file_without_gpg = line.replace('.gpg', '')
            print(not os.path.exists(file_without_gpg))
            if not os.path.isfile(file_without_gpg):
                os.system(f'gpg -d {line} > {file_without_gpg}')
                os.system(f'rm {line}')

