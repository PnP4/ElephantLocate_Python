import socket
import sys
import json
import matplotlib.pyplot as plt
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 8091)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

plt.axis([0, 10, 0, 1])
plt.ion()

plt.ion() # set plot to animated

ydata = [0] * 50
ax1=plt.axes()

# make plot
line, = plt.plot(ydata)
plt.ylim([10,40])



while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    x=[]
    y=[]
    connection, client_address = sock.accept()
    try:
        print >> sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            try:
                data = connection.recv(1000000)
                if data:
                    dic=json.loads(data.decode('utf8'))[0]
                    for i in range(0,len(dic['x'])):
                        if(len(x)!=0):
                            x.pop(0)
                            y.pop(0)
                        x.append(dic['x'][i])
                        y.append(dic['y'][i])
                        line.set_xdata(x)
                        line.set_ydata(y)  # update the data
                        plt.draw()  # update the plot
                        #print >> sys.stderr, 'received "%"' % data
                        print x[len(x)-1]
                else:
                    break
            except Exception,e:
                print e

    finally:
        # Clean up the connection
        connection.close()