
import json
from scipy.fftpack import fft
import numpy as np
import requests
#from gen import app

#recv_data=json.loads('{"b": 10, "N": 75, "x_rightchannel": [0.0, 0.13513513513513514, 0.2702702702702703, 0.40540540540540543, 0.5405405405405406, 0.6756756756756757, 0.8108108108108109, 0.945945945945946, 1.0810810810810811, 1.2162162162162162, 1.3513513513513513, 1.4864864864864866, 1.6216216216216217, 1.7567567567567568, 1.891891891891892, 2.027027027027027, 2.1621621621621623, 2.2972972972972974, 2.4324324324324325, 2.5675675675675675, 2.7027027027027026, 2.837837837837838, 2.9729729729729732, 3.1081081081081083, 3.2432432432432434, 3.3783783783783785, 3.5135135135135136, 3.6486486486486487, 3.783783783783784, 3.9189189189189193, 4.054054054054054, 4.1891891891891895, 4.324324324324325, 4.45945945945946, 4.594594594594595, 4.72972972972973, 4.864864864864865, 5.0, 5.135135135135135, 5.27027027027027, 5.405405405405405, 5.540540540540541, 5.675675675675676, 5.810810810810811, 5.9459459459459465, 6.081081081081082, 6.216216216216217, 6.351351351351352, 6.486486486486487, 6.621621621621622, 6.756756756756757, 6.891891891891892, 7.027027027027027, 7.162162162162162, 7.297297297297297, 7.4324324324324325, 7.567567567567568, 7.7027027027027035, 7.837837837837839, 7.972972972972974, 8.108108108108109, 8.243243243243244, 8.378378378378379, 8.513513513513514, 8.64864864864865, 8.783783783783784, 8.91891891891892, 9.054054054054054, 9.18918918918919, 9.324324324324325, 9.45945945945946, 9.594594594594595, 9.72972972972973, 9.864864864864865, 10.0], "x_leftchannel": [0.0, 0.13513513513513514, 0.2702702702702703, 0.40540540540540543, 0.5405405405405406, 0.6756756756756757, 0.8108108108108109, 0.945945945945946, 1.0810810810810811, 1.2162162162162162, 1.3513513513513513, 1.4864864864864866, 1.6216216216216217, 1.7567567567567568, 1.891891891891892, 2.027027027027027, 2.1621621621621623, 2.2972972972972974, 2.4324324324324325, 2.5675675675675675, 2.7027027027027026, 2.837837837837838, 2.9729729729729732, 3.1081081081081083, 3.2432432432432434, 3.3783783783783785, 3.5135135135135136, 3.6486486486486487, 3.783783783783784, 3.9189189189189193, 4.054054054054054, 4.1891891891891895, 4.324324324324325, 4.45945945945946, 4.594594594594595, 4.72972972972973, 4.864864864864865, 5.0, 5.135135135135135, 5.27027027027027, 5.405405405405405, 5.540540540540541, 5.675675675675676, 5.810810810810811, 5.9459459459459465, 6.081081081081082, 6.216216216216217, 6.351351351351352, 6.486486486486487, 6.621621621621622, 6.756756756756757, 6.891891891891892, 7.027027027027027, 7.162162162162162, 7.297297297297297, 7.4324324324324325, 7.567567567567568, 7.7027027027027035, 7.837837837837839, 7.972972972972974, 8.108108108108109, 8.243243243243244, 8.378378378378379, 8.513513513513514, 8.64864864864865, 8.783783783783784, 8.91891891891892, 9.054054054054054, 9.18918918918919, 9.324324324324325, 9.45945945945946, 9.594594594594595, 9.72972972972973, 9.864864864864865, 10.0], "y_rightchannel": [-0.7265425280053608, -0.5523410276219356, -0.34303385824013266, -0.1310063401514143, 0.04819661324841913, 0.16010118821654423, 0.17561958456869486, 0.07494687141810086, -0.1494279112491711, -0.49097505724079393, -0.9288864232030327, -1.4294265045169223, -1.9487754836684499, -2.4370982214845625, -2.843430830496362, -3.1208773041744005, -3.231564306117743, -3.1508182223006655, -2.870103795510736, -2.3983903080071642, -1.7617757751082217, -1.00138407912457, -0.16973421692989976, 0.6740553987952486, 1.4697394066804548, 2.1615336731847123, 2.7032456504605844, 3.0624227089353098, 3.2230998976411334, 3.186878911397094, 2.9722484533946485, 2.6122430376846593, 2.150712084334215, 1.6376148569929874, 1.1238538663213742, 0.6561995685986647, 0.2728386674965759, 1.1102230246251565e-16, -0.15001481172225295, -0.17922937570448805, -0.10282878116799476, 0.05338454139883421, 0.25658565817105516, 0.4711344461656126, 0.6629000567842087, 0.8032072031439134, 0.8719651908234366, 0.8596458471211548, 0.7679179665908202, 0.6089068131222412, 0.4032087830859701, 0.176934847737652, -0.04183456138322805, -0.22673825050999563, -0.35651272786732646, -0.41765169039735794, -0.406030939232436, -0.32731293674229567, -0.196096040049749, -0.03392726168591874, 0.13356407321045305, 0.2800476044648551, 0.38196153895671625, 0.42163326440551563, 0.3896559631027964, 0.28621651928318126, 0.12119764264681876, -0.08697303561524494, -0.313599891963778, -0.5308549942139302, -0.7113958133726933, -0.8320228962370765, -0.876922402229811, -0.8400797963375436, -0.7265425280053612], "y_leftchannel": [0.0, 0.838924600924541, 1.6180555561731835, 2.283141011909617, 2.790444168718697, 3.1106407234948446, 3.2312489059011957, 3.157357921359337, 2.9106023426368894, 2.526516064910461, 2.050569465264072, 1.5333288737106534, 1.0252637899914483, 0.5717554334554086, 0.20882768182538136, -0.03996750371530555, -0.16521294842798617, -0.17170547446614148, -0.07699636490053519, 0.09139342679214452, 0.29972829039087645, 0.5123291655894776, 0.6958609786025225, 0.8231478762796522, 0.8760946422000299, 0.8474063344261915, 0.740944976507343, 0.5707247175165693, 0.3587062835500779, 0.1316893682535315, -0.08229787118877363, -0.2576610858645637, -0.37450475752835766, -0.4211063037679591, -0.3953071511842736, -0.30466402790221514, -0.16535662920327077, -2.449293598294707e-16, 0.16535662920327232, 0.30466402790221303, 0.39530715118427356, 0.42110630376795943, 0.3745047575283573, 0.2576610858645635, 0.08229787118877308, -0.1316893682535319, -0.3587062835500802, -0.5707247175165702, -0.7409449765073428, -0.8474063344261946, -0.8760946422000315, -0.8231478762796512, -0.6958609786025217, -0.5123291655894773, -0.2997282903908775, -0.09139342679214504, 0.07699636490053693, 0.17170547446614126, 0.16521294842798562, 0.039967503715304, -0.20882768182538136, -0.5717554334554097, -1.0252637899914485, -1.5333288737106519, -2.0505694652640707, -2.5265160649104614, -2.910602342636889, -3.157357921359337, -3.2312489059011957, -3.1106407234948437, -2.7904441687186994, -2.283141011909616, -1.6180555561731835, -0.8389246009245452, -2.449293598294706e-15]}')

def filter(data):

		url = "http://localhost:5004"
		recv_data = data
		N=recv_data["N"]
		y1=recv_data["y_leftchannel"]

		#print y1

		# Number of sample points
		#N = 600
		# sample spacing
		T = 1.0 / N
		#x = np.linspace(0.0, N*T, N)
		#y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
		y=y1
		yf = fft(y)
		xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
		#import matplotlib.pyplot as plt
		#plt.plot(xf[:100], 2.0/N * np.abs(yf[0:N/2])[:100])

		#plt.grid()
		#plt.show()
		#r = requests.post(sen_url, data=json.dumps(recv_data))
		print (json.dumps(recv_data))
		requests.post(url, json=recv_data)
