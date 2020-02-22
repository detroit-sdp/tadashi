import socket

msgFromClient = raw_input("Input something to send to server: ")
print(msgFromClient)
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("localhost", 20001)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# msgFromServer = UDPClientSocket.recvfrom(bufferSize)
# msg = "Message from Server {}".format(msgFromServer[0])
# print(msg)