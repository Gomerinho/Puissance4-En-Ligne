import socket


HEADER = 64
PORT = 40000
FORMAT = 'utf-8'
DECONNEXION = "!DECONNEXION"
SERVER = "192.168.1.2"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

