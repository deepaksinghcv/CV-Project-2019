from matplotlib import pyplot as plt
import numpy as np
from skimage import io
import matlab.engine as me
import matlab
mEng = me.start_matlab()


def runOEF(modelpath,imagepath):
	[E,Es] = mEng.detect(imagepath,modelpath,nargout=2)
	
	E=np.array(E,dtype=float)
	Es=np.asarray(Es)
	
	return E,Es

