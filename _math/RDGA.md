# RDGA — Relational Dynamic Geometry Algebra

> RDGA is the algebraic backbone of RDG: it turns **relational geometry** into **operator‑grade algebra** that can feed MFE (fields) and Q (admissibility/quantization).

---

## 1. Purpose and scope

**Goal:** Provide a clean, minimal, operator‑centric algebra for:

- **Relational geometry:** incidence, parallelism, orthogonality, tangency, etc.
- **Relational operators:** union, intersection, complement, projection, composition.
- **Algebraic carriers:** polynomial systems, ideals, elimination structures.
- **Dynamic updates:** dependency‑graph propagation under motion of primitives.

RDGA is **relational‑first**: geometry is expressed as **constraints on tuples of objects**, then encoded algebraically.

---

## 2. Modes and layers

RDGA is designed to sit in the RDG → MFE → Q stack:

- **S‑mode (Structural):** geometric/relational primitives and constraints.
- **I‑mode (Index/Inference):** operators on relations (union, intersection, composition, etc.).
- **D‑mode (Data/Domain):** algebraic carriers (polynomials, ideals, elimination).
- **Γ‑mode (Update):** dynamic propagation of changes through dependency graphs.
- **Q‑mode (Qualifying/Quantizing):** admissibility, consistency, and (later) quantization rules.

This file focuses on **S/I/D/Γ**, and ends with hooks into **MFE** and **Q**.

---

## 3. Relational primitives (S‑mode)

### 3.1 Objects

We treat geometric entities as **relational knots**, not as bare coordinates:

- `Point(P)`
- `Line(L)`
- `Circle(C)`
- `Conic(K)`
- `Transform(T)` (isometries, similarities, projective maps, etc.)

Each object has an underlying coordinate representation, but RDGA keeps that **behind** the relational interface.

### 3.2 Relations

A relation is a subset of admissible tuples:



\[
R \subseteq \text{Obj}^n
\]



Examples:

- `Inc(P,L)` — point lies on line.
- `On(P,C)` — point lies on circle.
- `Par(L1,L2)` — lines are parallel.
- `Ort(L1,L2)` — lines are orthogonal.
- `Tan(C,L)` — circle tangent to line.
- `Map(T,X,Y)` — transform `T` sends `X` to `Y`.

Each such relation will have an **algebraic carrier** (Section 5).

---

## 4. Relational operators (I‑mode)

Relational operators act on sets of tuples. They are defined abstractly here, then given algebraic liftings in Section 5.

Let \( R, S \subseteq \text{Obj}^n \).

### 4.1 Union



\[
R \cup S = \{ x \mid x \in R \ \text{or} \ x \in S \}
\]



### 4.2 Intersection



\[
R \cap S = \{ x \mid x \in R \ \text{and} \ x \in S \}
\]



### 4.3 Complement



\[
\neg R = \{ x \mid x \notin R \}
\]



### 4.4 Projection

For \( R \subseteq \text{Obj}^n \), projection onto coordinate \( i \):



\[
\pi_i(R) = \{ x_i \mid (x_1,\dots,x_n) \in R \}
\]



### 4.5 Composition

For \( R \subseteq X \times Y \), \( S \subseteq Y \times Z \):



\[
R \circ S = \{ (x,z) \mid \exists y : (x,y)\in R \ \wedge \ (y,z)\in S \}
\]



---

## 5. Algebraic carriers (D‑mode)

### Solution‑Set Notation

For any relation \( R \) with algebraic carrier \( I_R \), we define its solution set as:



\[
\mathcal{S}(R) = \{ x \mid x \text{ satisfies all polynomials in } I_R \}
\]



or equivalently:



\[
\mathcal{S}(I_R) = \{ x \mid f(x) = 0 \ \forall f \in I_R \}.
\]



This object is used by both MFE (fields defined on solution sets) and Q‑layer (admissibility checks).


Each relation \( R \) is mapped to an algebraic carrier:



\[
\Phi : R \mapsto I_R \subseteq \mathbb{R}[x_1,\dots,x_n]
\]



where:

- \( I_R \) is an ideal (or more generally, a set of polynomial constraints).
- Solutions of \( I_R \) correspond to admissible configurations in \( R \).

### 5.1 Basic examples

Let coordinates be:

- Point \( P = (x_P, y_P) \)
- Points \( A = (x_A, y_A), B = (x_B, y_B) \)
- Line \( L = \overline{AB} \)
- Circle center \( O = (x_O, y_O) \), radius \( r \)

