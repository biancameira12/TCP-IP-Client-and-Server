from socket import *
from random import seed
from random import random

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("127.0.0.1",serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
seed(1)
print(random(), random(), random())
while 1:
	connectionSocket, addr = serverSocket.accept()
	clientChoise = connectionSocket.recv(1024)
	options = ["rock", "paper", "scissors"]
	serverChoise = options[((int)(10*random())%3)]
	if serverChoise == "rock":
		if clientChoise == "paper":
			response = "Win!"
		else: response = "Lost!"
	elif serverChoise == "paper":
		if clientChoise == "scissors":
			response = "Win!"
		else: response = "Lost!"
	else:
		if clientChoise == "paper":
			response = "Win!"
		else: response = "Lost!"
	print(clientChoise, serverChoise)
	connectionSocket.send(response)
	connectionSocket.close()