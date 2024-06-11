import numpy as np
import math
import pandas as pd

midparental_iq = 0.3 #use z-score
pgs = 0.2 #use z-score

n_sim = 10 ** 4
epsilon = 0.1

def iq_to_z(iq):
    return (iq - 100) / 15

def z_to_iq(z):
    return 15 * z + 100

p1_g = (0.8**0.5) * np.random.normal(size=n_sim) # Var(p1_g) = 0.8 * Var(population)
p2_g = (0.8**0.5) * np.random.normal(size=n_sim)

p1_p = p1_g + (0.2**0.5) * np.random.normal(size=n_sim) # Var(p1_p) = Var(population)
p2_p = p2_g + (0.2**0.5) * np.random.normal(size=n_sim)
p_gmean = (p1_g + p2_g) / 2
p_pmean = (p1_p + p2_p) / 2

c_g = p_gmean + (0.4**0.5) * np.random.normal(size=n_sim) # Var(c_g) = 0.8 * Var(population)
c_p = c_g + (0.2**0.5) * np.random.normal(size=n_sim) # Var(c_p) = Var(population)

c_pgs = ((5**0.5) / 5) * c_g + (0.84 ** 0.5) * np.random.normal(size=n_sim) # Var(c_pgs) = Var(population)

mask_c_pgs = np.abs(c_pgs - pgs) < epsilon
mask_p_mean = np.abs(p_pmean - midparental_iq) < epsilon
mask_combined = mask_c_pgs & mask_p_mean

pheno_selected = c_p[mask_combined]
geno_selected = c_g[mask_combined]

data = np.column_stack((p1_g, p2_g, p1_p, p2_p, c_g, c_p, c_pgs, p_gmean, p_pmean))
df = pd.DataFrame(data, columns=['p1_g', 'p2_g', 'p1_p', 'p2_p', 'c_g', 'c_p', 'c_pgs', 'p_gmean', 'p_pmean'])

corr_matrix = df.corr()

print("IQ: " + "mean = " + str(z_to_iq(np.mean(pheno_selected)))," SD = " + str(15*np.std(pheno_selected))," n =",pheno_selected.shape[0])


# Correlations to check for errors
print(corr_matrix)
'''
print(corr_matrix)

print("p1_g: ", np.mean(p1_g), np.std(p1_g))
print("p2_g: ", np.mean(p2_g), np.std(p2_g))
print("p1_p: ", np.mean(p1_p), np.std(p1_p))
print("p2_p: ", np.mean(p2_p), np.std(p2_p))
print("c_g: ", np.mean(c_g), np.std(c_g))
print("c_p: ", np.mean(c_p), np.std(c_p))
print("c_pgs: ", np.mean(c_pgs), np.std(c_pgs))
'''



