import json
#import pika
import __init__

try:
    while True:
        __init__.channel.basic_consume(__init__.callback,
                              queue='checkForElephant',
                              no_ack=True)

        __init__.channel.start_consuming()

except Exception,e:
    print e

