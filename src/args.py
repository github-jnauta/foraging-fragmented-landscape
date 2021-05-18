# Import necessary libraries
import argparse
import numpy as np 

class Args():
    """ Arguments """
    def __init__(self):
        parser = argparse.ArgumentParser("Specify specific variables")
        ## Landscape variables
        parser.add_argument(
            '--m', dest='maxlevel', type=int, default=8,
            help='maximum level of resolution as N=2**maxlevel'
        )
        parser.add_argument(
            '--sig', dest='sigma', type=float, default=1.,
            help='variance of the Gaussian distribution'
        )
        parser.add_argument(
            '--H', dest='H', type=float, default=0.5, help='Hurst exponent'
        )
        parser.add_argument(
            '--f', dest='f', type=float, default=0.1, help='fragmentation level'
        )
        ## Forager variables
        parser.add_argument(
            '--T', dest='T', type=int, default=10000, help='number of steps'
        )
        parser.add_argument(
            '--K', dest='K', type=int, default=10000, 
            help='number of resources to be encountered'
        )
        parser.add_argument(
            '--alpha', dest='alpha', type=float, default=2., 
            help='specify Levy parameter of the forager(s)'
        )
        ## Random number variables
        parser.add_argument(
            '--seed', dest='seed', type=int, default=1
        )
        ## Numerical variables
        parser.add_argument(
            '--reps', dest='reps', type=int, default=30,
            help='specify the number of repetitions per resource landscape'
        )
        ## Boolean variables
        parser.add_argument(
            '--save', dest='save', action='store_true',
            help='if included, saves the figure'
        )
        parser.add_argument(
            '--no-save', dest='save', action='store_false',
            help='if included, saves the figure'
        )
        parser.add_argument(
            '--compute', dest='compute', action='store_true', 
            help='if included, computed necessary quantities instead of loading them'
        )
        # Directory variables 
        parser.add_argument(
            '--ddir', dest='ddir', type=str, default='data/',
            help='specify directory for output data'
        )
        
        # Parse arguments
        self.args = parser.parse_args()