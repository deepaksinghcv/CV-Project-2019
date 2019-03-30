
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def calibrate(model):

    # Local Variables: scale, frac, beta, Y, X, model, opts
    # Function calls: i, genCalibData, learnBeta, calibrate, scales
    #% model = calibrate( model )
    #% Set calibration weights model.beta
    #%
    #% This file calls a function that uses a parfor. With
    #% 12 matlab workers, calibration should take ~20 min.
    opts = genCalibData()
    opts.frac = frac[int(1j)-1]
    opts.scale = scales(1j)
    [X, Y] = genCalibData(model, opts)
    model.beta[int(i)-1] = learnBeta(X.flatten(1), Y.flatten(1))
    return [model]