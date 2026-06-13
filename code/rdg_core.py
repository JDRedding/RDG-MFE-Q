# ============================================================
# CANONICAL RDG OPERATOR FLOW
# ============================================================
# 
# Γ(X_t)                 # accumulation via SID topology (+ PED flux if present)
# 
# Q[Γ(X_t)]              # admissibility test (manifold / curvature / flux bounds)

# if Q == 1:
#     X_{t+1} = Γ(X_t)   # admissible → keep accumulated state
# else:
#     X_{t+1} = σ(Γ(X_t))  # inadmissible → project onto admissible simplex
# 
# δ(X_t) = X_t - Γ(X_t)  # boundary / mismatch tracker (diagnostic; not fed back)
# 
# ============================================================

import numpy as np
from dataclasses import dataclass

@dataclass
class RDGState:
    x: np.ndarray          # field intensities on loci (must be non-negative)

@dataclass
class RDGParams:
    manifold_bound: float = 1.0   # global sum constraint for simplicity
    epsilon: float = 1e-8

def gamma_accumulate(state: RDGState, adj: np.ndarray) -> np.ndarray:
    """Γ-Operator: SID-based averaging (pure structural for minimal case)"""
    deg = adj.sum(axis=1, dtype=float)
    deg[deg == 0] = 1.0  # avoid div0
    # Each node averages itself + neighbors (weighted by topology)
    neigh_sum = adj @ state.x
    return (state.x + neigh_sum) / (1 + deg)

def q_admissible(gamma: np.ndarray, params: RDGParams) -> bool:
    """Q-Admissibility: check manifold bounds"""
    total = np.sum(gamma)
    return total <= params.manifold_bound + params.epsilon

def sigma_reconstruct(gamma: np.ndarray, params: RDGParams) -> np.ndarray:
    """σ-Projection: scale back onto simplex if violated"""
    total = np.sum(gamma)
    if total <= params.manifold_bound + params.epsilon:
        return gamma.copy()
    # Project onto simplex (scale to sum = bound)
    scale = params.manifold_bound / total
    return gamma * scale

def delta_boundary(state: RDGState, gamma: np.ndarray) -> np.ndarray:
    """δ-Boundary Engine: mismatch / gradient"""
    return state.x - gamma

def rdg_step(state: RDGState, adj: np.ndarray, params: RDGParams):
    """Full canonical RDG step"""
    gamma = gamma_accumulate(state, adj)
    if q_admissible(gamma, params):
        new_x = gamma
        q_flag = 1
    else:
        new_x = sigma_reconstruct(gamma, params)
        q_flag = 0
    
    delta = delta_boundary(state, gamma)
    
    return RDGState(x=new_x), {
        'gamma': gamma,
        'q': q_flag,
        'delta': delta,
        'total_before': np.sum(state.x),
        'total_after': np.sum(new_x)
    }

# === 2-Node Worked Example (matches your Pipeline.txt) ===
if __name__ == "__main__":
    # Fully connected 2-node
    adj = np.array([[0, 1], [1, 0]], dtype=float)
    
    x0 = np.array([0.8, 0.6])
    state = RDGState(x=x0)
    params = RDGParams(manifold_bound=1.0)
    
    print("Initial:", x0, "sum =", x0.sum())
    
    new_state, info = rdg_step(state, adj, params)
    print("Γ:", info['gamma'])
    print("Q:", info['q'])
    print("σ(X_{t+1}):", new_state.x)
    print("δ:", info['delta'])
