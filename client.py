import socket

localIP = ''
localPort = 20002
serverAddressPort = ('localhost', 20001)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.bind((localIP, localPort))
UDPClientSocket.settimeout(None)

while(True):
    msgFromClient = raw_input("Input something to send to server: ")
    print(msgFromClient)
    
    bytesToSend = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)

    if msgFromServer[0] == 'BASE':
        continue
    else:
        save = msgFromServer[0]
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        if msgFromServer[0] != save:
            msg = "Message from Server {}".format(msgFromServer[0])
            print(msg)
