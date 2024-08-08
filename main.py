import os
from rich import print
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

user = os.getlogin()

commands = {
        '1': 'feat',
        '2': 'upd',
        '3': 'bug-fix',
        '4': 'fix',
        '5': 'core',
        }

def menu():
    os.system('git status')

    table = Table(title="Star Wars Movies", row_styles=["none", "dim"])

    table.add_column("N%", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title")

    table.add_row("1", "[green]feat(A new feature)")
    table.add_row("2", "[yellow]upd(An update to an existing feature)")
    table.add_row("3", "[red]bug-fix(A bug fix)")
    table.add_row("4", "[red]fix(A hotfix)")
    table.add_row("5", "[blue]core(An install a new package)")
    table.add_row("6", "[green]lazygit")
    table.add_row("7", "[red]exit(Exit the script)")
    console = Console()
    console.print(table)
    choose = Prompt.ask("Choose one", default="1")
    if choose in ['1', '2', '3', '4', '5']:
        commit_message = Prompt.ask("Commit message")
        if commit_message == '':
            print('[red]Commit message is required')
            menu()
        git_command= f'git add . && git commit -m "{commands[choose]}: {commit_message}" && git push'
        os.system(git_command)
        print('[green]Done')
    else:
        if choose == '6':
            os.system('lazygit')
            menu()
        elif choose == '7':
            print('[red]Bye')
            exit()
        else:
            print('[red]Invalid option')
            menu()

if os.path.exists('.gpgrc'):
    # read file for each line
    with open('.gpgrc', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n', '')
            print(f'line: {line}')
            print(not os.path.exists(line))
            if not os.path.isfile(line):
                file_without_gpg = line.replace('.gpg', '')
                os.system(f'gpg -e -r {user} {file_without_gpg}')
                os.system(f'rm {file_without_gpg}')
    menu()
else:
    menu()
