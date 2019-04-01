from matplotlib import pyplot as plt
import numpy as np
from skimage import io
import matlab.engine as me
import matlab
from python_exec2 import *

modelpath='/home/ashishmenon/labpc/oef/cache/forest/model.mat'
imagepath= '/home/ashishmenon/labpc/oef/BSDS500/data/images/test/41096.jpg'

E=runOEF(modelpath,imagepath)
io.imshow(E,cmap='gray')
io.show()


