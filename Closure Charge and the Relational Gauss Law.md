# Closure Charge and the Relational Gauss Law

**Abstract.**  
We present a fully generalized formulation of the closure charge

$$
Q = \sum_{c \in \mathcal{C}} \Bigl( \bigotimes_{i=1}^{n} R_i \Bigr)_c,
$$

where the sum runs exclusively over admissible closures. This expression defines a universal closure invariant: a measure of the net relational content that remains after all internal cancellations permitted by the closure have occurred. We show that the invariant inherits the algebraic structure of its constituent densities, is conserved under continuous deformations that preserve the closure class, and stands in duality with curvature (or more generally with any relational defect). Scale dependence appears only in the density of the invariant, not in its total value. Familiar gauge, topological, geometric, and informational charges are recovered as special cases.

---

## 1. Generalized Definition

A more abstract and fully generalized version of the closure charge is

$$
Q = \sum_{c \in \mathcal{C}} \Bigl( \bigotimes_{i=1}^{n} R_i \Bigr)_c,
$$

where

- $\mathcal{C}$ is the set of admissible closures (loops, surfaces, processes, histories, equivalence classes, or completed relational structures),
- $R_i$ are relational densities, fields, operators, or invariants,
- $\otimes$ denotes whatever composition law preserves the relational structure (tensor product, contraction, exterior product, categorical product, convolution, etc.),
- the sum is taken only over completed closures.

This defines a **closure invariant** $Q$: a measure of the net relational content remaining after all internal cancellations permitted by the closure have occurred.

The original special case

$$
Q = \sum (\mathrm{SID} \otimes \mathrm{PED})_{\mathrm{closure}}
$$

is recovered when $n=2$ and the two densities are identified with SID and PED.

## 2. Quantization

$Q$ becomes discrete whenever the underlying relational variables belong to a discrete spectrum, lattice, homotopy class, representation ring, or quantized state space.

More generally,

$$
Q \in \Lambda,
$$

where $\Lambda$ is the admissible value set of the theory. Examples include

$$
\Lambda = \mathbb{Z},\qquad \mathbb{Z}_n,\qquad \text{weight lattice}(G),\qquad H_k(M,\mathbb{Z}).
$$

The integer-valued case is therefore only one realization of a broader principle:

> Closure invariants inherit the algebraic structure of the space from which their relational densities are drawn.

## 3. Closure Events

A closure event is any transition

$$
\Gamma : \mathcal{S}_{\text{open}} \to \mathcal{S}_{\text{closed}}
$$

for which all internal relational obligations are resolved.

Equivalent characterizations include

$$
\partial \mathcal{S} = 0
$$

or, more generally,

$$
\sum \text{boundary terms} = 0.
$$

A closure may represent:

- a closed geometric object,
- a completed dynamical process,
- a completed inference or measurement,
- a completed information flow,
- a completed causal cycle,
- a completed algebraic relation.

The notion is independent of any particular physical realization.

## 4. Conservation under Transformations

Let

$$
\Gamma_t : \mathcal{C} \to \mathcal{C}
$$

be a continuous family of admissible transformations. Then

$$
\frac{dQ}{dt} = 0
$$

whenever $\Gamma_t$ preserves the closure class. More generally,

$$
Q(\Gamma_t(C)) = Q(C).
$$

Thus $Q$ is not conserved because of a particular force law but because it labels an equivalence class under admissible deformations.

Changes occur only when closure classes are created, destroyed, merged, or split:

$$
\Delta Q \neq 0
$$

only at topological, combinatorial, informational, or relational phase transitions.

## 5. Relation to Geometry

Let $F$ denote the curvature, defect, obstruction, or incompatibility associated with the relational structure. Then

$$
Q = \int_C F
$$

or, in the discrete case,

$$
Q = \sum_C F.
$$

Geometry becomes an accounting system for closure content.

The specific identity of $F$ depends on the theory:

$$
F =
\begin{cases}
\text{electromagnetic curvature} \\
\text{Riemann curvature} \\
\text{torsion} \\
\text{gauge field strength} \\
\text{information divergence} \\
\text{network defect} \\
\text{cohomology class}
\end{cases}
$$

but the generalized statement remains:

> Closure charge and curvature are dual descriptions of the same relational imbalance.

## 6. Relation to Scale

Introduce a relational scale parameter $r_{\mathrm{rel}}$. The invariant satisfies

$$
\frac{\partial Q}{\partial r_{\mathrm{rel}}} = 0
$$

provided the closure class is preserved. What changes is not the total closure content but its density:

$$
\rho_Q \sim \frac{Q}{V(r_{\mathrm{rel}})}.
$$

Consequently

$$
F_{\mathrm{eff}} \propto \frac{Q}{r_{\mathrm{rel}}^{\,d-1}}
$$

in a $d$-dimensional relational manifold.

Inverse-square laws are therefore a special case of a more general dimensional-flux conservation principle.

## 7. Recovering Known Theories

Different choices of the relational variables $R_i$ recover familiar invariants. Examples include

$$
\begin{align*}
Q &= \oint E \cdot dA && \text{(Maxwell charge)}, \\
Q &= \int \operatorname{Tr}(F \wedge F) && \text{(Chern number)}, \\
Q &= \chi(M) && \text{(Euler characteristic)}, \\
Q &= \operatorname{Link}(K_1,K_2) && \text{(linking number)}, \\
Q &= \int G_{\mu\nu} n^\mu \, d\Sigma^\nu && \text{(gravitational flux constructions)}.
\end{align*}
$$

All appear as special instances of the same closure principle.

## 8. General Closure Principle

The deepest generalization is

$$
Q = \Phi(\text{closure class}),
$$

where $\Phi$ is any invariant mapping from a completed relational structure to an algebraic value space. Then:

- Closure creates invariant content.
- Continuous deformation preserves that content.
- Curvature, defect, information, and charge are different representations of that content.
- Scale changes redistribute the content but do not alter the invariant.
- Known gauge, topological, geometric, and informational charges emerge as special cases.

In RDG language this elevates the original expression from a specific charge formula to a universal closure invariant:

$$
\boxed{ Q = \sum_{\text{closures}} \mathcal{R} }
$$

where $\mathcal{R}$ is any conserved relational content and the closure operation itself is the fundamental source of quantization, conservation, and geometric meaning.

---

## Notes

The framework is purely relational: only completed structures contribute, all physical content is encoded in the mutual accounting of the densities $R_i$, and the algebraic, topological, and geometric properties of $Q$ follow directly from the restriction of the sum to closures.
