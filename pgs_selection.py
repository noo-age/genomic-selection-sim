import numpy as np
from matplotlib import pyplot as plt

pop_SD = 15
sibship_SD = pop_SD / (2**(1/2)) #within-family SD is sqrt(2)/2 of population SD, minus assortive mating
sim_iters = 10**4

pgs_r = 0.4
embryo_count = 10

def generate_correlated_normals(n, r):
    # Ensure r is within the valid range for correlation coefficients
    if not -1 <= r <= 1:
        raise ValueError("Correlation coefficient must be between -1 and 1")

    # Constructing the covariance matrix based on the specified correlation coefficient
    cov_matrix = [[1, r], [r, 1]]
    
    # Generating samples from a multivariate normal distribution
    samples = np.random.multivariate_normal(mean=[0, 0], cov=cov_matrix, size=n)
    
    return samples

def es_gain(pop_SD,pgs_r,embryo_count,sim_iters=10**4):
    arr = np.zeros(sim_iters)
    for i in range(sim_iters):
        normals = generate_correlated_normals(embryo_count,pgs_r)
        embryos = normals[:,0] * pop_SD/(2**(1/2))
        embryos_pgs = normals[:,1]
        embryos_mean = np.mean(embryos)
        gain = embryos[np.argmax(embryos_pgs)] - embryos_mean
        arr[i] = gain
    return np.mean(arr),np.std(arr)

pgs_r_range = range(0,10,1)
embryo_count_range = range(2,30,1)

'''
for e in embryo_count_range:
    for p in pgs_r_range:
        print("embryos " + str(e) + ", pgs_r " + str(p/10) + ", " + "gain: " + str(es_gain(pop_SD,p/10,e,sim_iters=10**3)))
'''

print(es_gain(pop_SD,pgs_r,embryo_count,sim_iters=10**4))
