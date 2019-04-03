from skimage import io,filters,color,feature
import os
import numpy as np
from skimage import transform
from python_exec2 import *

imageNamesArr = os.listdir("./testimages")

def getOEFImage(imagepath,modelpath):
	#override the function with OEF functionality
	#greyImage = color.rgb2grey(image)
	greyImage=runOEF(modelpath,imagepath)
	return greyImage

def getSobelImage(image):
	greyImage = color.rgb2grey(image)
	sobeledImage = filters.sobel(greyImage)

	return sobeledImage

def getCannyEdgeImage(image):
	greyImage = color.rgb2grey(image)
	cannyedImage = feature.canny(greyImage)

	return cannyedImage

def displayImages(imagesArr):
	for image in imagesArr:
		io.imshow(image,cmap='gray')
		io.show()

def getCorrelationBetween2Images(img1,img2):

	corrVal = None

	a = np.copy(resizedOEF)
	b = np.copy(resizedSobel)

	aMean = np.mean(a)
	bMean = np.mean(b)

	abar = np.reshape(a,(1,-1))
	bbar = np.reshape(b,(1,-1))

	abarnorm = abar-aMean
	bbarnorm = bbar-bMean


	top = np.dot(abarnorm,bbarnorm.T)[0][0]
	bottom1 = np.sqrt(np.dot(abarnorm,abarnorm.T))[0][0]
	bottom2 = np.sqrt(np.dot(bbarnorm,bbarnorm.T))[0][0]
	if bottom1 != 0.0 and bottom2 != 0.0:
	#                         print(bottom1,bottom2)
	    corrVal = top/(bottom1*bottom2)
	    # print("correlation value:",corrVal)
	
	return corrVal

for imageName in imageNamesArr:
	model='./cache/forest/model.mat'
	dire='./testimages/'+imageName
	image = io.imread(dire)
	resImageOEF = getOEFImage(dire,model)
	sobelImage = getSobelImage(image)
	# cannyEdgedImage = getCannyEdgeImage(image)

	dispImagesArr = []
	dispImagesArr.append(resImageOEF)
	dispImagesArr.append(sobelImage)
	#dispImagesArr.append(cannyEdgedImage)

	# print(dispImagesArr)

	displayImages(dispImagesArr)

	# print(resImageOEF.shape)
	# print(sobelImage.shape)

	resizedOEF = transform.resize(resImageOEF, (64,64))#,anti_aliasing=True)
	resizedSobel = transform.resize(sobelImage, (64,64))#,anti_aliasing=True)

	# print(resizedOEF-resizedSobel)
	corrVal = getCorrelationBetween2Images(resizedOEF,resizedSobel)
	print("CORRELATION VAL:",corrVal)
	

