""" Holds modules for generating fractal landscapes using fractional Brownian motion
    Currently, the main function that generates an L x L landscape uses the 
    two-dimensional spectral synthesis from (Saupe, 1988, Algorithms for random fractals).
"""
# Import necessary libraries
import numpy as np 

class Landscape(object):
    def __init__(self):
        pass 

    def binary_lattice(self, lattice, f):
        """ Generate binary lattice from the continuous fraction Brownian motion lattice """
        shifted_lattice = lattice + abs(np.min(lattice))    # Shift
        sorted_lattice = np.sort(shifted_lattice.flatten()) # Sort 
        # Determine cutoff point
        cutoff = sorted_lattice[int((1-f)*lattice.shape[0]*lattice.shape[1])]
        # Generate binary lattice
        _lattice = shifted_lattice / cutoff                 # Normalize lattice
        _lattice[_lattice >= 1] = 1                         # All above cutoff to 1
        _lattice[_lattice < 1] = 0                          # All below to 0
        return np.asarray(_lattice, dtype=np.int64)

    def SpectralSynthesis2D(self, L, H, sig=1, bounds=[0,1]):
        """ Generate fractional Brownian in two dimensions """
        A = np.zeros((L,L), dtype=np.cdouble)
        for i in range(L//2):
            for j in range(L//2):
                phase = 2*np.pi*np.random.random()
                if i!=0 or j!=0:
                    r = (i*i+j*j)**(-(H+1)/2) * np.random.normal(0, sig)
                else:
                    r = 0 
                A[i,j] = r*np.cos(phase) + 1j*r*np.sin(phase)
                i0 = 0 if i == 0 else L-i 
                j0 = 0 if j == 0 else L-j 
                A[i0,j0] = r*np.cos(phase) + 1j*r*np.sin(phase)

        # @TODO: Why does one need to loop 'twice'
        # (but note different indices are assigned)
        # See also https://link.springer.com/content/pdf/10.1023/A:1008193015770.pdf 
        for i in range(1, L//2):
            for j in range(1, L//2):
                phase = 2*np.pi*np.random.random() 
                r = (i*i+j*j)**(-(H+1)/2) * np.random.normal(sig)
                A[i,L-j] = r*np.cos(phase) + 1j*r*np.sin(phase)
                A[L-i,j] = r*np.cos(phase) - 1j*r*np.sin(phase)
        
        X = np.real(np.fft.fft2(A))
        return X 
