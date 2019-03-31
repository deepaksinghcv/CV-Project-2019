
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def collapse(W, opts, usemex):

    # Local Variables: orthog, Wori, o, usemex, W, V, nDists, opts
    # Function calls: nargin, collapseMex, collapse_orient, collapse, single
    #% V = collapse( W, opts, usemex )
    if nargin<3.:
        usemex = 1.
    
    
    #% TODO get rid of these restrictions
    orthog = np.array(np.hstack((np.arange(90., (-67.5)+(-22.5), -22.5))))-90.
    if usemex:
        V = collapseMex(W, np.single(orthog), (opts.gtWidth), (opts.nDists), (opts.nOrients), (opts.shrink), (opts.nThreads))
    else:
        nDists = opts.nDists
        V = 0.*W[:,:,0:opts.nOrients]
        for o in np.arange(1., (opts.nOrients)+1):
            Wori = W[:,:,int(np.dot(o-1., nDists)+1.)-1:np.dot(o, nDists)]
            V[:,:,int(o)-1] = collapse_orient(Wori, orthog[int(o)-1], opts)
            
        
    
    return [V]
def collapse_orient(Ws, theta, opts):

    # Local Variables: W, xx, Ws, Yq, theta, nDists, shrink, cen, yy, dx, dy, Y, X, d, i, k, m, p, r, dists, Xq, opts
    # Function calls: interpW_faster, cosd, imPad, abs, h, collapse_orient, ceil, meshgrid, linspace, w, max, sind
    nDists = opts.nDists
    shrink = opts.shrink
    #% pad chns and define central pixel grid 
    k = (nDists-1.)/2.
    cen = k+1.
    r = opts.gtWidth/1.0.
    p = np.ceil(matdiv(r, shrink))
    Ws = imPad(Ws, p, 'replicate')
    xx = np.arange(1.+p, (w-p)+1)
    yy = np.arange(1.+p, (h-p)+1)
    [X, Y] = matcompat.meshgrid(xx, yy)
    W = Ws[int(yy)-1,int(xx)-1,int(cen)-1]
    #% make step vector in orthog direction
    dx = cosd(theta)
    dy = sind(theta)
    m = matcompat.max(np.abs(np.array(np.hstack((dx, dy)))))
    dx = matdiv(dx, m)
    dy = matdiv(dy, m)
    #% translate d~=0 channels to line up with d=0
    dists = np.linspace((-r), r, nDists)
    for i in np.arange(1., (nDists)+1):
        d = dists[int(i)-1]
        if d == 0.:
            continue
        
        
        Xq = X+matdiv(np.dot(dx, d), shrink)
        Yq = Y-matdiv(np.dot(dy, d), shrink)
        W = W+interpW_faster(Ws[:,:,int(i)-1], Xq, Yq)
        
    return [W]
def interpW(W, x, y):

    # Local Variables: h, dy0, dy1, dx1, dx0, y1, W, y0, y, x, x0, x1
    # Function calls: size, interpW, floor
    x0 = np.floor(x)
    x1 = x0+1.
    dx0 = x-x0
    dx1 = 1.-dx0
    y0 = np.floor(y)
    y1 = y0+1.
    dy0 = y-y0
    dy1 = 1.-dy0
    h = matcompat.size(W, 1.)
    W = W[int((np.dot(x-1., h)+y0))-1]*dx1*dy1+W[int((np.dot(x0., h)+y0))-1]*dx0*dy1+W[int((np.dot(x-1., h)+y1))-1]*dx1*dy0+W[int((np.dot(x0., h)+y1))-1]*dx0*dy0
    return [W]
def interpW_faster(W, x, y):

    # Local Variables: h, dy0, dy1, dx1, dx0, y1, W, y0, y, x, x0, x1, inty, intx
    # Function calls: interpW_faster, all, size, floor
    #% avoid expensive interp math for integer input
    x0 = np.floor(x)
    intx = np.all(np.all((x == x0)))
    y0 = np.floor(y)
    inty = np.all(np.all((y == y0)))
    h = matcompat.size(W, 1.)
    dx1 = 1.-dx0
    y1 = y0+1.
    dy0 = y-y0
    dy1 = 1.-dy0
    W = W[int((np.dot(x-1., h)+y0))-1]*dx1*dy1+W[int((np.dot(x0., h)+y0))-1]*dx0*dy1+W[int((np.dot(x-1., h)+y1))-1]*dx1*dy0+W[int((np.dot(x0., h)+y1))-1]*dx0*dy0
    return [W]