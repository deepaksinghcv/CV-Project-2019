
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def clustMasks(opts):

    # Local Variables: gtWidth, E, zz, i, k, j, xx, yy, S, t, w, theta, dist, nDists, nOrients, K, opts
    # Function calls: all, cosd, sum, rem, nargout, single, meshgrid, zeros, linspace, error, sind, clustMasks, gradientMag, size
    gtWidth = opts.gtWidth
    nDists = opts.nDists
    nOrients = opts.nOrients
    if plt.rem(gtWidth, 2.) != 0.:
        matcompat.error('gtWidth should be even')
    
    
    #% define gtWidth x gtWidth grid
    [xx, yy] = matcompat.meshgrid(np.arange(-gtWidth/2.+1., (gtWidth/2.)+1))
    #% define the distances and orientations
    k = gtWidth/1.0.
    dist = np.linspace(k, (-k), nDists)
    theta = np.arange(0., (180.-.01)+(180./nOrients), 180./nOrients)
    #% render seg masks for each cluster
    K = np.dot(nDists, nOrients)
    S = np.zeros(gtWidth, gtWidth, K)
    for i in np.arange(1., (nOrients)+1):
        t = theta[int(i)-1]
        w = np.array(np.vstack((np.hstack((cosd(t))), np.hstack((sind(t))))))
        zz = np.dot(w[0], xx)+np.dot(w[1], yy)
        for j in np.arange(1., (nDists)+1):
            k = np.dot(i-1., nDists)+j
            S[:,:,int(k)-1] = zz > dist[int(j)-1]
            
        
    #% check for bugs
    #% demonstrate how to convert segs S to edges E
    if nargout > 1.:
        E = np.zeros(matcompat.size(S))
        for k in np.arange(1., (K)+1):
            E[:,:,int(k)-1] = gradientMag(np.single(S[:,:,int(k)-1])) > .01
            
    
    
    return [S, E]