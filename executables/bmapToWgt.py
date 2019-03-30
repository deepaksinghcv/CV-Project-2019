
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def bmapToWgt(bmap, type):

    # Local Variables: posmask, Wd, Wc, W, Wa, h, is, h1, L, js, Wgt, bmap, w, pad, type, w1, Wb
    # Function calls: imResample, struct, cleanbmap, max, bmapToWgt, asserteq, LtoW, labelmap, bwdist, mod, size
    #% Wgt = bmapToWgt( bmap, type )
    #%
    #% Input bmap should not be padded, and type
    #% is either 'exact' or 'max' or 'interp'. The
    #% Wgt returned is binary for 'exact' and 'max'.
    #%
    #% The 'max' type seems to work best but has the
    #% disadvantage that the weights don't sum to 1.
    #%
    #% The size of Wgt is the same as the size of
    #% the W returned by indToW when "ind" was built
    #% from the original image padded only to have
    #% height/width divisible by 4 (see imgDemo.m).
    bmap = cleanbmap(bmap)
    posmask = bwdist(bmap)<16./2.
    L = labelmap(bmap, posmask, struct('gtWidth', 16., 'nDists', 15., 'nOrients', 8., 'angleRad', 6.))
    #% All of the index math assumes the original image
    #% was padded to have height/width divisible by 4,
    #% since that is required by edgesChns
    [h, w] = matcompat.size(bmap)
    pad = np.mod((4.-np.mod(np.array(np.hstack((h, w))), 4.)), 4.)
    h = h+pad[0]
    w = w+pad[1]
    _switch_val=type
    if False: # switch 
        pass
    #% Nearest nbor downsampling
    elif _switch_val == 'exact':
        L = L[15:h-18.:2.,15:w-18.:2.]
        Wgt = LtoW(L)
        #% Charless's idea. Works really well
    elif _switch_val == 'max':
        W = LtoW(L)
        is = np.arange(16., (h-18.)+(2.), 2.)
        js = np.arange(16., (w-18.)+(2.), 2.)
        Wa = W[int(is)-1,int(js)-1,:]
        Wb = W[int(is)-1,int((js+1.))-1,:]
        Wc = W[int((is+1.))-1,int(js)-1,:]
        Wd = W[int((is+1.))-1,int((js+1.))-1,:]
        Wgt = matcompat.max(Wa, matcompat.max(Wb, matcompat.max(Wc, Wd)))
        #% Probably shouldn't use this
    elif _switch_val == 'interp':
        Wgt = LtoW(L)
        Wgt = Wgt[15:h-18.,15:w-18.,:]
        Wgt = imResample(Wgt, 0.5, 'bilinear')
    
    h1 = h/1.06.
    w1 = w/1.06.
    asserteq(matcompat.size(Wgt), np.array(np.hstack((h1, w1, 121.))))
    return [Wgt]