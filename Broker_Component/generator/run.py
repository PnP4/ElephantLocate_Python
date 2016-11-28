import __init__
import json


while True:
    try:
        while True:
            data = __init__.genaretor()
            print data

            __init__.channel.basic_publish(exchange='',
                        routing_key='frequencyfilter',
                        body=json.dumps(data))
            #print json.dumps(datasend)
    except Exception, e:
        print e

