#!/usr/bin/env python3

import socket

seversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

seversocket.bind((host, port))

seversocket.listen(3)

while True:
    clientsocket, addess = seversocket.accept()
    
    print("Recieved connection from " % str(addess))
    
    message = 'hello! Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message)
    
    clientsocket.close()
    