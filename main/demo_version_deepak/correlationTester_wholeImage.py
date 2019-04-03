from skimage import io,filters,color,feature
import os
import numpy as np
from PIL import ImageTk, Image
from skimage import transform
from python_exec2_withEs import *

modelpath='./cache/forest/model.mat'
oefImageFileName="corrOEF.jpg"
imageDirPath = "./testimages/"

imageNamesArr = os.listdir(imageDirPath)

def getOEFImage(imagepath):
	global modelpath
	global oefImageFileName
	
	[E,Es]=runOEF(modelpath,imagepath)

	# oefImage = ImageTk.PhotoImage(image=Image.fromarray(E.astype('uint8')))
	io.imsave(oefImageFileName,E/255)
	returnImg = io.imread(oefImageFileName)
	return returnImg

def getSobelImage(image):
	greyImage = color.rgb2grey(image)
	sobeledImage = filters.sobel(greyImage)

	return sobeledImage

def getSobelImageFromImagePath(imagepath):
	image = io.imread(imagepath)
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

	a = np.copy(img1)
	b = np.copy(img2)

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

#print("starting iterations:")
cnt = 0
for imageName in imageNamesArr:
	
	"""
	if cnt == 2: 
		break
	else:
		cnt+=1
	"""
	#print(imageName," being evaluated:")
	
	imagePath=imageDirPath+imageName
	resImageOEF = getOEFImage(imagePath)
	sobelImage = getSobelImageFromImagePath(imagePath)
	# cannyEdgedImage = getCannyEdgeImage(image)

	dispImagesArr = []
	dispImagesArr.append(resImageOEF)
	dispImagesArr.append(sobelImage)
	#dispImagesArr.append(cannyEdgedImage)

	# print(dispImagesArr)

	#displayImages(dispImagesArr)

	# print(resImageOEF.shape)
	# print(sobelImage.shape)

	#resizedOEF = transform.resize(resImageOEF, (128,128))#,anti_aliasing=True)
	#resizedSobel = transform.resize(sobelImage, (128,128))#,anti_aliasing=True)

	# print(resizedOEF-resizedSobel)
	corrVal = getCorrelationBetween2Images(resImageOEF,sobelImage)
	print("CORRELATION VAL: for "+imageName+" :",corrVal)
	
