# A concrete toy model with N=5 visible microstates in X, 
# integer-friendly mass units (total conserved measure = 20),  
# and alternating Discard → Induction steps.

import numpy as np
from scipy.stats import entropy

# Setup
N = 5
total_mass = 20.0
mu_X = np.array([4.0, 4.0, 4.0, 4.0, 4.0], dtype=float)
mu_N = 0.0

def entropies(mu):
    supp = np.sum(mu > 1e-8)
    S_SID = np.log(supp) if supp > 0 else 0.0          # Boltzmann-like (kB=1)
    p = mu / (np.sum(mu) + 1e-12)
    S_PED = entropy(p, base=np.e)                      # Shannon (nats)
    return S_SID, S_PED