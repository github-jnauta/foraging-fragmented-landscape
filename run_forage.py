""" Acts as a wrapper for running foraging scenarios in fractal landscapes 
    @TODO: Adapt description to updated model
"""
# Import necessary libraries
import numpy as np 
# Import modules 
import src.args 
import src.forage

if __name__ == "__main__":
    # Instantiate objects
    Argus = src.args.Args()
    args = Argus.args 

    System = src.forage.System()
    output = System.run_flight(args) 
    # Determine suffix for saving 
    suffix = "_L%(L)ixL%(L)i_K%(K)i_H%(H).3f_f%(f).3f_a%(alpha).3f"%(
        {
            'L': 2**args.maxlevel, 
            'K': args.K,
            'H': args.H,
            'f': args.f,
            'alpha': args.alpha
        }
    )
    # Save
    if args.save:
        for key, item in output.items():
            np.save(args.ddir+"%s%s"%(key, suffix), item)
    else:
        for key, item in output.items():
            print(key, item, np.mean(item))
