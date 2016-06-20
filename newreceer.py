import json
import serial
import numpy as np
from matplotlib import pyplot as plt
import socket               # Import socket module
#ser = serial.Serial('/dev/ttyACM0', 9600)

plt.ion() # set plot to animated

ydata = [0] * 50
ax1=plt.axes()

# make plot
line, = plt.plot(ydata)
plt.ylim([10,40])



s = socket.socket()         # Create a socket object
host = '' # Get local machine name
port = 8091                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()
   # start data collection
   while True:
       data = c.recv(1024*1024)
       print data
       '''ymin = float(min(ydata)) - 10
       ymax = float(max(ydata)) + 10
       plt.ylim([ymin, ymax])
       ydata.append(data)
       del ydata[0]
       line.set_xdata(np.arange(len(ydata)))
       line.set_ydata(ydata)  # update the data
       plt.draw()  # update the plot
        '''

