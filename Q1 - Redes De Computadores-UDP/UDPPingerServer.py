#by Hallyson Miranda

# UDPPingerServer.py
#o modulo socket é a base para toda a comunicação Python em rede
# precisaremos do módulo random para gerar perdas de pacotes aleatórias
import random
from socket import *

# Cria um socket UDP
# Note o uso de SOCK_DGRAM para pacotes UDP
#serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)

#atribui uma porta ao servidor
serverPort = 5000
# Atribui um endereço IP e um número de porta ao socket
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    # Gera um número aleatório de 0 a 10
    rand = random.randint(0, 10)
    # Recebe do cliente o pacote junto com seu endereço de destino
    message, address = serverSocket.recvfrom(1024)
    # Escreve a mensagem em letras maiúsculas
    message = message.decode()
    message = message.upper()
    message = message.encode()
    # Se rand < 3, consideramos que o pacote foi perdido
    #Coloquei o 3 porque o índice começa do 0
    if rand < 3:
        print(rand)
        continue
        # Caso contrário, o servidor responde
    serverSocket.sendto(message, address)

