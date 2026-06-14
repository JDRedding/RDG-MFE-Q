# A concrete toy model with N=5 visible microstates in X, 
# integer-friendly mass units (total conserved measure = 20),  
# and alternating Discard → Induction steps.

# Simulation loop
steps = 5
history = []

for t in range(steps):

    # === DISCARD PHASE (R_discard) ===
    # Identify lowest-mass states (weakest distinctions)
    sorted_idx = np.argsort(mu_X)
    discard_mass = 0.0

    # Clip 40% of states (lowest 2 of 5)
    for i in range(int(0.4 * N)):
        idx = sorted_idx[i]
        clip = 0.5 * mu_X[idx]       # remove 50% of each weak state
        mu_X[idx] -= clip
        discard_mass += clip

    mu_N += discard_mass  # push clipped mass into null stratum

    # === INDUCTION PHASE (I_E) ===
    # Engine pulls 60% of discarded mass back from null
    pull = min(0.6 * discard_mass, mu_N)
    mu_N -= pull

    # Engine bias: favor lower-index states (structure creation)
    bias = np.array([0.40, 0.30, 0.15, 0.10, 0.05])
    bias /= np.sum(bias)

    mu_X += pull * bias

    # === ENTROPY MEASURES ===
    S_SID, S_PED = entropies(mu_X)
    history.append((mu_X.copy(), mu_N, S_SID, S_PED))

    print(f"\nStep {t+1}:")
    print("mu_X:", np.round(mu_X, 3))
    print("mu_N:", round(mu_N, 3))
    print("Total:", round(np.sum(mu_X) + mu_N, 3))
    print("S_SID:", round(S_SID, 3), "S_PED:", round(S_PED, 3))
