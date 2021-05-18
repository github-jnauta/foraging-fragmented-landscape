""" Visualize (plot) the different implementations of random searches """
# Import necessary libraries
import numpy as np 
import matplotlib.pyplot as plt 

def truncated_zipf(alpha, N):
    """ Compute the cumulative distribution function for the truncated
        discrete zeta distribution (Zipf's law)
    """
    x = np.arange(1, N+1)
    weights = x ** -alpha
    weights /= np.sum(weights)
    cdf = np.cumsum(weights)
    return cdf 

def sample(cdf):
    """ Generate sample from given (discrete) cdf """
    rand = np.random.random() 
    for i in range(len(cdf)):
        if rand < cdf[i]:
            return i + 1

L = 2**8
N = 100
directions = np.array([[1, 0], [0, 1], [-1,0], [0,-1]])

fig, ax = plt.subplots(1,1, figsize=(4,4), tight_layout=True)
alpha = [1.1, 2.0, 3.0]
colors = ['k', 'navy', 'firebrick']
for i, a in enumerate(alpha):
    cdf = truncated_zipf(a, N)
    x = np.zeros((N,2), dtype=int)
    x[0,:] = L//2
    for n in range(1,N):
        levy_dist = sample(cdf)
        direction = directions[np.random.randint(len(directions))]
        x[n,:] = ( x[n-1,:] + direction*levy_dist ) % L 

    ax.plot(
        x[:,0], x[:,1], color=colors[i]
    )
ax.set_xlim(0,L)
ax.set_ylim(0,L)
plt.show()