import subprocess as sp
import os
import glob

os.chdir("..")


NNET_CONFIGS = "birdNetworks/Yolo2/"

TRAIN = "./darknet detector train "
TRANS = "darknet53.conv.74"


difConfigs   = ['birdCfg/easyYolo2Bird.data', 'birdCfg/hardYolo2Bird.data']
difficulties = ['easy', 'hard']
for i, diff in enumerate(difficulties):
	networks = glob.glob(NNET_CONFIGS+diff+"/*")
	for net in networks:
		FULL_C = TRAIN + difConfigs[i] +" "+ net +" "+ TRANS
		print(FULL_C)
		sp.call(FULL_C, shell=True)
	



