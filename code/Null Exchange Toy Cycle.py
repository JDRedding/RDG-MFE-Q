# ============================================================================
#  NULL EXCHANGE CYCLE — DISCRETE SIMULATION (N = 5)
#  --------------------------------------------------------------------------
#  This script implements a minimal, operator-faithful model of the
#  Null Exchange Cycle:
#
#      • R_discard : X → 𝓝   (clipping / discard flow)
#      • Induction I_E : 𝓝 → X (anti-clipping)
#      • Null Stratum 𝓝 : pre-geometric reservoir
#      • Global conservation:  μ_X + μ_𝓝 = constant
#      • SID / PED entropy tracking via SID_PED_Q
#
#  MODEL OVERVIEW
#  --------------------------------------------------------------------------
#  Visible space X has N = 5 microstates with an initial uniform measure.
#  At each step:
#
#      1. DISCARD PHASE (R_discard):
#         - Identify lowest-mass states.
#         - Clip a fraction of their mass.
#         - Shunt clipped mass into the null stratum 𝓝.
#
#      2. INDUCTION PHASE (I_E):
#         - Engine E pulls a fraction of null mass back into X.
#         - Re-encodes it with a bias toward low-index states.
#         - Creates visible structure (PED entropy decreases).
#
#  ENTROPY MEASURES
#  --------------------------------------------------------------------------
#      • S_SID : log of support size (Boltzmann-like)
#      • S_PED : Shannon entropy of μ_X
#
#  EXPECTED BEHAVIOR
#  --------------------------------------------------------------------------
#      • μ_𝓝 grows as discarded structure accumulates.
#      • μ_X becomes increasingly skewed (engine-driven emergence).
#      • S_PED decreases monotonically (visible ordering).
#      • S_SID remains constant unless states are zeroed.
#
#  This simulation is the discrete, integer-friendly demonstration of the
#  full Null Exchange Cycle: global conservation + visible irreversibility +
#  engine-driven structure formation.
#
# ============================================================================

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
