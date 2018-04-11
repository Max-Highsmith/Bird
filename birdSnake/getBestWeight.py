#get best weights
#
#given a specific network cycle through all weight files available for that network,
#print training validation curve and save the best results to best weight folder
#

import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt
#
#ex networkStruct="yolo2"
#"./darknet detector map birdCfg/easyYolo2Bird.data birdNetwork/Yolo2/easy/easybs32res208dec5e3.cfg results/temp"
def getValidMap(dataFile, networkFile, weightFile):
	#"./darknet detector map birdCfg/easyYolo2Bird.data birdNetworks/Yolo2/easy/easybs32res208dec5e3.cfg backup/easy/ results/temp"
	MAX_ITERATIONS   = 6000
	START_ITERATIONS = 2000
	OBS_FREQ =2000
	weight_intervals = np.linspace(START_IT, MAX_IT, (MAX_IT - START_IT)/OBS_FREQ) 
	bestmAPVal    = 0
	bestmAPWeight = 0
	observedmAP = []
	for i in weight_intervals:
		"./darknet detector mAP "+dataFile+ " "+networkFile+" "+weightFile + " results/temp"
		x = open("results/temp.txt", "r")
		mAP = float(x.read())
		observedmAP.append(mAP)
		if mAP > bestmAPVal
			bestmAPVal    = mAP
			bestmAPWeight = i

		x.close()

	#plot mAP:
	#TODO
	return [bestmAPWeight, mAP]



for 