**Incidence** `Inc(P,L)`:



\[
I_{\text{Inc}} = \left\{ (y_P - y_A)(x_B - x_A) - (y_B - y_A)(x_P - x_A) \right\}
\]



**Circle membership** `On(P,C)`:



\[
I_{\text{Circ}} = \left\{ (x_P - x_O)^2 + (y_P - y_O)^2 - r^2 \right\}
\]



**Intersection** of line and circle (point(s) \( P \)):



\[
I_P = I_{\text{Inc}} + I_{\text{Circ}}
\]



Solutions of \( I_P \) give the intersection points.

### 5.2 Operator lifting

Given \( R, S \) with carriers \( I_R, I_S \):

- **Intersection:**
  

\[
  \Phi(R \cap S) = I_R + I_S
  \]


- **Union:**
  

\[
  \Phi(R \cup S) = I_R \cap I_S
  \]


- **Composition** (eliminate intermediate variables \( y \)):
  

\[
  \Phi(R \circ S) = \text{Elim}_y(I_R + I_S)
  \]


- **Projection** onto a subset of variables:
  

\[
  \Phi(\pi_i(R)) = \text{Elim}_{\text{all but } i}(I_R)
  \]



Implementation detail (symbolic): Gröbner bases or other elimination methods.

---

### Closure Under Operator Lifting

RDGA requires that the carrier mapping \( \Phi \) is closed under all relational operators:



\[
\Phi(R \ \text{op} \ S) = \Phi(R) \ \widehat{\text{op}} \ \Phi(S)
\]



where \( \widehat{\text{op}} \) is the corresponding algebraic operator:

- intersection → ideal sum  
- union → ideal intersection  
- composition → elimination  
- projection → elimination  

This closure property is what makes RDGA an operator algebra rather than a symbolic geometry layer.


## 6. Dynamic update (Γ‑mode)

RDGA becomes dynamic when tied to an update operator:



\[
\Gamma : \text{State}_t \to \text{State}_{t+1}
\]



A **state** includes:

- Primitive objects (with current coordinates/parameters).
- Relations among them.
- Algebraic carriers for each relation.
- Dependency graph describing how objects/relations depend on others.

### 6.1 Dependency graph

- **Nodes:** objects and relations.
- **Edges:** “depends on” (e.g., `L` depends on `A,B`; `P` depends on `L,C`).

When a primitive changes (e.g., dragging `A`):

1. Update coordinates of `A`.
2. Recompute any derived objects depending on `A` (e.g., `L`).
3. Recompute carriers \( I_R \) for affected relations.
4. Re‑solve affected systems (e.g., intersection points).
5. Push updates to any attached fields (MFE) and admissibility checks (Q).


### RDGA Invariants

RDGA maintains several invariants across updates:

1. **Ideal Dimension:**  
   The dimension of \( I_R \) must match the expected geometric dimension unless degeneracy is allowed.

2. **Rank Conditions:**  
   Jacobian rank must be sufficient to define a well‑posed locus.

3. **Structural Invariants:**  
   Relations preserve their arity and tuple structure.

4. **Coordinate‑Free Invariants:**  
   Incidence, parallelism, orthogonality, and tangency remain invariant under admissible transforms.

These invariants are checked during Γ‑updates and Q‑layer evaluation.


---

## 7. ASCII operator tables

### 7.1 Logical/relational operators

```text
+-----------------+---------------------------+-------------------------------+
| Operator        | Set-theoretic definition | Algebraic carrier (Φ)         |
+-----------------+---------------------------+-------------------------------+
| R ∩ S           | { x | x∈R ∧ x∈S }        | I_R + I_S                     |
| R ∪ S           | { x | x∈R ∨ x∈S }        | I_R ∩ I_S                     |
| ¬R              | { x | x∉R }              | (complement of solution set)  |
| π_i(R)          | projection on coord i    | Elim_{others}(I_R)            |
| R ∘ S           | relational composition   | Elim_y(I_R + I_S)             |
+-----------------+---------------------------+-------------------------------+
```

### 7.2 Common geometric relations

