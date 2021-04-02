from colorama import *

init()


def helpMenu(options) -> None:
    # TODO: insert common use cases for CLI eventually
    print(Fore.CYAN + Style.BRIGHT + 'Usage:')
    print(Style.BRIGHT + Fore.CYAN + 'General Usage:' + Style.RESET_ALL)
    print(Fore.RED + 'mlh -command ' +  Fore.GREEN + '[<optional-argument>]')
    print(Fore.RED + 'my_program ' +  Fore.GREEN + '[<optional-argument>]')
    print()
    print(Fore.CYAN + Style.BRIGHT + 'Popular Usage:' + Style.RESET_ALL)
    print(Fore.GREEN + 'mlh -h or mlh -help: ' +  Fore.RESET + 'View the help page')
    print(Fore.GREEN + 'mlh -o: ' +  Fore.RESET + 'View the open ports with the ' + Style.BRIGHT + 'process running and process ID' + Style.RESET_ALL)
    print(Fore.GREEN + 'mlh -c <port number>: ' +  Fore.RESET + 'Close the specified port')
    print(Fore.GREEN + 'mlh -f: ' +  Fore.RESET + 'View a random fact about port security')

    

    # print(menu)