import subprocess as sp
import os
import glob

os.chdir("..")


TRAIN = "./darknet detector train "
TRANS = "darknet53.conv.74"

difConfigs   = ['birdCfg/easyBird.data', 'birdCfg/hardBird.data']
difficulties = ['easy', 'hard']
for i, diff in enumerate(difficulties):
	networks = glob.glob("birdNetworks/tinyYolo/"+diff+"/*")
	for net in networks:
		FULL_C = TRAIN + difConfigs[i] +" "+ net +" "+ TRANS
		print(FULL_C)
		sp.call(FULL_C, shell=True)
	



