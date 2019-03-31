
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def labelmap(bmap, mask, opts):

    # Local Variables: nearest, dist, thetaBin, V, locs, ind, Theta, nOrients, bmap, Dx, Dy, theta, nDists, gtWidth, C, labels, nLabels, I, J, step, R, U, T, dx, dy, Nearest, Dist, h, k, Labels, mask, edges, w, opts
    # Function calls: binangles360, angleimage, cosd, distBin, all, double, cross, sign, labelmap, meshgrid, ind2sub, bwdist, sind, repmat, find, size
    #% [Labels,Dist,Theta] = labelmap( bmap, mask, opts )
    #% It is assumed that bmap was already cleaned (cleanbmap.m)
    gtWidth = opts.gtWidth
    nOrients = opts.nOrients
    nDists = opts.nDists
    nLabels = np.dot(nOrients, nDists)
    #% calculate distances and angles
    [h, w] = matcompat.size(bmap)
    [Dist, Nearest] = bwdist(bmap)
    Nearest = np.double(Nearest)
    Theta = angleimage(bmap, (opts.angleRad))
    [R, C] = ind2sub(np.array(np.hstack((h, w))), Nearest)
    [J, I] = matcompat.meshgrid(np.arange(1., (w)+1), np.arange(1., (h)+1))
    Dx = C-J
    Dy = -(R-I)
    #% focus on locations indicated by mask
    locs = nonzero(mask)
    dx = Dx[int(locs)-1]
    dy = Dy[int(locs)-1]
    nearest = Nearest[int(locs)-1]
    theta = Theta[int(nearest)-1]
    thetaBin = binangles360(theta, (nOrients*2.))
    T = np.array(np.hstack((sind(theta), cosd(theta), 0.*theta)))
    V = np.array(np.hstack((dy, dx, 0.*dx)))
    U = np.cross(T, V)
    dist = Dist[int(locs)-1]*np.sign((-U[:,2]))
    #% standardize
    ind = thetaBin > nOrients
    dist[int(ind)-1] = -dist[int(ind)-1]
    thetaBin[int(ind)-1] = thetaBin[int(ind)-1]-nOrients
    #% bin distance
    k = (nDists-1.)/2.
    step = matdiv(gtWidth-2., nDists-1.)
    edges = np.array(np.hstack((np.dot(step, np.array(np.hstack((np.arange(1., (k)+1)))))-step/2., gtWidth/2.)))
    labels = np.dot(thetaBin-1., nDists)+distBin.conj().T
    #% IMPORTANT assertion that has caught MANY bugs
    #% write result images
    Labels = matcompat.repmat((nLabels+1.), np.array(np.hstack((h, w))))
    Dist = Labels
    Theta = Labels
    Labels[int(locs)-1] = labels
    Dist[int(locs)-1] = distBin
    Theta[int(locs)-1] = thetaBin
    return [Labels, Dist, Theta]