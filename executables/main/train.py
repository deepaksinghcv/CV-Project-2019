def train(*varargin):
        dfs = mcellarray([mstring('imWidth'), 32, mstring('gtWidth'), 16, mstring('nOrients'), 8, mstring('nDists'), 15, mstring('nPos'), 2e6, mstring('nNeg'), 2e6, mstring('nTrees'), 24, mstring('fracFtrs'), 1 / 8, mstring('shrink'), 2, mstring('minCount'), 1, mstring('minChild'), 8, mstring('maxDepth'), 64, mstring('split'), mstring('gini'), mstring('nHistBins'), 4, mstring('grdSmooth'), 0, mstring('chnSmooth'), 2, mstring('simSmooth'), 8, mstring('normRad'), 4, mstring('nCells'), 5, mstring('angleRad'), 6, mstring('seed'), 1, mstring('calibrate'), 1, mstring('useParfor'), 1, mstring('cacheDir'), mstring('/home/ashishmenon/labpc/oef/cache/'), mstring('modelFnm'), mstring('model'), mstring('bsdsDir'), mstring('/home/ashishmenon/labpc/oef/BSDS500/data/')])
    opts = getPrmDflt(varargin, dfs, 1)
    if (nargin == 0):
        model = opts; print model
        return
        

        # if forest exists load it and return
        forestDir = mcat([opts.cacheDir, mstring('/forest/')])
        forestFnm = mcat([forestDir, opts.modelFnm])
        if (exist(mcat([forestFnm, mstring('.mat')]), mstring('file'))):
            load(mcat([forestFnm, mstring('.mat')]))
            return
            

            # compute constants and store in opts
            nTrees = opts.nTrees
            nCells = opts.nCells; print nCells
            shrink = opts.shrink

            nOrients = opts.nOrients
            nDists = opts.nDists; print nDists

            angleRad = opts.angleRad
            opts.nClusts = nOrients * nDists; print opts.nClusts

            opts.nPos = round(opts.nPos)
            opts.nNeg = round(opts.nNeg); print opts.nNeg

            imWidth = opts.imWidth
            gtWidth = opts.gtWidth; print gtWidth

            imWidth = round(max(gtWidth, imWidth) / shrink / 2) * shrink * 2
            opts.imWidth = imWidth
            opts.gtWidth = gtWidth; print opts.gtWidth

            nChnsGrad = (opts.nHistBins + 1) * 2
            nChnsColor = 3; print nChnsColor

            nChns = nChnsGrad + nChnsColor
            opts.nChns = nChns; print opts.nChns

            opts.nChnFtrs = imWidth * imWidth * nChns / shrink / shrink
            opts.nSimFtrs = (nCells * nCells) * (nCells * nCells - 1) / 2 * nChns
            opts.nTotFtrs = opts.nChnFtrs + opts.nSimFtrs
            opts.clustFnm = sprintf(mstring('clusters_%d_%d_%d_%d_%d_%d'), imWidth, gtWidth, nDists, nOrients, shrink, angleRad)
            disp(opts)


            # compute cluster data if it doesn't exist
            clustFnm = mcat([opts.cacheDir, mstring('/clust/'), opts.clustFnm, mstring('.mat')])
            if not exist(clustFnm, mstring('file')):
                disp(mstring('Clust file not found'))

                clusters = genClustData(opts)
                save(clustFnm, mstring('clusters'))

                

                # train nTrees random trees (can use parfor if enough memory)
                stream = RandStream(mstring('mrg32k3a'), mstring('Seed'), opts.seed)

                #ASHISH
                if (opts.useParfor):                    mslice[1:nTrees]
                    trainTree(opts, stream, i)
                    
                else:
                    for i in mslice[1:nTrees]:
                        trainTree(opts, stream, i)
                        
                        

                        # build model struct
                        model = mergeTrees(opts)
                        model.beta = mcat([]); print model.beta

                        # add test time options (can be changed later)
                        opts = model.opts
                        opts.stride = opts.shrink; print opts.stride

                        opts.nThreads = 4
                        opts.nTreesEval = round(nTrees / 2); print opts.nTreesEval

                        opts.scales = mcat([.25, .5, 1, 2])
                        opts.sharpen = mcat([1, 1, 2, 2]); print opts.sharpen

                        opts.collapse = 1
                        opts.nms = 0; print opts.nms
                        model.opts = opts

                        # learn calibration weights model.beta
                        if (opts.calibrate):
                            model = calibrate(model); print model
                            
                            # save model
                            if (not exist(forestDir, mstring('dir'))):
                                mkdir(forestDir)
                                
                                save(mcat([forestFnm, mstring('.mat')]), mstring('model'), mstring('-v7.3'))

                                
