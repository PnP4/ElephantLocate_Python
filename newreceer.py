import json
import serial
import numpy as np
from matplotlib import pyplot as plt
import socket               # Import socket module
#ser = serial.Serial('/dev/ttyACM0', 9600)
from random import randint

X = np.linspace(0,2,1000)
Y = np.linspace(-5,5,1000)

plt.ion()
graph = plt.plot(X,Y)[0]
N = 600
T = 1.0 / 800.0
x = np.linspace(0.0, N * T, N * 10)
y = np.sin(randint(0,9) * 2.0 * np.pi * x)


s = socket.socket()         # Create a socket object
host = '' # Get local machine name
port = 8091                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()
   while True:
       data = c.recv(1024 * 1024*1024)
       print data
       x = np.linspace(0.0, N * T, N * 10)
       y = np.sin(randint(0, 9) * 2.0 * np.pi * x)
       #Y = X ** 2 + np.random.random(X.shape)
       graph.set_xdata(x)
       graph.set_ydata(y)
       plt.draw()
       plt.pause(0.5)
       point = point + cun
       '''ymin = float(min(ydata)) - 10
       ymax = float(max(ydata)) + 10
       plt.ylim([ymin, ymax])
       ydata.append(data)
       del ydata[0]
       line.set_xdata(np.arange(len(ydata)))
       line.set_ydata(ydata)  # update the data
       plt.draw()  # update the plot
        '''

