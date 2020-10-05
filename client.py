from socket import *

serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print("*****Rock, Paper or Scissors*****")
clientChoice = input("Digit rock, paper or scissors:")
clientSocket.send(clientChoice.encode())
modifiedSentence = clientSocket.recv(1024)
print ("From Server:", modifiedSentence)
clientSocket.close()