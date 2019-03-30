
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def edgesChns(I, opts):

    # Local Variables: I1, simSm, Ishrink, chnsSim, I, H, k, M, chnsReg, O, chns, i, s, chnSm, cs, shrink, opts
    # Function calls: rgbConvert, convTri, imResample, max, cat, cell, edgesChns, gradientHist, round, gradientMag, size
    #% Compute feature channels
    #% [chnsReg,chnsSim] = edgesChns( I, opts )
    #%
    #% This is a slightly modified version of the edgesChns
    #% file from Piotr Dollar's Structured Edge Detection
    #% Toolbox, https://github.com/pdollar/edges.
    shrink = opts.shrink
    chns = cell(1., (opts.nChns))
    k = 0.
    if matcompat.size(I, 3.) == 1.:
        cs = 'gray'
    else:
        cs = 'luv'
        
    
    I = rgbConvert(I, cs)
    Ishrink = imResample(I, (1./shrink))
    k = k+1.
    chns.cell[int(k)-1] = Ishrink
    for i in np.arange(1., 3.0):
        s = 2.**(i-1.)
        if s == shrink:
            I1 = Ishrink
        else:
            I1 = imResample(I, (1./s))
            
        
        I1 = convTri(I1, (opts.grdSmooth))
        [M, O] = gradientMag(I1, 0., (opts.normRad), .01)
        H = gradientHist(M, O, matcompat.max(1., matdiv(shrink, s)), (opts.nHistBins), 0.)
        k = k+1.
        chns.cell[int(k)-1] = imResample(M, matdiv(s, shrink))
        k = k+1.
        chns.cell[int(k)-1] = imResample(H, matcompat.max(1., matdiv(s, shrink)))
        
    chns = cat(3., chns.cell[0:k])
    chnSm = matdiv(opts.chnSmooth, shrink)
    if chnSm > 1.:
        chnSm = np.round(chnSm)
    
    
    simSm = matdiv(opts.simSmooth, shrink)
    if simSm > 1.:
        simSm = np.round(simSm)
    
    
    chnsReg = convTri(chns, chnSm)
    chnsSim = convTri(chns, simSm)
    return [chnsReg, chnsSim]