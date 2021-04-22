#!/usr/bin/python3
import socket


HEADER = 64
PORT = 40001
FORMAT = 'utf-8'
DECONNEXION = "!DECONNEXION"
SERVER = "vps-aef73ebf.vps.ovh.net"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def envoyer(msg):
    message = msg.encode(FORMAT)
    message_longueur = str(len(message)).encode(FORMAT)
    message_longueur += b' '*(HEADER-len(message_longueur))

    client.send(message_longueur)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def communication():
    while (True):
        envoyer(input())

communication()