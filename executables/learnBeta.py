
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def plt.solve(X, y):

    # Local Variables: D, N, beta, y, X, opts
    # Function calls: double, asserteq, lsqcurvefit, ones, solve, optimoptions, size
    #% Solve subproblem k using lsqcurvefit with analytic derivatives
    [N, D] = matcompat.size(X)
    asserteq(matcompat.size(y), np.array(np.hstack((N, 1.))))
    opts = optimoptions('lsqcurvefit', 'Jacobian', 'on', 'Display', 'off')
    beta = lsqcurvefit(myfun, np.ones(D, 1.), X, np.double(y), np.array([]), np.array([]), opts)
    return [beta]
def myfun(beta, X):

    # Local Variables: D, F, J, N, beta, X
    # Function calls: myfun, double, nargout, exp, repmat, size
    #% size( beta )   = [D 1] 
    #% size(  X   )   = [N D]
    #% size( X*beta ) = [N 1]
    [N, D] = matcompat.size(X)
    F = 1.-np.exp(np.dot(-X, beta))
    F = np.double(F)
    if nargout > 1.:
        J = matcompat.repmat((1.-F), np.array(np.hstack((1., D))))*X
        J = np.double(J)
    
    
    return [F, J]