#Server part
import time
from multiprocessing import Process
import random
from time import gmtime, strftime
from random import randint
import socket
import select
import os
import subprocess as sp

# HOST = '172.31.32.39'
HOST = '127.0.0.1'
#HOST = '192.168.0.104'
PORT = 6668
portmsg = 5001

mySocket = socket.socket()
mySocket.bind((HOST, portmsg))

mySocket.listen(1)
conn, addr = mySocket.accept()
print("Connection from: " + str(addr))
data = conn.recv(1024).decode()
ts = time.time()
if data:
    data = str(data)
    print ("Received Timestamp" + str(data))
    print ("Server Timestamp" + str(ts))
else:
     pass       
conn.close()

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)



def receive():
    print("Receiving")
    imgcounter = 1
    basename = "image %s.jpg"
    while True:

        read_sockets, write_sockets, error_sockets = select.select(
            connected_clients_sockets, [], [])

        for sock in read_sockets:

            if sock == server_socket:

                sockfd, client_address = server_socket.accept()
                connected_clients_sockets.append(sockfd)

            else:
                try:

                    data = sock.recv(4096)
                    txt = str(data)

                    if data:

                        if data.startswith('SIZE'):
                            tmp = txt.split()
                            size = int(tmp[1])

                            print('Image Recieved')

                            sock.sendall("GOT SIZE")

                        else:
                            ts = time.time()
                            #myfile = open(basename % imgcounter, 'wb')  #with numbers
                            myfile = open(basename % ts, 'wb') #with timestamps
                            myfile.write(data)
                            while len(data):
                                data = sock.recv(40960000)
                                myfile.write(data)
                            myfile.close()
                            sock.sendall("GOT IMAGE")
                            sock.shutdown()
                except:
                    sock.close()
                    connected_clients_sockets.remove(sock)
                    continue
            imgcounter += 1
    server_socket.close()


def getMetadata():
        # Function to get location data from autopilot
        # Returns <datastructure> @karan decide
    pass


if __name__ == '__main__':
    """ p1 = Process(target=process)
    p1.start() """
    p2 = Process(target=receive)
    p2.start()
