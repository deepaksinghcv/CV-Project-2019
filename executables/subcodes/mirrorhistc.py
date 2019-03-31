
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def mirrorhistc(x, e):

    # Local Variables: b, lastBin, nn, bn, n, bp, np, x, e
    # Function calls: all, mirrorhistc, max, min, histc, length, abs, error, diff, ndims, any, size
    #% [N,B] = mirrorhistc( X, E )
    #%
    #% Suppose E = [a b]. Then the binning
    #% used is (-b,-a] (-a,a) [a,b).
    #% 
    #% Suppose E = [a b c]. Then the binning
    #% used is (-c,-b] (-b,-a] (-a,a) [a,b) [b,c).
    #%
    #% ...and so on.
    if np.any((e<=0.)) or not np.all((np.diff(e) > 0.)):
        matcompat.error('invalid bin edges')
    
    
    if np.abs(matcompat.max(x)) >= e[int(0)-1]:
        matcompat.error('data is out of bounds')
    
    
    if matcompat.ndim(x) > 2. or matcompat.max(matcompat.size(x)) > 1.:
        matcompat.error('data should be a vector')
    
    
    x = x.flatten(0).conj()
    e = e.flatten(0).conj()
    e = np.array(np.hstack((0., e)))
    lastBin = length(e)-1.
    [nn, bn] = histc((-x[int((x<0.))-1]), e)
    bn = lastBin-bn+1.
    nn = nn[int(0-1.)-1:1.:-1.]
    [np, bp] = histc(x[int((x >= 0.))-1], e)
    bp = bp+lastBin-1.
    np = np[0:0-1.]
    b = 0.*x
    b[int((x<0.))-1] = bn
    b[int((x >= 0.))-1] = bp
    n = np.array(np.hstack((nn[0:0-1.], nn[int(0)-1]+np[0], np[1:])))
    return [n, b]