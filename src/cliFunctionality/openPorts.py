import socket  #importing library 


def openPorts(options) -> None:
    # TODO: insert common use cases for CLI eventually
  
    ip = '127.0.0.1'  #getting ip-address of host
    
    for port in range(1024, 65535):      #check for all available ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not s.connect_ex(('127.0.0.1', port)):
            print('[OPEN] Port open :',port) #print open port number
    

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