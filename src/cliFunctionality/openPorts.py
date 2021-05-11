# importing libraries
import socket
import psutil
from colorama import *

init()


def openPorts(options, history) -> None:

    pids = {}  # To store all the processes t be compared to connections
    port_data = {}  # To store the process info about stuff running on that port
    allPorts = []  # To store all the ports to be returned

    ip = "127.0.0.1"  # getting ip-address of host

    # Loop through all the processes
    for p in psutil.process_iter():
        try:
            name = p.name()
            pids[p.pid] = name
        except (psutil.NoSuchProcess, psutil.ZombieProcess):
            pass

    # Loop through all the conenctions
    connections = psutil.net_connections()
    for con in connections:
        this_id = con.laddr[1]
        if con.pid in pids and this_id:
            try:
                port_data[this_id].add(str(pids[con.pid]))
            except KeyError:
                port_data[this_id] = {str(pids[con.pid])}

    # check if the function was calld from inside closePorts
    if not options:
        print(Fore.CYAN + "OPEN PORTS", Style.RESET_ALL)
        print("-----------")

    # Loop through all the ports
    for port in range(1024, 65535):  # check for all available ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not s.connect_ex(("127.0.0.1", port)):
            if not options:
                print(
                    Fore.GREEN, port, Style.RESET_ALL, ", ".join(port_data[port])
                )  # print open port number
            allPorts.append(port)
        s.close()  # close socket
    print()
    return allPorts
