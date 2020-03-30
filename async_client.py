# Client Part
import random
import socket, select
from time import gmtime, strftime
from random import randint
import os
from multiprocessing import Process
import time
import subprocess as sp
import json

cwd = os.getcwd()

HOST = '127.0.0.1'
#HOST = '192.168.0.104'
#HOST = '13.126.54.101'
# HOST = 'ec2-13-126-54-101.ap-south-1.compute.amazonaws.com'

print ("Sending to ") + HOST


portmsg = 5001
        
mySocket = socket.socket()
mySocket.connect((HOST,portmsg))
ts = time.time()
message = str(ts)
        
if message != 'q':
        mySocket.send(message.encode())
"""         data = mySocket.recv(1024).decode()
                
        print ('Server: ' + data)
                
        message = raw_input("Client -> ") """
                
# mySocket.close()

PORT = 6668
PORTX = 6969
coordLat = [42.546245,23.424076,33.93911,17.060816,18.220554,41.153332,40.069099,12.226079,-11.202692,-75.250973,-38.416097,-14.270972,47.516231,-25.274398,12.52111,40.143105,43.915886,13.193887,23.684994,50.503887]
coordLong = [1.601554,53.847818,67.709953,-61.796428,-63.068615,20.168331,45.038189,-69.060087,17.873887,-0.071389,-63.616672,-170.132217,14.550072,133.775136,-69.968338,47.576927,17.679076,-59.543198,90.356331,4.469936]

finalList = []

def capture():
    # add cam_test function
    temp = 0
    while temp<len(coordLat):
        ts = time.time()
        """ print str(coordLat[temp])+"   "+str(ts)
        print str(coordLong[temp])+"   "+str(ts) """
        coordStamp = (str(coordLat[temp]),str(coordLong[temp]),str(ts))
        finalList.append(coordStamp)
        print coordStamp
        temp = temp + 1
        time.sleep(0.5)
    jsonDump = json.dumps(finalList)
    print jsonDump
    time.sleep(0.5)
    with open("Coords.json",'w') as file:
        file.write(jsonDump)

    """ print("Transmitting")
    time.sleep(0.1)
    print ("this") """
    pass

def coordinates():
    # Simulating GPS sensor of UAV
    # When sensor is available, similar function will get coordinates and send them to the server
    while True:
        print "here"
        time.sleep(0.5)
    pass

def transmit():
    while True:
        for filename in os.listdir(cwd):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".JPG") or filename.endswith(".jpeg") or filename.endswith(".tiff") or filename.endswith(".bmp"):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server_address = (HOST, PORT)
                    sock.connect(server_address)

                    # open image
                    myfile = open(filename, 'rb')
                    bytes = myfile.read(4096)
                    size = len(bytes)

                    # send image size to server
                    sock.sendall("SIZE %s" % size)
                    answer = sock.recv(4096)

                    #print ('answer = %s' % answer)

                    # send image to server
                    if answer == 'GOT SIZE':
                        while bytes:
                            sock.sendall(bytes)
                            bytes = myfile.read(40960000)

                        # check what server send
                        # answer = sock.recv(4096)
                        print ('answer = %s' % answer)

                        if answer == 'GOT IMAGE' :
                            print ('Image successfully sent to server')

                    myfile.close()
                    sp.call(["rm", filename])
                finally:
                    sock.close()
            elif filename.endswith(".json"):
                print "Entered json check"
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server_address = (HOST, PORTX)
                    sock.connect(server_address)

                    # open image
                    myfile = open(filename, 'rb')
                    bytes = myfile.read(4096)
                    size = len(bytes)

                    # send image size to server
                    sock.sendall("SIZE %s" % size)
                    answer = sock.recv(4096)

                    #print ('answer = %s' % answer)

                    # send image to server
                    if answer == 'GOT SIZE':
                        while bytes:
                            sock.sendall(bytes)
                            bytes = myfile.read(40960000)

                        # check what server send
                        # answer = sock.recv(4096)
                        print ('answer = %s' % answer)

                        if answer == 'GOT IMAGE' :
                            print ('File successfully sent to server')

                    myfile.close()
                    sp.call(["rm", filename])
                finally:
                    sock.close()
            else:
                time.sleep(2)
                continue
        time.sleep(5)

def getMetadata():
    # Function to get location data from autopilot
    # Returns <datastructure> @karan decide
    pass

if __name__ == '__main__':
    p1 = Process(target = capture)
    #p1 = Process(target = coordinates)
    #p1.start()
    p2 = Process(target = transmit)
    p2.start()