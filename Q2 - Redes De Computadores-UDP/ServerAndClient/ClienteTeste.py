
import socket

HOST = ''
PORT = 5030

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
arq = open(os.getcwd() + 'index.html', 'w')

while 1:
    dados = conn.recv(1024)
    if not dados:
        break
    print(dados)

arq.close()
conn.close()

