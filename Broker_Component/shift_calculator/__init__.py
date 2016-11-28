import pika
import json
import numpy as np
from scipy.signal import correlate

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='calculator')


def callback(ch, method, properties, body):
    recv_data = json.loads(body)
    y1 = recv_data["y_leftchannel"]
    y2 = recv_data["y_rightchannel"]
    x1 = recv_data["y_rightchannel"]
    N = recv_data["N"]
    b = recv_data["b"]
    time = np.arange(1 - N, N)  # time is centered at 0

    cross_correlation = correlate(y1, y2)
    shift_calculated = time[cross_correlation.argmax()] * 1.0 * b / N
    print len(y1)
    y3 = sum([np.sin(2 * np.pi * i * (x1 - shift_calculated) / b) for i in range(1, 5)])
    print "Calculated shift: ", shift_calculated
