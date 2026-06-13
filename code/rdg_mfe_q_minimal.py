# ================================================================
# RDG–MFE–Q DISCRETE ENGINE (PYTHON TOY MODEL)
#
# This code implements a minimal discrete RDG–MFE–Q update cycle:
#   - rdg_update_geometry  → SID-driven Γ-geometry adjustment
#   - mfe_life_step        → PED/MFE field update (Life-like rule)
#   - q_filter             → Q-admissibility restoration (σ-like)
#   - rdg_mfe_q_step       → full Γ → Q → σ pipeline step
#
# For the full operator definitions and canonical update flow,
# refer to the main specification:
#
#     RDG-MFE-Q PIPELINE
#
# which defines Γ-accumulation, Q-admissibility, σ-projection,
# and δ-boundary extraction in the formal RDG operator framework.
# ================================================================

import numpy as np
from dataclasses import dataclass

@dataclass
class RDGState:
    adj: np.ndarray  # adjacency matrix (N x N)
    x: np.ndarray    # field/state on nodes (N,)

@dataclass
class RDGParams:
    target_degree: float = 3.0
    q_threshold: float = 0.5

def rdg_update_geometry(state: RDGState, params: RDGParams) -> np.ndarray:
    adj = state.adj.copy()
    deg = adj.sum(axis=1).astype(float)
    N = len(deg)
    for i in range(N):
        if deg[i] > params.target_degree + 0.5:
            # trim edges (simple example)
            neighbors = np.where(adj[i] == 1)[0]
            if len(neighbors) > 0:
                adj[i, neighbors[0]] = 0
                adj[neighbors[0], i] = 0
    return adj

def mfe_life_step(state: RDGState) -> np.ndarray:
    adj = state.adj
    x = state.x
    neigh_count = adj @ x
    survive = (x == 1) & ((neigh_count == 2) | (neigh_count == 3))
    born = (x == 0) & (neigh_count == 3)
    return np.where(survive | born, 1, 0).astype(int)

def q_filter(state: RDGState, params: RDGParams) -> RDGState:
    adj = state.adj.copy()
    x = state.x
    deg = adj.sum(axis=1).astype(float)
    mean_deg = deg.mean()
    lower = max(2, int(mean_deg * params.q_threshold))
    for i in range(len(deg)):
        if deg[i] < lower:
            candidates = np.where(adj[i] == 0)[0]
            np.random.shuffle(candidates)
            to_add = candidates[:int(lower - deg[i])]
            adj[i, to_add] = 1
            adj[to_add, i] = 1
    return RDGState(adj=adj, x=x)

def rdg_mfe_q_step(state: RDGState, params: RDGParams) -> RDGState:
    new_adj = rdg_update_geometry(state, params)
    new_x = mfe_life_step(RDGState(adj=new_adj, x=state.x))
    new_state = RDGState(adj=new_adj, x=new_x)
    return q_filter(new_state, params)

# Example: small graph
N = 10
adj = np.random.randint(0, 2, (N, N))
np.fill_diagonal(adj, 0)
adj = (adj + adj.T) // 2  # undirected
x = np.random.randint(0, 2, N)

state = RDGState(adj=adj, x=x)
params = RDGParams()

for t in range(5):
    state = rdg_mfe_q_step(state, params)
    print(f"Step {t}: active nodes = {state.x.sum()}")
