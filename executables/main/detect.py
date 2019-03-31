
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def detect(imagename, filename):

    # Local Variables: I1, E, nms, threshW, scales, I, k, collapse, sh, filename, i, beta, imagename, opts, calibrate, sc, model, E1, sharpen, Es, nThreads
    # Function calls: load, detect, imResample, h, sum, isfield, length, w, imread, ssdetect, true
    I = plt.imread(imagename)
    model = np.load(filename, 'model')
    model = model.model
    model.opts.nms = 0.
    model.opts.nThreads = 8.
    #% set to num logical cpu cores
    model.opts.calibrate = true
    #% see section 3 of cvpr paper (p.4)
    model.opts.collapse = true
    #% see section 5.3 of cvpr paper (pp.6-7)
    #% [E,Es] = detect(I, model)
    #%
    #% INPUTS
    #%  I     - HxWx3 RGB image
    #%  model - OEF model (output of train.m)
    #%
    #% OUTPUTS
    #%  E     - HxW image of boundary strengths in [0,inf)
    #%  Es    - HxWxO boundary strengths at different orientations,
    #%          where O = model.opts.nOrients is set at train time.
    #%
    #% Note that you probably want to set model.opts.collapse=1.
    #% This dramatically speeds up detection at almost no cost in
    #% accuracy (ODS/AP drop by < .01). You can also get slightly
    #% better AP by setting model.opts.calibrate = 1, but this
    #% requires calibration weights model.beta (see calibrate.m).
    #% check parameters
    opts = model.opts
    k = length((opts.scales))
    if opts.calibrate:
        
    
    
    if not isfield(opts, 'threshW'):
        model.opts.threshW = 0.
    
    
    #% run ssdetect once for each scale
    scales = opts.scales
    sharpen = opts.sharpen
    beta = model.beta
    Es = 0.
    for i in np.arange(1., (k)+1):
        sc = scales[int(i)-1]
        sh = sharpen[int(i)-1]
        if opts.calibrate:
            model.beta = beta[int(i)-1]
        
        
        I1 = imResample(I, sc)
        model.opts.sharpen = sh
        E1 = ssdetect(I1, model)
        Es = Es+imResample(E1, np.array(np.hstack((h, w))))
        
    Es = matdiv(Es, k)
    #% flatten and optionally perform nms
    if not opts.nms:
        E = np.sum(Es, 3.)
    else:
        E = nms[int(Es)-1,0,79,int((opts.nThreads))-1]
        
    
    return [E, Es]
def ssdetect(I, model):

    # Local Variables: E, inds, chnsSim, I, cen, m, chnsReg, n, r, W, V, ind, model, opts
    # Function calls: indToWavg, reshape, convTri, exp, h, imToInd, impad4, single, WtoE, w, edgesChns, ssdetect, collapse
    #% pad image, making divisible by 4
    opts = model.opts
    I = impad4(I, (opts.imWidth/2.))
    #% apply forest to image and build weights W
    [chnsReg, chnsSim] = edgesChns(I, opts)
    if opts.sharpen:
        I = convTri(np.single(I), 1.)
    
    
    ind = imToInd(model, chnsReg, chnsSim)
    W = indToWavg(ind, model)
    if opts.threshW > 0.:
        W[int((W<opts.threshW))-1] = 0.
    
    
    if opts.calibrate:
        W = 1.-np.exp(np.dot(-model.beta, W))
    
    
    #% optionally collapse d~=0 channels onto d=0
    if opts.collapse:
        V = collapse(W, opts)
        W[:] = 0.
        n = opts.nDists
        m = opts.nOrients
        cen = (n+1.)/2.
        inds = np.reshape(np.arange(1., (np.dot(m, n))+1), n, m)
        W[:,:,inds[int(cen)-1,:]] = V
    
    
    #% build E from distributions W
    E = WtoE(model, W, I)
    r = opts.gtWidth/2.
    E = E[int(1.+r)-1:h+r,int(1.+r)-1:w+r,:]
    return [E]