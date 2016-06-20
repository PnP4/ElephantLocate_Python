import matplotlib.pyplot as plt
import numpy as np
import random
import socket
import sys
import json
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8091)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)


N = 600
T = 1.0 / 800.0
x = np.linspace(0.0, N * T, N*10)
y = np.sin(20* 2.0 * np.pi * x)
currentpos=0;

def generatedata(noofele):
    global currentpos
    global x,y
    qt=[]
    q=[]
    q.append(5)
    q.append(5)
    skip=len(x)*0.001 #x parts for a milliseecond
    x_send=[]
    y_send=[]
    nextdata=currentpos
    for j in range(0,noofele):
        x_send.append(x[nextdata])
        y_send.append(y[nextdata])
        nextdata=nextdata+skip
        nextdata=int(nextdata)%len(x)
    q[0]=x_send
    q[1] = y_send
    currentpos=nextdata%len(x)
    qt.append(q)
    return qt

def senddata():
    try:

        # Send data
        message = 'This is the message.  It will be repeated.'
        print >>sys.stderr, 'sending "%s"' % message
        iqp=0
        while(True):
            #data = generatedata(5)
            #datas=str(json.dumps(data))
            #print datas
            #dic = json.loads(datas)
            #print dic
            datas=str(random.randint(0,100))
            sock.sendall(datas)

        # Look for the response
        #amount_received = 0
        #amount_expected = len(message)

        '''while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data'''

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()



senddata()
print len(x)
#plt.plot(data['x'], data['y'])
#plt.axis([0, 1, -.8, .8])
#plt.xlabel('time')
#plt.ylabel('amplitude')
#plt.show()