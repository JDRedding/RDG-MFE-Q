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
