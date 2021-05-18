## Group foraging in fragmented landscapes 
This repository contains code for running foraging models in fragmented landscapes. The resource landscapes are generated using fractional Brownian motion (fBm), which is defined by a Hurst exponent _H_ and a fraction of coverage _f_. 

# Running the code
The main scripts for parallelization of the code on multiple _threads_ on single CPU, or via SSH on specified nodes, are availabile in the `bash/` directory.
Main running script `run_forage.py` requires 
- `numpy`
- `numba`
And plotting obviously requires `matplotlib`, and a valid LaTeX installation for captions, labels, etc.
