# importing libraries
import socket
import psutil
from signal import SIGKILL
from colorama import *

from .openPorts import openPorts

init()


def closePorts(options, history) -> None:

    ports_to_close = [int(i) for i in options]

    ports = openPorts([1], history)

    for port in ports_to_close:
        closed = 2
        for proc in psutil.process_iter():
            # proc = psutil.Process(proc)
            for conns in proc.connections(kind="inet"):
                if conns.laddr[1] == port:
                    if port in ports:
                        try:
                            proc.send_signal(SIGKILL)
                            closed = 1
                            # continue
                        except:
                            closed = 0

        if closed == 1:
            print(
                Fore.GREEN + "Success: " + Fore.RESET,
                "Port",
                port,
                "closed successfully\n",
            )
        elif not closed:
            print(
                Fore.RED + "Error: " + Fore.RESET,
                "There was an error in closing the port",
                port,
                "\n",
            )
        else:
            print(
                Fore.RED + "Error: " + Fore.RESET,
                "Either the port is not open, or is running a system process\n",
            )

    return
