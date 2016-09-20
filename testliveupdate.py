import pylab as plt
import numpy as np
from random import randint

X = np.linspace(0,2,1000)
Y = np.linspace(-1.5,1.5,1000)

plt.ion()
graph = plt.plot(X,Y)[0]
N = 600
T = 1.0 / 800.0
x = np.linspace(0.0, N * T, N * 10)
y = np.sin(randint(0,9) * 2.0 * np.pi * x)
point=0
cun=10;
while point<len(x):
    x = np.linspace(0.0, N * T, N * 10)
    y = np.sin(randint(0, 9) * 2.0 * np.pi * x)
    Y = X**2 + np.random.random(X.shape)
    graph.set_xdata(x)
    graph.set_ydata(y)
    plt.draw()
    plt.pause(0.5)
    point=point+cun