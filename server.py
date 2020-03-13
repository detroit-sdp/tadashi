#!/usr/bin/env python
import socket
from const import *

localIP = ''
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
UDPServerSocket.settimeout(None)

while(True):
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	command = bytesAddressPair[0]
	address = bytesAddressPair[1]

	command = commands[0]
	args = commands[1:]
	sendaddress = None

	if command.upper() == 'STATUS':
		sendaddress = ('192.168.105.111', 20002)
	elif command.upper() == 'GOTO':
		sendaddress = ('192.168.105.95', 20001)

	print('Message from Client:{}'.format(message))
	print('Client IP Address:{}'.format(address))

	UDPServerSocket.sendto(str.encode(message), sendaddress)