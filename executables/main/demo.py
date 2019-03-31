
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

#% Quick OEF demo script
#% =====================
#% Load model
file = '/home/ashish95/Documents/oef/cache/forest/model.mat'
try:
    np.load(file, 'model')
except :
        #% download the trained model (98 MB)

#% Set some options before calling detect.m
model.opts.nms = 0.
model.opts.nThreads = 8.
#% set to num logical cpu cores
model.opts.calibrate = true
#% see section 3 of cvpr paper (p.4)
model.opts.collapse = true
#% see section 5.3 of cvpr paper (pp.6-7)
#% Detect boundaries
#%I = imread('/home/ashish95/Documents/oef/BSDS500/data/images/test/87015.jpg');
I = '/home/ashish95/Documents/oef/BSDS500/data/images/test/87015.jpg'
[E, Es] = detect(I, file)
#% View results
plt.figure
plt.subplot(131.)
plt.imshow(I)
plt.subplot(132.)
imagesc(E)
colormap(gray)
plt.axis(offimage)
plt.subplot(133.)
nOrients = matcompat.size(Es, 3.)
labels = strsplit(num2str(np.arange(1., (nOrients)+1)))
montage2(Es, struct('labels', cellarray(np.hstack((labels)))))