```text
+----------------+---------------------------+-----------------------------------------------+
| Relation       | Tuple type                | Example algebraic carrier                     |
+----------------+---------------------------+-----------------------------------------------+
| Inc(P,L)       | (Point, Line)            | line equation satisfied by P                   |
| On(P,C)        | (Point, Circle)          | (xP-xO)^2 + (yP-yO)^2 - r^2 = 0                |
| Par(L1,L2)     | (Line, Line)             | direction(L1) × direction(L2) = 0              |
| Ort(L1,L2)     | (Line, Line)             | direction(L1) · direction(L2) = 0              |
| Tan(C,L)       | (Circle, Line)           | distance(center(C), L) - r = 0                 |
| Map(T,X,Y)     | (Transform, Obj, Obj)    | coordinates(Y) - T(coordinates(X)) = 0         |
+----------------+---------------------------+-----------------------------------------------+
```

---

## 8. RDGA → MFE mapping (fields on relational carriers)

MFE (Metric/Field Engine) attaches **fields** to the **solution sets** of RDGA carriers.

### 8.1 Conceptual mapping

- RDGA gives:  
  \[
  I_R \subseteq \mathbb{R}[x_1,\dots,x_n]
  \]
  whose solution set \( \mathcal{S}_R \) is a geometric locus or configuration space.

- MFE defines fields on \( \mathcal{S}_R \):
  - Scalar fields: \( \phi : \mathcal{S}_R \to \mathbb{R} \)
  - Vector fields: \( \mathbf{F} : \mathcal{S}_R \to T\mathcal{S}_R \)
  - Tensor fields: etc.

### 8.2 Attachment rule

Given a relation \( R \) with carrier \( I_R \):

1. Compute (or represent) its solution set \( \mathcal{S}_R \).
2. Define field(s) restricted to \( \mathcal{S}_R \):
   - Example: a potential field along a line, or a flow along a curve.
3. When RDGA updates \( I_R \) (due to motion), MFE:
   - Updates the domain \( \mathcal{S}_R \).
   - Re‑expresses fields in the new coordinates/geometry.

### 8.3 Examples

- **Field along a line:**  
  `Inc(P,L)` defines a line locus; MFE attaches a 1D field \( \phi(s) \) along the line parameter \( s \).

- **Field on intersection curve:**  
  `R = R_1 ∩ R_2` with carrier \( I_R = I_{R_1} + I_{R_2} \); MFE attaches a field to the intersection locus (e.g., a flow along a circle‑line intersection).

### Example: Relational Composition

Let:

- \( R = \text{Inc}(A,L) \subseteq \text{Point} \times \text{Line} \)
- \( S = \text{Inc}(L,B) \subseteq \text{Line} \times \text{Point} \)

Then the composition:



\[
R \circ S \subseteq \text{Point} \times \text{Point}
\]



represents all pairs of points \( (A,B) \) that lie on a common line.

Algebraically:



\[
I_{R \circ S} = \text{Elim}_L(I_R + I_S)
\]



which eliminates the line parameters and yields the condition that \( A \) and \( B \) are collinear.


- **Transform‑induced fields:**  
  `Map(T,X,Y)` defines how fields are pushed forward or pulled back via `T`.

  ### Transform Algebra

Transforms form an algebra with:

- composition: \( T_3 = T_2 \circ T_1 \)
- identity: \( \mathrm{Id} \)
- inverse (when defined): \( T^{-1} \)

The carrier for a transform relation:



\[
\text{Map}(T,X,Y)
\]



is:



\[
I_{\text{Map}} = \{ Y - T(X) = 0 \}.
\]



Transform composition lifts to carriers via substitution and elimination.  
Transforms also propagate through dependency graphs and push/pull MFE fields.


---

## 9. RDGA → Q admissibility rules

Q‑layer enforces **admissibility** and, later, **quantization** on top of RDGA+MFE.

### 9.1 Admissibility types

1. **Geometric consistency:**
   - No contradictory constraints (e.g., over‑constrained systems with no real solutions).
   - Non‑degeneracy conditions (e.g., distinct points where required, non‑zero radius, etc.).

2. **Topological/structural consistency:**
   - Correct dimensionality of solution sets (e.g., expecting a curve vs. a discrete set).
   - Avoiding pathological configurations unless explicitly allowed.

3. **Field compatibility:**
   - Fields defined by MFE must be well‑posed on \( \mathcal{S}_R \) (no undefined singularities unless flagged).

### Dimensionality Expectations

For each relation \( R \), RDGA assigns an expected geometric dimension \( \dim_{\text{exp}}(R) \).

Examples:
- A point: 0‑dimensional  
- A line: 1‑dimensional  
- A circle: 1‑dimensional  
- Intersection of two curves: 0‑dimensional (typically discrete)

