import numpy as np
import json
from random import randint
import requests
from flask import jsonify
#from gen import app

def gen():
	a,b, N = 0, 10, 75
	shift = -3

	x = np.linspace(a,b,N)
	x1 = 1*x + shift

	url = "http://localhost:5003"

	y1 = sum([np.sin(2*np.pi*i*x/b) for i in range(1,5)]) #left channel
	y2 = sum([np.sin(2*np.pi*i*x1/b) for i in range(1,5)]) #right channel

	y3 = sum([np.sin(2*np.pi*i*5*x/b) for i in range(1,5)]) #left channel
	y4 = sum([np.sin(2*np.pi*i*11*x1/b) for i in range(1,5)]) #right channel

	y5 = sum([np.sin(2*np.pi*i*24*x/b) for i in range(1,5)]) #left channel
	y6 = sum([np.sin(2*np.pi*i*36*x1/b) for i in range(1,5)]) #right channel

	try:
		while True:
			rndint=randint(0,3)

			datasend={}

			if(rndint==0):
				datasend["y_leftchannel"]=y1.tolist()
				datasend["y_rightchannel"] = y2.tolist()
			elif (rndint==1):
				datasend["y_leftchannel"] = y3.tolist()
				datasend["y_rightchannel"] = y4.tolist()
			elif (rndint == 2):
				datasend["y_leftchannel"] = y5.tolist()
				datasend["y_rightchannel"] = y6.tolist()


			datasend["x_leftchannel"]=x.tolist()
			datasend["x_rightchannel"]=x.tolist()
			datasend["N"]=N
			datasend["b"]=b

			datasend= datasend

			r = requests.post(url, json= datasend)
			print r
			#print json.dumps(datasend)

	except Exception :
		print Exception.message



