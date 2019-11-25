from socket import *
import sys

args = sys.argv

HOST = args[1]
PORT = int(args[2])
filename = args[3]

print(HOST)
print(PORT)
print(filename)

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.connect((HOST, PORT))

serverSocket.send(('GET ' + filename + ' HTTP/1.0\n').encode())
resposta = serverSocket.recv(1024)

print(resposta.decode())
