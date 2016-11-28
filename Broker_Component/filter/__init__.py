import pika
import json
from scipy.fftpack import fft
import numpy as np

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='frequencyfilter')
channel.queue_declare(queue='checkForElephant')


def callback(ch, method, properties, body):
    data = json.loads(body)
    N = data["N"]
    y1 = data["y_leftchannel"]
    print data
    # print y1
    # Number of sample points
    # N = 600
    # sample spacing
    T = 1.0 / N
    # x = np.linspace(0.0, N*T, N)
    # y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
    y = y1
    yf = fft(y)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)
    # import matplotlib.pyplot as plt
    # plt.plot(xf[:100], 2.0/N * np.abs(yf[0:N/2])[:100])

    # plt.grid()
    # plt.show()
    print "sending"
    channel.basic_publish(exchange='',
                          routing_key='checkForElephant',
                          body=json.dumps(data))