#import socket module
from socket import *
import sys # para terminar o programa
import os
import string,cgi,time
from http.server import BaseHTTPRequestHandler, HTTPServer
from _thread import *

#Prepara o socket servidor
#codigo_inicio

HOST = ''              # Endereco IPdo Servidor
PORT = 5030           # Porta que o Servidor esta
serverTcp = socket(AF_INET, SOCK_STREAM)
orig = (HOST, PORT)
serverTcp.bind(orig)
serverTcp.listen(1)

#codigo_fim

def respost(connectionSocket):
    #Estabelece a conexão
    print('Ready to serve...')

    
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

        resposta = 'HTTP/1.0 404\n'
        resposta += 'Content-type: text/html\n\n'
        resposta += '<html lang="en">'
        resposta += '<body>'
        resposta += '404 - File Not Found'
        resposta += '</body>'
        resposta += '</html>\r\n'
        connectionSocket.send(resposta.encode())

        connectionSocket.close()

    except FileNotFoundError:
        print("File not Found")
        resposta = 'HTTP/1.0 404\n'
        resposta += 'Content-type: text/html\n\n'
        resposta += '<html lang="en">'
        resposta += '<body>'
        resposta += '404 - File Not Found'
        resposta += '</body>'
        resposta += '</html>\r\n'
        connectionSocket.send(resposta.encode())

        connectionSocket.close()

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverTcp.accept()
   
    start_new_thread(respost, (connectionSocket, ))

serverSocket.close()
sys.exit()#Termina o programa depois de enviar os dados
