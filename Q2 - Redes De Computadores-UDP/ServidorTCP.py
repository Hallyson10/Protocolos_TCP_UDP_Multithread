#import socket module
from socket import *
import sys # para terminar o programa
import os
import string,cgi,time
from http.server import BaseHTTPRequestHandler, HTTPServer

#Prepara o socket servidor
#codigo_inicio

HOST = ''              # Endereco IP do Servidor
PORT = 5030           # Porta que o Servidor esta
serverTcp = socket(AF_INET, SOCK_STREAM)
orig = (HOST, PORT)
serverTcp.bind(orig)
serverTcp.listen(1)

#codigo_fim

while True:
    #Estabelece a conexão
    print('Ready to serve...')
    
    #codigo_inicio
    connectionSocket, addr = serverTcp.accept() 
    #codigo_fim
    print ('Conectado por', addr)
    
    try:
        #codigo_inicio
        message = connectionSocket.recv(1024)
        #codigo_fim
        
        filename = message.decode().split()[1]
        #abrindo arquivo solicitado pelo cliente
        f = open(os.getcwd() + filename, 'r')

        #codigo_inicio
        outputdata = f.readlines()
        #transformando em vetor de linhas 
       
        #codigo_fim

        #Envia um linha de cabeçalho HTTP para o socket
        #codigo_inicio
        connectionSocket.send('HTTP/1.0 200 OK\n'.encode())
        connectionSocket.send('Content-type: text/html\n\n'.encode())
        #codigo_fim

        #Envia o conteúdo do arquivo solicitado ao cliente
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    
    except IOError:
        #Envia uma mensagem de resposta “File not Found”
        connectionSocket.send('HTTP/1.0 404 \n'.encode())
        connectionSocket.send('Content-type: text/html\n\n'.encode())
        #codigo_inicio
        connectionSocket.send('<html lang="en">'.encode())
        connectionSocket.send('<body>'.encode())
        connectionSocket.send('404 - File Not Found'.encode())
        connectionSocket.send('</body>'.encode())
        connectionSocket.send('</html>\r\n'.encode())
        #codigo_fim

        #Fecha o socket cliente
        #codigo_inicio
        connectionSocket.close()
        #codigo_fim
sys.exit()#Termina o programa depois de enviar os dados
