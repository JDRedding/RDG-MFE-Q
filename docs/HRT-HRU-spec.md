# HRT / HRU Specification

> **MFERDGQ Framework** · Formal Architecture Document  
> Status: Draft · Layer: Core Engine

---

## HRT — Historical Relational Theory (the cone)

HRT defines the full relational universe: geometry, history, and constraints.

```
HRT = (RDG, SID, PED, RED, p, P, A)
```

### Structure

| Element | Role |
|---|---|
| **Apex (Q-forcing)** | Invariant generator point; source of admissibility and constraint |
| **SID-face** | Structure |
| **PED-face** | Evaluation |
| **RED-face** | Dynamics |

### Historical Triad (extracted by H)

| Symbol | Meaning |
|---|---|
| `p` | Present slice |
| `P` | Accumulated past |
| `A` | Attractor trajectory |

---

## HRU — Historical Relational Update (the engine inside the cone)

HRU is the motor that advances the effective state forward through the cone.

```
HRU = Ω Λ Q H Γ Σ Π_Q G
```

**Update law:**

```
S_eff(next) = HRU(S_eff(now))
```

### The 8-Operator Cycle

| # | Operator | Name | Action |
|---|---|---|---|
| 1 | **G** | Generative geometry | `∅ → 𝒮` · Produces the full relational phase space |
| 2 | **Π_Q** | Q-projection | `𝒮 → 𝒮_Q ⊆ 𝒮` · Restricts to structurally admissible states |
| 3 | **Σ** | Structural summation | `𝒫(𝒮_Q) → SID` · Assembles admissible fragments into coherent structures |
| 4 | **Γ** | Relational lift | `SID → RDG` · Lifts structure into explicit relational (graph) form |
| 5 | **H** | Historical operator | `RDG → (p, P, A)` · Extracts present, past record, and attractor |
| 6 | **Q** | Admissible slicing | `(p, P, A) → ℱ_adm` · Restricts futures that don't break history |
| 7 | **Λ** | Re-embedding | `ℱ_adm → 𝒮′_Q` · Writes filtered future back into the geometric substrate |
| 8 | **Ω** | Closure / seal | `𝒮′_Q → 𝒮_eff` · Commits the new state as the baseline for the next cycle |

### Full Loop

```
G → Π_Q → 𝒮_Q → Σ → SID → Γ → RDG → H → (p,P,A) → Q → ℱ_adm → Λ → 𝒮′_Q → Ω → 𝒮_eff
```

One traversal of this loop = one historical update of reality.

---

## HRT over HRU — Conical Relationship

| Layer | Provides |
|---|---|
| **HRT** | Cone geometry · SID/PED/RED faces · Historical triad (p, P, A) · Admissibility constraints |
| **HRU** | 8-step generative cycle · New effective state S_eff |

### Conical Structure

```
         apex = Q-forcing
        /     |     \
  SID-face  PED-face  RED-face
        \     |     /
       interior = HRU cycle
             |
          base = S_eff
```

**Unified interpretation:**

- **HRT** = the space and rules of historical reality
- **HRU** = the engine that moves reality forward

---

## Operator Reference

### 1. G — Generative Geometry

- **Role:** Raw substrate of "what can exist" before history or choice
- **Interpretation:** The full relational phase space
- **Action:** `G : ∅ → 𝒮`

Does not pick states; generates the space of possible structures.

---

### 2. Π_Q — Q-Projection (Restriction)

- **Role:** Cuts down the raw space to what is structurally admissible
- **Interpretation:** Enforces basic relational rules
- **Action:** `Π_Q : 𝒮 → 𝒮_Q ⊆ 𝒮`

After Π_Q, the state is in Q-legal geometry.

---

### 3. Σ — Structural Summation

- **Role:** Assembles admissible pieces into coherent structures (SIDs, patterns)
- **Interpretation:** Builds "objects" from allowed relations
- **Action:** `Σ : 𝒫(𝒮_Q) → SID`

Sums compatible fragments into a stable relational unit.

---

### 4. Γ — Relational Lift

- **Role:** Lifts a structural object into explicit relational form (RDG-style)
- **Interpretation:** Turns "shape" into "graph of relations"
- **Action:** `Γ : SID → RDG`

Produces nodes, edges, weights — a structure dynamics can run on.

---

### 5. H — Historical Operator

- **Role:** Extracts and updates history: moment, memory, attractor
- **Interpretation:** "Given what has actually happened…"
- **Action:** `H : RDG → (p, P, A)`

Where `p` = present state, `P` = past record, `A` = attractor/trajectory.

---

### 6. Q — Admissible Slicing (Historical)

- **Role:** Uses history to restrict which futures are allowed
- **Interpretation:** "Given (p, P, A), which branches are still legal?"
- **Action:** `Q : (p, P, A) → ℱ_adm`

Produces the HRM admissible set — futures that do not break history.

---

### 7. Λ — Re-Embedding

- **Role:** Pushes the historically-filtered structure back into the field/engine
- **Interpretation:** Writes the updated relational state back into MFE/FM/etc.
- **Action:** `Λ : ℱ_adm → 𝒮′_Q`

Re-embeds the chosen/filtered future into the geometric substrate.

---

### 8. Ω — Closure / Seal

- **Role:** Closes the cycle to prevent drift or regression
- **Interpretation:** The "commit" operation — this is now the new baseline reality
- **Action:** `Ω : 𝒮′_Q → 𝒮_eff`

After Ω, the updated structure becomes the new effective G-space input for the next cycle.

---

*Part of the MFERDGQ framework. See also: `RDG-MFE-Q-core-engine.md`, `CFM-operators.md`*
