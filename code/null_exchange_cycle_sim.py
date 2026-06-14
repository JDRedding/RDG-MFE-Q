import numpy as np
from scipy.stats import entropy

# Discrete Null Exchange Cycle Simulation
# Parameters
N = 5  # number of visible states in X
total_mass = 20.0  # conserved total measure
mu_N = 0.0  # initial null mass
mu_X = np.array([4.0, 4.0, 4.0, 4.0, 4.0])  # uniform initial

print("Initial:")
print("mu_X:", mu_X)
print("mu_N:", mu_N)
print("Total:", np.sum(mu_X) + mu_N)

# Function to compute entropies
def compute_entropies(mu):
    # SID: effective support size (log of non-zero count, kB=1)
    support = np.sum(mu > 1e-6)
    S_SID = np.log(support) if support > 0 else 0
    # PED: Shannon entropy (natural log)
    probs = mu / (np.sum(mu) + 1e-12)
    S_PED = entropy(probs, base=np.e)
    return S_SID, S_PED

S_SID0, S_PED0 = compute_entropies(mu_X)
print("S_SID:", S_SID0, "S_PED:", S_PED0)

# Simulation loop
steps = 5
history = []

for t in range(steps):
    # === DISCARD PHASE (R_discard) ===
    # Simple discard: clip lowest 40% mass to null, or push from tail states
    sorted_idx = np.argsort(mu_X)
    discard_mass = 0.0
    for i in range(int(0.4 * N)):  # discard from lowest states
        idx = sorted_idx[i]
        discard_amount = 0.5 * mu_X[idx]
        mu_X[idx] -= discard_amount
        discard_mass += discard_amount
    mu_N += discard_mass
    
    # Compute post-discard
    S_SID_d, S_PED_d = compute_entropies(mu_X)
    R_disc = (S_SID0 - S_SID_d) + (S_PED0 - S_PED_d)  # rough combined
    
    # === INDUCTION PHASE (I_E) ===
    # Simple engine E: redistribute pulled mass uniformly or biased to first states
    pull_mass = min(0.6 * discard_mass, mu_N)  # not all, engine efficiency
    mu_N -= pull_mass
    # Bias: add more to lower index states (structure creation)
    bias = np.array([0.4, 0.3, 0.15, 0.1, 0.05])
    bias /= np.sum(bias)
    added = pull_mass * bias
    mu_X += added
    
    # Record
    S_SID, S_PED = compute_entropies(mu_X)
    history.append((mu_X.copy(), mu_N, S_SID, S_PED))
    
    print(f"\nStep {t+1}:")
    print("mu_X:", np.round(mu_X, 3))
    print("mu_N:", round(mu_N, 3))
    print("Total:", round(np.sum(mu_X) + mu_N, 3))
    print("S_SID:", round(S_SID, 3), "S_PED:", round(S_PED, 3))

# Final check
print("\nFinal Total:", np.sum(mu_X) + mu_N)