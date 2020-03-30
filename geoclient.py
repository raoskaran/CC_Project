# Import socket module
import socket
import pickle, time, json
from pprint import pprint
# Create a socket object
s = socket.socket()
coords = {}
key = 1
# Define the port on which you want to connect
port = 12348
HOST = '127.0.0.1'
# connect to the server on local computer
s.connect((HOST, port))
print "Receiving"
# receive data from the server
while True:
    data = s.recv(1024)
    if data:
        coords[key] = data+" "+str(time.time())
        key+=1
    else:
        pprint(coords)
        break
# close the connection
with open('coords.json', 'w') as f:
    json.dump(coords, f)
s.close()