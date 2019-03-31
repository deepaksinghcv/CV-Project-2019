
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def ncc(seg, width):

    # Local Variables: B, hash, y, i, siz, s, N, seg, width, S, cacheDir, u, x, Nu, xs, ys, uniq, o2, o1
    # Function calls: load, hashMat, unique, false, floor, sum, nan, uint8, ceil, uniqfilt, length, save, ncc, find, bwlabel, size
    #% N = ncc( seg, w )
    #%
    #% N(i,j) = number of connected components in the
    #%   w-by-w window centered on location (i,j) of seg
    #%
    #% What do I mean by "number of connected components"?  
    #% Here are some example segmentation patches:
    #% 
    #%   1 1 2 2 1 1
    #%   1 1 2 2 1 1      this patch has THREE segments, even
    #%   1 1 2 2 1 1      though unique() only returns [1;2].
    #%   1 1 2 2 1 1
    #% 
    #%   3 3 7 7 7 7
    #%   3 3 7 7 7 7      this patch has FOUR segments, even
    #%   7 7 3 3 3 3      though unique() is simply [3;7].  
    #%   7 7 3 3 3 3
    #%
    #% THIS CODE IS VERY SLOW, hence all results are cached.
    cacheDir = '/home/ashishmenon/labpc/oef/cache/clust/nccCache/'
    hash = hashMat(np.array(np.vstack((np.hstack((seg.flatten(1))), np.hstack((width))))))
    try:
        np.load(np.array(np.hstack((cacheDir, hash))), 'N')
    except :
            siz = matcompat.size(seg)
            o1 = np.floor(((width-1.)/2.))
            o2 = np.ceil(((width-1.)/2.))
            #% This takes ~80 seconds per image
            N = np.nan(siz)
            B = false(siz)
            B[int(o1+1.)-1:0-o2,int(o1+1.)-1:0-o2] = 1.
            Nu = uniqfilt(seg, o2)
            N[int(np.logical_and(B, Nu == 1.))-1] = 1.
            [ys, xs] = nonzero(np.logical_and(B, Nu > 1.))
            for i in np.arange(1., (length(ys))+1):
                y = ys[int(i)-1]
                x = xs[int(i)-1]
                S = seg[int(y-o1)-1:y+o2,int(x-o1)-1:x+o2]
                uniq = np.unique(S)
                N[int(y)-1,int(x)-1] = 0.
                for s in uniq.flatten(0).conj():
                    u = np.unique(bwlabel((S == s), 4.))
                    N[int(y)-1,int(x)-1] = N[int(y)-1,int(x)-1]+np.sum((u != 0.))
                    
                
            #% convert to uint8 to save disk space
            #% (but this converts NaNs to 0s..)
            N = np.uint8(N)
            plt.save(np.array(np.hstack((cacheDir, hash))), 'N')
    
    return [N]
def uniqfilt(seg, k):

    # Local Variables: seg, i, k, nuniq, se
    # Function calls: max, imdilate, uniqfilt, ones, zeros, size
    #% nuniq = uniqfilt(seg,k)
    #%
    #% INPUTS
    #%   seg     groundTruth{j}.Segmentation
    #%   k       filter half width
    #%
    #% ASSUME THAT SEG LABELS ARE {1,2,...,NSEGS}
    #%
    #% This function is a fast version of the following:
    #% [h w] = size(seg);
    #% nuniq = zeros(h,w);
    #% for y = 1:h
    #%   y1 = max(1,y-k);
    #%   y2 = min(h,y+k);
    #%   for x = 1:w
    #%     x1 = max(1,x-k);
    #%     x2 = min(w,x+k);
    #%     patch = seg(y1:y2,x1:x2);
    #%     nuniq(y,x) = numel(unique(patch));
    #%   end
    #% end
    #% How long does it take to run unique(seg)? I tried this for all
    #% groundTruth{j}.Segmentation for all images. It took 0.0123 sec
    #% at most, 0.0027 sec on average, and 0.0022 sec at best.
    se = np.ones((2.*k+1.))
    nuniq = np.zeros(matcompat.size(seg))
    for i in np.arange(1., (matcompat.max(seg.flatten(1)))+1):
        nuniq = nuniq+imdilate((seg == i), se)
        
    return [nuniq]