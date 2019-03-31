
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def binangles360(angles, nBins):

    # Local Variables: a, nBins, b, edges, angles, delta, orient
    # Function calls: binangles360, any, error
    #% Assume angles lie in [0,360]
    if np.any(np.logical_or(angles<0., angles > 360.)):
        matcompat.error('angles should be in the range [0,360]')
    
    
    #%
    #% change from [0,360] to [-270,90]
    #%
    angles[int((angles > 90.))-1] = angles[int((angles > 90.))-1]-360.
    delta = 360./nBins
    a = -270.+delta/2.
    b = +90.-delta/2.
    edges = np.arange(a, (b)+(delta), delta)
    orient = nBins-orient+1.
    orient[int((orient == nBins+1.))-1] = 1.
    return [orient]