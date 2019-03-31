
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def nms(Es, alpha, tol, nThreads):

    # Local Variables: E, nThreads, outlier, Oe, Ye, O, Xe, Xt, tol, X, Y, alpha, Ot, nOrients, Yt, Es
    # Function calls: convTri, nms, edgeOrient, atan, sum, cos, edgesNmsMex, nargin, single, abs, pi, sin, size
    #% E = nms( Es, alpha, tol, nThreads )
    if nargin<2.:
        alpha = 1.
    
    
    if nargin<3.:
        tol = 80.
    
    
    if nargin<4.:
        nThreads = 4.
    
    
    nOrients = matcompat.size(Es, 3.)
    tol = np.dot(tol, np.pi)/180.
    #% Flatten and smooth slightly (it helps)
    E = np.sum(Es, 3.)
    E = convTri(E, 1.)
    #% Compute orientation map
    np.array([])
    Ot = np.dot(matdiv(np.single((Ot-1.)), nOrients), np.pi)
    Oe = edgeOrient(E, 4.)
    if tol > 0.:
        outlier = np.abs((Oe-Ot)) > tol
        Oe[int(outlier)-1] = Ot[int(outlier)-1]
    
    
    Xt = np.cos(Ot)
    Yt = np.sin(Ot)
    Xe = np.cos(Oe)
    Ye = np.sin(Oe)
    X = Xt+np.dot(alpha, Xe-Xt)
    Y = Yt+np.dot(alpha, Ye-Yt)
    O = atan((Y/X))
    #% Use those orientations to do nms
    E = edgesNmsMex(E, O, 1., 5., 1.01, nThreads)
    return [E]
def edgeOrient(W, r):

    # Local Variables: Oxy, Oyy, O, W, r, Oy, Ox
    # Function calls: convTri, pi, Oxx, edgeOrient, atan, sign, gradient2, mod
    #% compute approximate orientation map
    [Ox, Oy] = gradient2(convTri(W, r))
    [Oxy, Oyy] = gradient2(Oy)
    O = np.mod(atan((Oyy*np.sign((-Oxy))/(Oxx+1e-5))), np.pi)
    return [O]