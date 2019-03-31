
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def cleanbmap(bmap):

    # Local Variables: list, bmap
    # Function calls: cleanedgelist, cleanbmap, bwmorph, edgelink, edgelist2image, inf, size
    list = edgelink(bmap)
    list = cleanedgelist(list, 7.)
    bmap = edgelist2image(list, matcompat.size(bmap))
    bmap = bwmorph(bwmorph(bmap, 'fill'), 'thin', np.inf)
    #% [update 17 Sep 2014]
    #% If the output bmap has a single, isolated 'on' pixel
    #% then edgelink will not find it, which leads to bugs
    bmap = bwmorph(bmap, 'clean')
    return [bmap]