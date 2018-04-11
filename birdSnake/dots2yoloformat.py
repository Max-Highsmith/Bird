##AUTHOR MAX HIGHSMITH
###NOTE  this script was written and run on external hard drive the parameters
##  DOT_FILES, NORMAL_FILE, JUST_DOTS, YOLO_LOADABLE will have to be adjusted to point to correct folders
##  This script pulls 512x512 data and assembles labels that are in yolo readable format
###
import os
from PIL import Image
import cv2
import numpy as np
import glob
import skimage
from skimage import feature

#given list of points and file name write textfile indicating points
BOX_SIZE=0.04
PIC_SIZE=512

DOT_FILES   = "/media/sisyphus/Icarus/Bird Data/DataOfIllions/PaperData/crop512_dot/"
NORMAL_FILE = "/media/sisyphus/Icarus/Bird Data/DataOfIllions/PaperData/crop512_upload/"
JUST_DOTS   = "/media/sisyphus/Icarus/Bird Data/DataOfIllions/PaperData/JustDots/"
YOLO_LOADABLE= "../birdData/"

difficulties = ['easy', 'hard']
dotDifficulties = ['easy_dot', 'hard_dot']
stageInAnalysis = ['train','val','test','test_total']
dotStageInAnalysis = ['train_dot', 'val_dot', 'test_dot', 'test_dot_total']
year = ['2014','2016']


#dot Img,  as PIL IMAGE
#raw img,  as PIL IMAGE
#imageName filename
#creates the justdotfile for a single image given its dotlabeled and unlabeled components
def createJustDots(dotImg, rawImg, imageName, justDotDirectory, dot_count):
	dotAr = np.asarray(dotImg);
	rawAr = np.asarray(rawImg);
	rawArB= cv2.GaussianBlur(rawAr, (5,5),0)
	img3  = cv2.absdiff(rawArB, dotAr)
	mask_1 = cv2.cvtColor(rawArB, cv2.COLOR_BGR2GRAY)
	mask_1[mask_1<50]=0;
	mask_1[mask_1>0]=255;
	img_4 = cv2.bitwise_or(img3, img3, mask=mask_1)
	jdAr  = np.max(img_4, axis=2)
	just_dot = Image.fromarray(jdAr);
	dot_count = dot_count+1;
	just_dot.save(justDotDirectory+"/"+imageName, "JPEG");


## current path to dot images including stage, diff, year
## current path to raw images including stage, diff, year
def createJustDotsDirectory(dotDif, dif, dotStage, stage, year):
#	currentDots = DOT_FILES+dotDifficulties[0]+"/"+dotStageInAnalysis[2]+"/"+year[0]
#	currentNorm = NORMAL_FILE+difficulties[0]+"/"+stageInAnalysis[2]+"/"+year[0]
	currentDots = DOT_FILES+dotDif+"/"+dotStage+"/"+year
	currentNorm = NORMAL_FILE+dif+"/"+stage+"/"+year
	print(currentDots)
	dotFiles = sorted(glob.glob(currentDots+"/*"))
	normFiles = sorted(glob.glob(currentNorm+"/*"))	
	print(dotFiles)
	for i in range(0, len(dotFiles)):
		dotImg = Image.open(dotFiles[i])
		rawImg = Image.open(normFiles[i])
		imageName = os.path.basename(dotFiles[i])
		#justDotDirectory = "../PaperData/JustDots/"+dif+"/"+stage+"/"+year
		justDotDirectory = JUST_DOTS+dif+"/"+stage+"/"+year
		dot_count =0
		createJustDots(dotImg, rawImg, imageName, justDotDirectory, dot_count)



def writeLabelFile(points, fileName, diff, stage, year):
    #fileCode = open("../PaperData/YoloLoadable/"+diff+"/"+stage+"/"+year+"/"+fileName.split(".")[0]+".txt","w")
    fileCode = open(YOLO_LOADABLE+diff+"/"+stage+"/"+year+"/"+fileName.split(".")[0]+".txt","w")
   #fileCode = open(SPL_LAB_DIR+"birdImg-"+str(indx)+".txt", "w")
    for i, point in enumerate(points):
        print(point[1]/PIC_SIZE);
        fileCode.write("0 ");
        fileCode.write(str(point[1]/PIC_SIZE)+" ");
        fileCode.write(str(point[0]/PIC_SIZE)+" ");
        fileCode.write(str(BOX_SIZE)+" ");
        fileCode.write(str(BOX_SIZE)+"\n");
    fileCode.close();

def getLabelsFromADotFile(dotFile, fileName, diff, stage, year):
#cycle through dots
    dotImg = cv2.imread(dotFile,0);
    blobs  = feature.blob_log(dotImg, min_sigma=3, max_sigma=10, num_sigma=1, threshold=0.05)
 #   detector = cv2.SimpleBlobDetector_create()
  #  keypoints = detector.detect(dotImg)
    writeLabelFile(blobs, fileName, diff, stage, year);

def getLabelsFromDirectOfDotFiles(diff, stage, year):
   # dotFiles = glob.glob("../PaperData/JustDots/"+diff+"/"+stage+"/"+year+"/*.jpg");
    dotFiles = glob.glob(JUST_DOTS+diff+"/"+stage+"/"+year+"/*.jpg");
    for dotFile in dotFiles:
        print(dotFile);
        baseName = os.path.basename(dotFile)
   #     indx    = int(dotFile.split('dot_')[1].split('.')[0]);
        getLabelsFromADotFile(dotFile, baseName, diff, stage, year);


def copyRawImagesToYOLO(diff, stage, year):
	pics = glob.glob(NORMAL_FILE+diff+"/"+stage+"/"+year+"/*.jpg")
	for pic in pics:
		impic = Image.open(pic)
		impic.save(YOLO_LOADABLE+diff+"/"+stage+"/"+year+"/"+os.path.basename(pic))

#copyRawImagesToYOLO(difficulties[0], stageInAnalysis[2], year[0])

for i, diff in enumerate(difficulties):
	for j, stage in enumerate(stageInAnalysis):
		for k, ye in enumerate(year):
			print("nutin")
		#create just dot imagesOA
			createJustDotsDirectory(dotDifficulties[i], difficulties[i], dotStageInAnalysis[j], stageInAnalysis[j], year[k])
		#copy raw images to yolo usable folder
			copyRawImagesToYOLO(difficulties[i], stageInAnalysis[j], year[k])
		#copy labels to yolo usable folder
			getLabelsFromDirectOfDotFiles(difficulties[i], stageInAnalysis[j], year[k])

