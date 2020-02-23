#!/usr/bin/env python
import socket
localIP = ''    # I don't think you change this, but if it fails then set to 'localhost', '127.0.0.1',
				# or '192.168.105.x' as shown in ifconfig

localPort = 20001
bufferSize = 1024

# msgFromServer = 'test return'
# bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print('UDP server up and listening')

while(True):
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]

	print('Message from Client:{}'.format(message))
	print('Client IP Address:{}'.format(address))