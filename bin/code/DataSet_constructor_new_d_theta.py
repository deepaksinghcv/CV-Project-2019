
# coding: utf-8

# In[ ]:


from skimage import io
from matplotlib import pyplot as plt
import skimage
import sklearn
import scipy.io
import AngleCalculator as AC

import os
gtlist=[]
imglist=[]
data=os.listdir('../../../BSR/BSDS500/data/groundTruth/train/')
addr='../../../BSR/BSDS500/data/groundTruth/train/'
for i in range(len(data)):
    mat=scipy.io.loadmat(addr+str(data[i]))   
    gt=mat['groundTruth'][0,1][0,0][1]
    gtlist.append(gt)
    img=io.imread('../../../BSR/BSDS500/data/images/train/'+ data[i].split('.')[0]+'.jpg')
    imglist.append(img)
    
    
# io.imshow(a1,cmap='gray')
# io.show()
# io.imshow(b,cmap='gray')
# io.show()
# io.imshow(b1,cmap='gray')
# io.show()
# io.imshow(c,cmap='gray')
# io.show()
# io.imshow(c1,cmap='gray')
# io.show()

# print(len(gtlist),len(imglist))


# In[3]:


# from skimage import io
# io.imshow(gtlist[0])


# In[ ]:


import numpy as np
d={}
for k in range(len(gtlist)):
    a=gtlist[k]
    a_im=imglist[k]
    for i in range (a.shape[0]):
        for j in range (a.shape[1]):
            patch=a[i:16+i,j:16+j]
            patch_img=a_im[i:16+i,j:16+j]
            d['array']=patch_img
            locx,locy = np.where(patch == 1)
            if len(list(zip(locx,locy)))<2:
                if not os.path.exists('../../../output/background'):
                    os.makedirs('../../../output/background')
                scipy.io.savemat('../../../output/background/'+str(k)+'_'+str(i)+'_'+str(j)+'_'+'16.mat',d,appendmat=True,do_compression=True)
            
            else:
                dist,theta=AC.getUpdatedDandTheta(patch)
                bins_theta=list(np.arange(-90+22.5,90+22.5,22.5))
                theta_digitized = np.digitize(theta, bins_theta)
                bins_d=list(np.arange(-7,8))
                d_digitized = np.digitize(dist, bins_d)
                if not os.path.exists('../../../output/{}_{}'.format(d_digitized,theta_digitized)):
                    os.makedirs('../../../output/{}_{}'.format(d_digitized,theta_digitized))
                scipy.io.savemat('../../../output/{}_{}/{}_{}_{}_16.mat'.format(d_digitized,theta_digitized,k,i,j),d,appendmat=True,do_compression=True)

        
        
             
        
        
         
       
        
        
    


# In[ ]:


def getThetaInDegrees(o):
    if(o.shape[0] >= 2):
        theta = -np.arctan((o[0,0]-o[1,0])/(o[0,1]-o[1,1]))
        #theta = -np.arctan((o[0,1]-o[1,1])/o[0,0]-o[1,0])
       
    return theta*180/np.pi



def checkForSign(nep,orig):
    retVal = 0
#     print("origin",orig)
#     print("nep",nep)
    
    diff = orig-nep
    
    x = diff[0]
    y = diff[1]
    
    
    if x > 0 :
        if y < 0:
            retVal = -1
            return retVal
        if y > 0:
            retVal = +1
            return retVal
        if y == 0:
            retVal = +1
            return retVal
        
    if x < 0 :
        if y < 0:
            retVal = +1
            return retVal
        if y > 0:
            retVal = -1
            return retVal
        if y == 0:
            retVal = -1
            return retVal
        
    if x == 0 :
        if y < 0:
            retVal = +1
            return retVal
        if y > 0:
            retVal = -1
            return retVal
        if y == 0:
            retVal = 0
            return retVal
            


# def getDandTheta(a):
#     actualD = 0
#     xc,yc = np.int(np.floor(a.shape[0]/2)),np.int(np.floor(a.shape[1]/2))
#     orig = np.array([xc,yc])
    
#     #find locations of pixels
#     locx,locy = np.where(a == 1)
    
#     o = np.array(list(zip(locx,locy)))
    
#     dVals = np.sqrt(np.sum((o-orig)**2,axis=1))
    
#     nep = o[np.argmin(np.sqrt(np.sum((o-orig)**2,axis=1)))]
    
#     signCheck = checkForSign(nep,orig)
#     d = np.min(dVals)
#     actualD =  signCheck*d
    
    
#     thetaInDegrees = getThetaInDegrees(o)
#     return actualD,thetaInDegrees

