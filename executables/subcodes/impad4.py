
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def impad4(I, r):

    # Local Variables: Ipad, I, r, p
    # Function calls: imPad, nargin, h, impad4, w, mod
    #% Pad image by r on all sides, plus extra on
    #% the right and bottom as necessary to make
    #% divisible by 4, as required by edgesChns
    if nargin<2.:
        r = 0.
    
    
    p = np.array(np.hstack((r, r, r, r)))
    p[int(np.array(np.hstack((2., 4.))))-1] = p[int(np.array(np.hstack((2., 4.))))-1]+np.mod((4.-np.mod((np.array(np.hstack((h, w)))+2.*r), 4.)), 4.)
    Ipad = imPad(I, p, 'symmetric')
    return [Ipad]