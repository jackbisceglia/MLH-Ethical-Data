from colorama import *

import random

init()

all_ports = [
    "Since COVID-19, the US FBI reported a 300% increase in reported cybercrimes",
]


def funFacts(options) -> None:

    rand = random.choice(all_ports)
    print(Fore.GREEN + "> " + Fore.RESET + rand + "\n")

    