The actual dimension of the carrier ideal \( I_R \) is:



\[
\dim(I_R) = \text{Krull dimension of } \mathbb{R}[x]/I_R.
\]



Q‑layer compares:



\[
\dim(I_R) \quad \text{vs.} \quad \dim_{\text{exp}}(R)
\]



to detect degeneracy or over‑constraint.


### 9.2 Q‑rules over RDGA

Let \( I_R \) be a carrier and \( \mathcal{S}_R \) its solution set.

**Q1 — Existence:**

- Require \( \mathcal{S}_R \neq \emptyset \) unless the relation is explicitly allowed to be empty.
- If empty, mark relation as **inadmissible** or **void**.

**Q2 — Dimensionality:**

- Expected dimension \( \dim_{\text{exp}}(R) \) vs. actual dimension \( \dim(\mathcal{S}_R) \).
- If mismatch is not allowed (e.g., expecting a point but getting a line), mark as inadmissible or degenerate.

**Q3 — Non‑degeneracy:**

- Enforce inequalities (e.g., \( r > 0 \), \( A \neq B \)) as part of admissibility.
- These are not polynomial equalities, but can be tracked as side‑constraints.

**Q4 — Field regularity:**

- For fields \( \phi, \mathbf{F} \) attached via MFE:
  - Check for forbidden singularities or discontinuities on \( \mathcal{S}_R \).
  - If present and not allowed, mark configuration as inadmissible.

### Inequalities and Side‑Constraints

Not all geometric constraints are polynomial equalities. RDGA tracks non‑degeneracy conditions as side‑constraints:

- \( r > 0 \) (circle radius)  
- \( A \neq B \) (line defined by two distinct points)  
- direction vectors nonzero  
- determinant ≠ 0 (invertible transforms)

These are stored separately from the ideal \( I_R \) and evaluated during Q‑layer admissibility checks.


### 9.3 Q‑flags

Q‑layer can annotate each relation \( R \) with flags:

```text
Q_OK        : admissible, non-degenerate
Q_EMPTY     : no real solutions
Q_DEGEN     : degenerate (dimension mismatch, collapsed geometry)
Q_SINGULAR  : field singularities present
Q_UNCHECKED : not yet evaluated
```

These flags feed back into higher‑level logic (e.g., simulation, search, or optimization).

---

## 10. Minimal example: line–circle intersection with fields and Q

1. **RDGA (S/I/D):**
   - Relations: `Inc(P,L)`, `On(P,C)`
   - Carrier: \( I_P = I_{\text{Inc}} + I_{\text{Circ}} \)
   - Solutions: intersection points \( \{P_1, P_2\} \) (or fewer in degenerate cases).

2. **MFE:**
   - Attach a scalar field \( \phi(P) \) (e.g., potential) defined at each intersection point.
   - As `A` or `O` moves, \( I_P \) changes, and so do the positions of \( P_1, P_2 \) and the field values.

3. **Q:**
   - Check if \( I_P \) has real solutions:
     - If none: `Q_EMPTY`.
   - Check if the intersection is tangential (double root):
     - If tangency is allowed: `Q_OK` with a `DEGEN` note.
     - If not: `Q_DEGEN`.
   - Check field regularity at \( P_i \):
     - If singular: `Q_SINGULAR`.

---


## 11. Implementation Notes

RDGA is **symbolic-friendly** but does not mandate a specific CAS.  
Gröbner bases, resultants, triangular sets, or numeric solvers with symbolic wrappers are all acceptable.

The key contract between layers:

- **RDG** provides relational structure and dependency graphs.  
- **RDGA** provides algebraic carriers and operator lifting.  
- **MFE** attaches and evolves fields on solution sets.  
- **Q** evaluates admissibility and flags configurations.

The following examples illustrate RDGA carriers, operator lifting, elimination, Q‑checks, and Γ‑mode propagation in a minimal CAS‑agnostic way.

### Representation Note

In the code examples below, carriers are represented as Python **lists of polynomials**:

```python
I_Inc = [poly1]
I_On  = [poly2]
```

**Conceptually**, RDGA treats these lists as **generators of ideals** in  
$\mathbb{R}[x_1,\dots,x_n]$.  
The list representation is simply a convenient CAS-friendly encoding. All operator liftings (sum, intersection, elimination) are performed at the ideal level.

---

### Minimal SymPy Demonstration

