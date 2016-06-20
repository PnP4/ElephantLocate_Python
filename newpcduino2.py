#!/usr/bin/env python
import json
import time, os
import socket
import sys


## For simplicity's sake, we'll create a strings and filenames for our paths
ADC_PATH= os.path.normpath('/proc/')
ADC_FILENAME = "adc"
PWM_PATH= os.path.normpath('/sys/class/leds/')
PWM_DIR = "pwm"
PWM_FILENAME = "brightness"
PWM_MAX = "max_brightness"

## create empty arrays to store the pointers for our files
adcFiles = []
pwmFiles = []
pwmMaxFiles = []

adcFiles.append(os.path.join(ADC_PATH, ADC_FILENAME+str(3)))
def coldata(amnt):
	data=[]
	while(amnt>0):
		file= adcFiles[0]
		fd = open(file, 'r')
		fd.seek(0)
		#print "ADC Channel: " + str(adcFiles.index(file)) + " Result: " + fd.read(16)
		data.append(fd.read(16).split(":")[1])
		fd.close()
		amnt=amnt-1
	return data

print coldata(10)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.2', 8091)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
while (1):
	try:
		senddata=coldata(10)
		datas = str(json.dumps(senddata))
		sock.sendall(senddata)
	finally:
		print >> sys.stderr, 'closing socket'
		sock.close()