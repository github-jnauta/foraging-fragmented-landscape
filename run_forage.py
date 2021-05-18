""" Acts as a wrapper for running foraging scenarios in fractal landscapes 
    @TODO: Adapt description to updated model
"""
# Import necessary libraries
import time 
import numpy as np 
# Import modules 
import src.args 
import src.forage

if __name__ == "__main__":
    # Instantiate objects
    Argus = src.args.Args()
    args = Argus.args 
    # Start clock for computation time estimates
    starttime = time.time()
    # Initialize system
    System = src.forage.System()

    # Compute output
    output = System.run_flight(args) 

    # Save or print output
    printstr = "L%(L)ixL%(L)i, H=%(H).2f, f=%(f).2f, \u03B1=%(alpha).2f, K=%(K)i"%(
        Argus.argdict
    )
    seconds = time.time() - starttime
    minutes = seconds / 60 
    hours = minutes / 60 
    timestr = "%.4fs (%.2fmin) (%.2fhrs)"%(seconds, minutes, hours)
    print("Computations finished for %s\n approx. time: %s"%(printstr, timestr))
    if args.save:    
        # Determine suffix for saving 
        suffix = "_L%(L)ixL%(L)i_K%(K)i_H%(H).3f_f%(f).3f_a%(alpha).3f"%(Argus.argdict)
        for key, item in output.items():
            np.save(args.ddir+"%s%s"%(key, suffix), item)
    else:
        print("Output:")
        for key, item in output.items():
            print(key, item, np.mean(item))
