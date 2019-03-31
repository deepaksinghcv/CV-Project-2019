
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def mexomp(cppFile):

    # Local Variables: cppFile, cmd
    # Function calls: mexomp, sprintf, eval
    #% mexomp( cppFile )
    #% Compile mex file with OpenMP opts set
    cmd = np.array(np.hstack(('mex %s \'-DUSEOMP\' CXXFLAGS="\\$CXXFLAGS ', '-fopenmp" LDFLAGS="\\$LDFLAGS -fopenmp"')))
    eval(sprintf(cmd, cppFile))
    return 