#assempble easyTrain.txt, etc

import glob
import os

difficulties = ['easy', 'hard']
stageInAnalysis = ['train','val','test','test_total']
years = ['2014','2016']

for diff in difficulties:
	for stage in stageInAnalysis:
		fh = open("../birdData/"+diff+stage+'.txt','w')
		for year in years:
			pics = glob.glob("../birdData/"+diff+"/"+stage+"/"+year+"/*.jpg")
			for pic in pics:
				fh.write("birdData/"+diff+"/"+stage+"/"+year+"/"+os.path.basename(pic)+'\n')
		fh.close()	
			


