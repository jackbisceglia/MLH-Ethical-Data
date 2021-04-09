#importing libraries 
import socket
import psutil
from signal import SIGKILL
from colorama import *

init()


def closePorts(options) -> None:

    ports = [int(i) for i in options]
    print(ports)