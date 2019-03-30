
# coding: utf-8

# In[11]:


import matlab.engine as me
import matlab
import time
import numpy as np


# In[12]:


def getPatch():
#     a= np.array([
#     [1,1,1,0,0,0,0,0,1,0,1,0,1,1,1,1],
#     [1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0],
#     [1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0],
#     [1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0],
#     [1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
#     [1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
#     [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0], 
#    ])

#     a= np.array([
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
#    ])

    a= np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
       ])

#     a= np.array([
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
#            ])
    
    return a


# In[13]:


def getMinimumDistanceToLists(locOfOnes,orig):
    minDistDict = {}
    for i in range(len(locOfOnes)):
        dists = []
        tempList = locOfOnes[i]
        for j in range(len(tempList)):
            dist = np.sqrt(np.sum((orig-tempList[j])**2))
            dists.append(dist)
            
#             print("distances",orig,tempList[j],dist)
            
        minDist = np.min(dists)
        
        minDistDict[i]=minDist
        
    
    return minDistDict
    


# In[14]:


def getNearestPixelToOrig(nearestEdgeList,orig):
    dists = []
    for i in range(len(nearestEdgeList)):
        dist = np.sqrt(np.sum((orig-nearestEdgeList[i])**2))
        dists.append(dist)
        
    nearestPixel = nearestEdgeList[np.argmin(dists),:]
    return nearestPixel


# In[15]:


#initiate the matlab engine
mEng = me.start_matlab()

#get the image patch from anywhere
# patch = getPatch()
# patchSize = patch.shape[0]


def getUpdatedDandTheta(patch):
    data = patch.tolist()
    imageMat = matlab.uint8(data)
    imageMat.reshape((patch.shape[0],patch.shape[1]))
    [locOfOnes,edgeMat,edgeType] = mEng.edgelink(imageMat,nargout=3)
    
#     print(x)
#     print(y)
#     print(z)
    
    edgeMat = np.array(edgeMat,dtype=int)
    edgeMat = edgeMat > 0
    edgeMat = edgeMat.astype(int)
    
    tempx = []
    for i in range(len(locOfOnes)):
        tempx.append(np.array(locOfOnes[i])-1)
        tempx[i] = tempx[i].astype(int)
    
    locOfOnes = tempx
#     print(locOfOnes)
#     print(edgeMat)
#     print(edgeType)
    
    xc,yc = np.int(np.floor(patch.shape[0]/2)),np.int(np.floor(patch.shape[1]/2))
    orig = np.array([xc,yc])
    
#     print(orig)
    
    #find the distance from orig to all pixel location in the
    #locOfOnes list
    
    minDistDict = getMinimumDistanceToLists(locOfOnes,orig)
    
#     print(minDistDict)
    
    minListIndex = list(minDistDict.keys())[np.argmin(list(minDistDict.values()))]
    
    nearestEdgeList = locOfOnes[minListIndex]
    
    nearestPixel = getNearestPixelToOrig(nearestEdgeList,orig)
    
#     print(nearestEdgeList)
#     print(nearestPixel)
    
    d = np.sqrt(np.sum((orig-nearestPixel)**2))
    
    nears = np.array(np.where((nearestEdgeList == (nearestPixel[0], nearestPixel[1])).all(axis=1)))
    nearIdx = nears[0][0]
    
    lowIdx = 0
    if(nearIdx - 6 < 0):
        lowIdx = 0
    else:
        lowIdx = nearIdx - 6
        
    highIdx = nearIdx + 6
    
    pixelsToFit = nearestEdgeList[lowIdx:highIdx,:]
#     print(pixelsToFit)
    
    
    #call polyfit to the nearestEdgeList
    z = np.polyfit(pixelsToFit[:,0],pixelsToFit[:,1],1)
    theta = np.rad2deg(np.arctan(1/z[0]))
    
    return d,theta
    
    
    
    


# In[49]:


# getUpdatedDandTheta(patch)

