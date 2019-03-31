
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def asserteq(varargin):

    # Local Variables: varargin, i
    # Function calls: length, error, asserteq, isequal
    #% asserteq(in1, in2, ...)
    #% Assert all arguments are equal (via "isequal")
    #% If nargin is 1 then do nothing
    #% Sam Hallman, 2013
    if length(varargin) >= 2.:
        for i in np.arange(2., (length(varargin))+1):
            if not isequal(varargin.cell[0], varargin.cell[int(i)-1]):
                matcompat.error('inputs %d,%d not equal', 1., i)
            
            
            
    
    
    return 