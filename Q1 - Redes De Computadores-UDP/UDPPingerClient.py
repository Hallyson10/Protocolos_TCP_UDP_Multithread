#by Hallyson Miranda

import time
from datetime import datetime
from socket import *


#o nome ou IP do servidor. Se nome, uma consulta DNS será realizada. Porta do servidor.
serverName = 'localhost'

#serverPort = 5000
serverPort = 5000


#criando socket cliente. indicando o endereço IPv4 e o segundo UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

#se a porta não é especificada, o SO escolhe uma aleatória
clientSocket.settimeout(1.0)

#estão contidos na msg
ping = ""
numseq = 0
Time = datetime.now()
modifiedMessage = ""


for i in range(10):
    #incrementando o i de 0 até 9 nesse caso
    nseq = i+1
    Time = datetime.now() 
    ping = "PING " + str(numseq) + " " + str(Time.hour) + ":" + str(Time.minute) + ":" + str(Time.second)
    
    initTime = time.time()
    clientSocket.sendto(ping.encode(),(serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    except:
        print('Solicitação expirada')
    else:
        finTime = time.time()
        RTT = finTime - initTime
        print (modifiedMessage.decode() + " - RTT = " + str(RTT))
    ping = ""
