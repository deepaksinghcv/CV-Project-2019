
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def buildW(I, model, method):

    # Local Variables: I, chns, indToW, W, chnsSs, model, method
    # Function calls: buildW, edgesChns, impad4, imToInd, nargin
    #% W = buildW( I, model, [method] )
    #% method is either 'avg' or 'vote'
    #% This file is used for calibration
    if nargin<3.:
        method = 'avg'
    
    
    #% Select method for building W from tree predictions
    _switch_val=method
    if False: # switch 
        pass
    elif _switch_val == 'avg':
        indToW = indToWavg
    elif _switch_val == 'vote':
        indToW = indToWvote
    
    #% Run forest over the image and build W
    [chns, chnsSs] = edgesChns(impad4(I), (model.opts))
    W = indToW[int(imToInd(model, chns, chnsSs))-1,int(model)-1]
    return [W]