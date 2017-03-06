#!/usr/bin/env python
from socket import *
import time

HOST = 'localhost'
PORT = 1111
BUFIZ = 1024
ADDR = (HOST,PORT)

def recvfile(filename):
    print 'starting receive file...'
    f = open(filename,'wb')
    cliSockfd.send('no problem')
    while True:
        data = cliSockfd.recv(4096)
        if data == 'EOF':
            print 'recved file success!'
            break
        f.write(data)
    f.close()

def sendfile(filename):
    print 'starting send file...'
    cliSockfd.send('no problem')
    f = open(filename,'rb')
    while True:
        data = f.read(4096)
        if not data:
            break
        cliSockfd.send(data)
    f.close()
    time.sleep(1)
    cliSockfd.send('EOF')
    print 'send file success!'

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.bind(ADDR)
sockfd.listen(5)
while True:
    print('waiting for connection...')
    cliSockfd,addr = sockfd.accept()
    print('...connected from:',addr)
    
    while True:
        msg = cliSockfd.recv(4096)
        act,filename = msg.split()
        if act == 'put':
            print 'recving msg!'
            recvfile(filename)
        elif act == 'get':
            print 'sending msg!'
            sendfile(filename)
        else:
            print 'error!'
            continue
