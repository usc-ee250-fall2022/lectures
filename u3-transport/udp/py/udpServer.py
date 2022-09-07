# https://pythontic.com/modules/socket/udp-client-server-example
import socket
import os
import signal


# def create_handler(obj):
#     def _handler(signum, frame):
#         print(' received kill signal')
#         # example obj method
#         obj.close()
#         signal.signal(signum, signal.SIG_DFL)
#         os.kill(os.getpid(), signum)  # Rethrow signal without catching it

#     return _handler





localIP     = "127.0.0.1"
localPort   = 20001

bufferSize  = 1024
msgFromServer       = "Server acknowledges receipt"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.settimeout(10)
# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

# Alternatively SIGTSTP for ctrl+z
#signal.signal(signal.SIGINT, create_handler(UDPServerSocket))
 

print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "\tClient IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)