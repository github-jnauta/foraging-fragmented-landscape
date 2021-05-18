""" Code for analyzing the raw data """
# Import necessary libraries
import time 
import numpy as np 
# Import modules
import src.args 

class Analyze(object):
    def __init__(self) -> None:
        pass

    def compute_search_efficiency(self, args):
        """ Compute the search efficiency η"""
        # Specify directories
        _dir = "data/"
        _rdir = "results/"
        # Load variable arguments
        _alpha = np.loadtxt(_dir+"alpha.txt")
        _H = np.loadtxt(_dir+"H.txt")
        _seeds = np.loadtxt(_dir+"seeds.txt")
        # Start clock for computation time estimates
        starttime = time.time()

        for i, H in enumerate(_H):
            # Allocate
            eta = np.zeros((len(_alpha), len(_seeds)))
            for j, alpha in enumerate(_alpha):
                for k, seed in enumerate(_seeds):
                    suffix = "_L{L}x{L}_K{K}_H{H:.2f}_f{f:.3f}_a{a:.3f}_seed{seed}".format(
                        L=args.L, K=args.K, f=args.f, H=H, a=alpha, seed=seed
                    )
                    _d = np.load(_dir+"travel_distance{s}.npy".format(suffix))
                    eta[j,k] = np.mean(_d / args.K)
            # Save
            save_suffix = "_L{L}x{L}_K{K}_H{H:.2f}_f{f:.3f}".format(
                L=args.L, K=args.K, f=args.f, H=H
            )
            np.save(_rdir+"search_efficiency{:s}".format(save_suffix), eta)

        # Print some time-related statements
        _time = time.time() - starttime
        print("Search efficiency computed after approx. time: {:.2f}s".format(_time))


if __name__ == "__main__":
    Argus = src.args.Args() 
    args = Argus.args 
    Annie = Analyze() 
    # Analyze
    Annie.compute_search_efficiency(args)

    