```python
import sympy as sp
from sympy import groebner, resultant, symbols
import networkx as nx
from itertools import chain

# ===================================================================
# 1. Variables & Object Representations
# ===================================================================
xA, yA, xB, yB = symbols('xA yA xB yB', real=True)   # Line AB
xP, yP         = symbols('xP yP', real=True)          # Point P
xO, yO, r      = symbols('xO yO r', real=True)        # Circle

# ===================================================================
# 2. Relational Carriers (D-mode)
# ===================================================================

def carrier_Inc_P_Line(P_vars, A_vars, B_vars):
    """Inc(P, Line(AB))"""
    xP, yP = P_vars
    xA, yA = A_vars
    xB, yB = B_vars
    return [(yP - yA)*(xB - xA) - (yB - yA)*(xP - xA)]

def carrier_On_P_Circle(P_vars, O_vars, r):
    """On(P, Circle(O,r))"""
    xP, yP = P_vars
    xO, yO = O_vars
    return [(xP - xO)**2 + (yP - yO)**2 - r**2]

def carrier_Collinear(A_vars, B_vars, P_vars):
    """Collinear(A, B, P)"""
    xA, yA = A_vars
    xB, yB = B_vars
    xP, yP = P_vars
    return [xA*(yB - yP) + xB*(yP - yA) + xP*(yA - yB)]

# Instantiate
I_Inc = carrier_Inc_P_Line((xP, yP), (xA, yA), (xB, yB))
I_On  = carrier_On_P_Circle((xP, yP), (xO, yO), r)
I_Col = carrier_Collinear((xA, yA), (xB, yB), (xP, yP))

print("I_Inc :", I_Inc[0])
print("I_On  :", I_On[0])
print("I_Col :", I_Col[0])
```

### Operator Lifting Examples

```python
# -------------------------------------------------------------------
# Intersection: R ∩ S  →  I_R + I_S
# -------------------------------------------------------------------
I_inter = I_Inc + I_On                     # line–circle intersection

# -------------------------------------------------------------------
# Composition & Elimination
# -------------------------------------------------------------------
def eliminate(polys, vars_to_elim):
    """Groebner-based elimination"""
    G = groebner(polys, *vars_to_elim, domain=sp.RR, order='lex')
    return [p for p in G if not any(v in p.free_symbols for v in vars_to_elim)]

# Eliminate P → condition on remaining variables
collinear_via_P = eliminate(I_Inc + I_Col, [xP, yP])

# -------------------------------------------------------------------
# Projection example
# -------------------------------------------------------------------
proj_P = eliminate(I_Inc, [xA, yA, xB, yB])   # should leave no constraint on P
```

### Basic Q-Layer Checks (Γ-mode ready)

```python
def quick_q_check(I, expected_dim, vars_list):
    """Lightweight dimensionality check"""
    try:
        G = groebner(I, *vars_list, domain=sp.RR)
        rank_est = len([p for p in G if p != 0])
        dim_est = len(vars_list) - rank_est
        status = "Q_OK" if dim_est == expected_dim else "Q_DEGEN"
        return status, dim_est, expected_dim
    except:
        return "Q_UNCHECKED", -1, expected_dim

vars_P = [xP, yP]

print("\nQ-check line-circle intersection (expect 0-dim):",
      quick_q_check(I_inter, 0, vars_P))

print("Q-check collinearity (expect 1-dim curve):",
      quick_q_check(I_Col, 1, vars_P))
```

### Dependency Graph Skeleton (Γ-mode)
Note: The dependency graph encodes structural propagation only. Numerical solving, field updates (MFE), and admissibility checks (Q) occur after graph‑driven recomputation of carriers.


```python
G = nx.DiGraph()

# Nodes
G.add_node("A", type="Point")
G.add_node("B", type="Point")
G.add_node("P", type="Point")
G.add_node("Line_AB", type="Line")
G.add_node("Circle_O", type="Circle")
G.add_node("Rel_Inc", type="Relation", carrier=I_Inc)
G.add_node("Rel_On",  type="Relation", carrier=I_On)

# Edges
G.add_edges_from([("A", "Line_AB"), ("B", "Line_AB"),
                  ("Line_AB", "Rel_Inc"), ("P", "Rel_Inc"),
                  ("Circle_O", "Rel_On"), ("P", "Rel_On")])

print("Dependency graph ready for propagation.")
```
This demonstration shows the RDGA concepts in isolation; a full engine integrates these components with RDG’s structural layer, MFE’s field evolution, and Q‑layer admissibility.
