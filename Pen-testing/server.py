#!/usr/bin/python3.13

import socket

serversocket = socket. socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serversocket.bind(('192.168.56.1', port))

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()

    print("received connection from %s " % str(address))

    message = 'hello! Thank you for connecting to the server. This is an example of how sockets can be used' + "\r\n"

    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()