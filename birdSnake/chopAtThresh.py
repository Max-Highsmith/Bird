#given a file of results as in in comp4_det_test_bird.txt
#rewrtie file removing all entries with less than 0.5 probability

import csv

'''
NAME_OF_NET="easy64batchThresh.txt"
THRESH = 0.5
newResults = open("../birdResults/"+NAME_OF_NET, 'w');
writer = csv.writer(newResults, delimiter=' ')
with open("../results/comp4_det_test_bird.txt") as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
		if float(row[1]) > THRESH:
			writer.writerow(row)

'''

def ChopAtThresh(threshold, fileName):
	newResults = open("birdResults/"+"Thrsh"+str(int(100*threshold))+fileName+".txt", 'w')
	writer = csv.writer(newResults, delimiter=' ')
	with open("results/"+fileName+"bird.txt") as csvfile:
		reader = csv.reader(csvfile, delimiter=' ')
		for row in reader:
			if float(row[1]) > threshold:
				writer.writerow(row)
