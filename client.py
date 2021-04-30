#!/usr/bin/python3
import socket
import sys
import threading
import pickle

from datetime import datetime

import username

HEADER = 64
PORT = 40001
FORMAT = 'utf-8'
DECONNEXION = "!FIN"
SERVER = "vps-aef73ebf.vps.ovh.net"
ADDR = (SERVER, PORT)



def envoyer(msg, client):
    
    message = msg.encode(FORMAT)
    message_longueur = str(len(message)).encode(FORMAT)
    message_longueur += b' '*(HEADER-len(message_longueur))

    client.send(message_longueur)
    client.send(message)
    
def reception_async(conn):
    while True:
        try:
            contenu = recevoir(conn)
            if(contenu is not None):
                print(contenu)
        except:
            print("Erreur fatale lors de la réception. Cause probable : défaillance du serveur. Fin du programme.")
            break
            

def recevoir(conn):
    longueur_message = conn.recv(HEADER).decode(FORMAT)
    if(longueur_message):
        longueur_message = int (longueur_message)
        message = conn.recv(longueur_message)
        try:
            message = message.decode(FORMAT)
        except:
            message = pickle.loads(message)
        return message


def partie(conn):
    while True:
        envoyer(input(), conn)

def rejoindre():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Bienvenue dans le jeu du puissance 4!")
    print("Nom d'utilisateur :")
    #pseudo = username.form_pseudo()
    pseudo = input()

    conn.connect(ADDR)
    ecoute = threading.Thread(target=reception_async, args=(conn,))
    ecoute.start()
    envoyer(pseudo, conn)

    partie(conn)


if(__name__ == "__main__"):
    rejoindre()