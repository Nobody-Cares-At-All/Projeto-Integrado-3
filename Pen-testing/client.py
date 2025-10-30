#!/usr/bin/python3.13

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 444

clientSocket.connect(('192.168.56.1', port))

message = clientSocket.recv(1024)

clientSocket.close()

print(message.decode('ascii'))