from colorama import *

import random

init()

all_ports = [
    [
        "There are 65,535 virtual ports and all of them are related to network communications.",
        "https://helpdeskgeek.com/networking/hdg-explains-what-is-a-computer-port-what-are-they-used-for/",
    ],
]


def funFacts(options, history) -> None:

    rand = random.choice(all_ports)
    print(Fore.GREEN + "> " + Fore.RESET + rand[0])
    print(Fore.GREEN + "Source: " + Fore.RESET + rand[1] + "\n")
