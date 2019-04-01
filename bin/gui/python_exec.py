from matplotlib import pyplot as plt
import numpy as np
from skimage import io
import matlab.engine as me
import matlab
mEng = me.start_matlab()

#model=scipy.io.loadmat('model.mat')   
#model_hd5= h5py.File('model.mat', 'r')

# model= mEng.load("/home/ashish95/Documents/CV_project/oef/cache/forest/model.mat")


# model.opts.nms       = 0
# model.opts.nThreads  = 8
# model.opts.calibrate = true  
# model.opts.collapse  = true
filename='/home/ashishmenon/labpc/oef/cache/forest/model.mat'
imagename= '/home/ashishmenon/labpc/oef/BSDS500/data/images/test/41096.jpg'

#--------------------------------------------------------------------------------------------------
# I = io.imread('/home/ashish95/Documents/CV_project/oef/BSDS500/data/images/train/2092.jpg');
# print(I.shape)
# data = I.tolist()
# print(len(data))
# image_mat = matlab.uint8(data)
# image_mat.reshape((321, 481,3))
#--------------------------------------------------------------------------------------------------

#[x,y,z]=eng.edgelink(image_mat,nargout=3)


[E,Es] = mEng.detect(imagename,filename,nargout=2)
# figure, subplot(131), imshow(I),
# subplot(132), imagesc(E),
# colormap gray, axis off image,
# subplot(133), nOrients = size(Es,3);
# labels = strsplit(num2str(1:nOrients));
# montage2( Es, struct('labels',{labels}) );
print(type(E))

E=np.array(E,dtype=int)
io.imshow(E,cmap='gray')
io.show()

