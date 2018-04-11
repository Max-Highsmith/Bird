# hyper parameter grid search of yolo2 network

import csv
import numpy as np
import subprocess as sp
import os
import copy
import sys

os.chdir("..")


#FILESTRUCTURE CONFIGS
NET_FOLD = sys.argv[1]
BASE_NET = sys.argv[2]

difficulties =['easy', 'hard']

#Hyper Parameters
batchSizes = [32,64]
resolutions = [208, 416, 832]
decays      = [0.005, 0.0005, 0.00005]
decLab      = ['5e3','5e4','5e5']


otherCFGs = np.empty([len(difficulties), len(batchSizes), len(resolutions), len(decays)], dtype=object)
dummyCFGs  = copy.deepcopy(otherCFGs)

#create the file writers:
for l, diff in enumerate(difficulties):
	for i, bs in enumerate(batchSizes):
		for j, res in enumerate(resolutions):
			for k, dec in enumerate(decays):
				fileName = NET_FOLD+difficulties[l]+"/"+diff+"bs"+str(bs)+"res"+str(res)+"dec"+decLab[k]+".cfg"
				print(fileName)
				dummyCFGs[l,i,j,k] = open(NET_FOLD+difficulties[l]+"/"+diff+"bs"+str(bs)+"res"+str(res)+"dec"+decLab[k]+".cfg", 'w')
				otherCFGs[l,i,j,k] = csv.writer(dummyCFGs[l,i,j,k], delimiter=' ', lineterminator='\n')				


originalCFG = open(NET_FOLD+BASE_NET,'r')
reader = csv.reader(originalCFG, delimiter=' ')
for row in reader:
	for l, diff in enumerate(difficulties):
		for i, sz in enumerate(batchSizes):
			for j, res in enumerate(resolutions):
				for k, dec in enumerate(decays):
					##changes according to value
					if row:
						if "decay" in row[0]:
							otherCFGs[l,i,j,k].writerow(['decay='+str('{0:f}'.format(decays[k])).rstrip('0')])
						elif "width" in row[0]:
							otherCFGs[l,i,j,k].writerow(['width='+str(resolutions[j])])
						elif "height" in row[0]:
							otherCFGs[l,i,j,k].writerow(['height='+str(resolutions[j])])
						elif "batch=64" in row[0]:
							otherCFGs[l,i,j,k].writerow(['batch='+str(batchSizes[i])])
						else:
							otherCFGs[l,i,j,k].writerow(row)
					else:
						otherCFGs[l,i,j,k].writerow([])




