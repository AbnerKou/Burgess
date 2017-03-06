#!/usr/bin/env python
import sys
import socket
import time
HOST = 'localhost'
PORT = 1111
BUFSIZ = 1024
ADDR = (HOST,PORT)

cliSockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def recvfile(filename):
    f = open(filename,'wb')
    while True:
        msg = cliSockfd.recv(4096)
        if msg == 'EOF':
            print 'recv file success!'
            break
        f.write(msg)
    f.close
def sendfile(filename):
    f = open(filename,'rb')
    while True:
        msg = f.read(4096)
        if not msg:
             break
        cliSockfd.sendall(msg)
    f.close()
    time.sleep(1)
    cliSockfd.sendall('EOF')
    print 'send file success'
def confirm(cliSockfd,client_command):
    cliSockfd.send(client_command)
    msg = cliSockfd.recv(4096)
    if msg == 'no problem':
        return True
try:
    cliSockfd.connect(ADDR)
    while True:
        client_command = raw_input('>>>')
        if not client_command:
            continue
        act,filename = client_command.split()
        print act
        if act == 'put':
            if confirm(cliSockfd,client_command):
                sendfile(filename)
            else:
                print 'server error1!'
        elif act == 'get':
            if confirm(cliSockfd,client_command):
                recvfile(filename)
            else:
                print 'server error2!'
        else:
            print 'command error!'
except socket.error,e:
    print 'error:',e
finally:
    cliSockfd.close()

