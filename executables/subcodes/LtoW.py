
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def LtoW(L):

    # Local Variables: W, h, L, w, y, x, z
    # Function calls: meshgrid, zeros, LtoW, size
    #% W = LtoW( L )
    [h, w] = matcompat.size(L)
    W = np.zeros(h, w, 121.)
    if 1.:
        #% simple version
    for y in np.arange(1., (h)+1):
        for x in np.arange(1., (w)+1):
            W[int(y)-1,int(x)-1,int(L[int(y)-1,int(x)-1])-1] = 1.
            
        
    else:
        #% harder to read but faster
        [x, y] = matcompat.meshgrid(np.arange(1., (w)+1), np.arange(1., (h)+1))
        x = x.flatten(1)
        y = y.flatten(1)
        z = L.flatten(1)
        W[int((y+np.dot(x-1., h)+np.dot(np.dot(z-1., h), w)))-1] = 1.
        
    
    return [W]