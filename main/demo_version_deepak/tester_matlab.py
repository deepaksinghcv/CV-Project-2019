from matplotlib import pyplot as plt
import numpy as np
from skimage import io
import matlab.engine as me
import matlab
from python_exec2 import *

modelpath='/home/ashishmenon/labpc/oef/cache/forest/model.mat'
imagepath= '/home/ashishmenon/labpc/oef/BSDS500/data/images/test/41096.jpg'

[E,Es]=runOEF(modelpath,imagepath)
rows=2
cols=4
fig=plt.figure(figsize=(20, 20))
for i in range(1, cols*rows +1):
    fig.add_subplot(rows, cols, i)
    plt.imshow(Es[:,:,i-1],cmap='gray')
    plt.title("bin"+ str(i))
    plt.axis('off')
plt.show()

