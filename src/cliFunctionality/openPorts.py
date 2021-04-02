#importing libraries 
import socket
import psutil
from colorama import *

init()


def openPorts(options) -> None:
    # TODO: insert common use cases for CLI eventually

    data = {}

    pids = {}
    for p in psutil.process_iter():
        try:
            name = p.name()
            # print(name)
            pids[p.pid] = name
            data[name] = {'process': p}
        except(psutil.NoSuchProcess, psutil.ZombieProcess):
            pass

    connections = psutil.net_connections()

    for con in connections:
        if con.pid in pids and con.laddr[1]:
            print(Fore.GREEN + str(con.laddr[1]), " : ", Style.RESET_ALL + str(pids[con.pid]), )


    print("\n-----------\n")
  
    ip = '127.0.0.1'  #getting ip-address of host
    
    for port in range(1024, 65535):      #check for all available ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not s.connect_ex(('127.0.0.1', port)):
            print('[OPEN] Port open :' + Fore.GREEN, port, Style.RESET_ALL) #print open port number
    

        # try:
    
        #     serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
    
        #     serv.bind((ip,port)) # bind socket with address
                
        # except:
    
        #     print('[OPEN] Port open :',port) #print open port number
    
        s.close() #close connection


    # menu =''' Usage:
    
    # General Usage:
    # mlh -command [<optional-argument>]
    # my_program [<optional-argument>]
        
    # Popular Usage:
    # '''

    # print(menu)