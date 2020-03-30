# first of all import the socket library
import socket
import pickle
import time, json
# next create a socket object
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12348

# Next bind to the port
s.bind(('', port))
print "socket binded to %s" % (port)

coordLat = [42.546245, 23.424076, 33.93911, 17.060816, 18.220554, 41.153332, 40.069099, 12.226079, -11.202692, -
            75.250973, -38.416097, -14.270972, 47.516231, -25.274398, 12.52111, 40.143105, 43.915886, 13.193887, 23.684994, 50.503887]
coordLong = [1.601554, 53.847818, 67.709953, -61.796428, -63.068615, 20.168331, 45.038189, -69.060087, 17.873887, -
             0.071389, -63.616672, -170.132217, 14.550072, 133.775136, -69.968338, 47.576927, 17.679076, -59.543198, 90.356331, 4.469936]

# put the socket into listening mode
s.listen(5)
print "Server is listening"

# a forever loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    c, addr = s.accept()
    print 'Got connection from', addr
    print 'Sending coords'
    while True:
        for (x, y) in zip(coordLat, coordLong):
            data = str(x)+" "+str(y)
        #    print(data)
            c.send(data)
            time.sleep(1)
        break
    c.close()