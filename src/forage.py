""" Implements single forager in fractal landscape 
    @TODO: Adapt description to updated model
"""
# Import necessary libraries
import numpy as np 
import numba 
# Import modules 
import src.landscapes

###################
# Numba functions #
@numba.jit(nopython=True, cache=True)
def nb_set_seed(seed):
    np.random.seed(seed)
    
@numba.jit(nopython=True, cache=True)
def truncated_zipf(alpha, N):
    """ Compute the cumulative distribution function for the truncated
        discrete zeta distribution (Zipf's law)
    """
    x = np.arange(1, N+1)
    weights = x ** -alpha
    weights /= np.sum(weights)
    cdf = np.cumsum(weights)
    return cdf 

@numba.jit(nopython=True, cache=True)
def sample(cdf):
    """ Generate sample from given (discrete) cdf """
    rand = np.random.random() 
    for i in range(len(cdf)):
        if rand < cdf[i]:
            return i + 1

@numba.jit(nopython=True, cache=True)
def nb_forage_Levy_flight(K, landscape, alpha, reps, xmin=1):
    """ Forage within the resource landscape until detection of K resources 
        The forager executes a Levy flight with parameter α, wherein displacements
        on the landscape lattice are discrete
        Landscape boundaries are periodic
    """
    L, _ = landscape.shape 
    directions = np.array([[1, 0], [0, 1], [-1,0], [0,-1]], dtype=np.int64)
    # Compute cdf for Zipf's law as the discrete power law distribution
    _cdf = truncated_zipf(alpha, L)
    # Allocate space for storing
    distances = np.zeros(reps, dtype=np.float64)

    ## Run the Levy flight foraging
    #! @NOTE: Repeats reps times, as landscape creating is (relatively) expensive
    for rep in range(reps):
        # Initialize forager position
        x = np.array([np.random.randint(L),np.random.randint(L)])
        # Initialize random walk variables
        levy_steps = 0 
        current_steps = 0
        # Initialize measures
        number_detected = 0
        travel_distance = 0. 
        while number_detected < K:
            # Sample a Levy flight
            if current_steps == 0:
                levy_steps = sample(_cdf)
                direction = directions[np.random.randint(0,len(directions))]
            # Update position
            x[0] = ( x[0] + direction[0] ) % L 
            x[1] = ( x[1] + direction[1] ) % L
            # Increment distance measures
            travel_distance += 1.
            current_steps += 1
            current_steps = 0 if current_steps >= levy_steps else current_steps
            # Check if there is a resource at the current site 
            if landscape[x[0], x[1]]:
                number_detected += 1
                # Truncate current flight at resource detection
                current_steps = 0
                
        distances[rep] = travel_distance
    return distances, number_detected


#################
# Class wrapper #
class System(object):
    def __init__(self):
        pass 

    def run_flight(self, args):
        """ Execute Levy flight foraging in fractal landscape """
        # Seed the RNG
        np.random.seed(args.seed)
        nb_set_seed(args.seed)
        # Instantiate necessary objects
        landscapes = src.landscapes.Landscape()
        # Generate the landscape
        L = 2**args.maxlevel 
        lattice = landscapes.SpectralSynthesis2D(L, args.H)
        landscape = landscapes.binary_lattice(lattice, args.f)
        print("Generated landscape, running foraging...")
        # Run 
        output = nb_forage_Levy_flight(args.K, landscape, args.alpha, args.reps)
        # Return output as dictionary
        out = {}
        out['travel_distance'] = output[0]
        return out 