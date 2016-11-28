import __init__

while True:
    try:
        while True:
            __init__.channel.basic_consume(__init__.callback,
                                  queue='calculator',
                                  no_ack=True)

            __init__.channel.start_consuming()

    except Exception, e:
        print e

