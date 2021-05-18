import numpy as np 
import numba 
import matplotlib.pyplot as plt 

# @numba.jit(nopython=True, cache=True)
def truncated_zipf(alpha, N):
    """ Compute the cumulative distribution function for the truncated
        discrete zeta distribution (Zipf's law)
    """
    x = np.arange(1, N+1)
    weights = x ** -alpha
    weights /= np.sum(weights)
    cdf = np.cumsum(weights)
    return cdf 

# @numba.jit(nopython=True, cache=True)
def sample(cdf):
    rand = np.random.random() 
    for i in range(len(cdf)):
        if rand < cdf[i]:
            return i + 1

N = 64 
a = 1.1
cdf = truncated_zipf(a, N)

samples = np.zeros(10000)
for i in range(len(samples)):
    samples[i] = sample(cdf)
print(samples)
plt.hist(samples, bins=np.arange(1,N+2), density=True)
plt.xlim(1,N)
plt.show()
