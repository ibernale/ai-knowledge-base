---
title: "Agent READMEs: An Empirical Study of Context Files for Agentic Coding (full text)"
url: https://arxiv.org/abs/2505.01824
source: arxiv
type: full-text
parent: "[[2026-05-03-agent-readmes-an-empirical-study-of-context-files-for-agenti]]"
ingested: 2026-05-03
extraction: ar5iv
---

# Smoothness of the Augmented Lagrangian Dual in Convex Optimization

###### Abstract

This paper investigates the general linearly constrained optimization problem: , where is a closed proper convex function, , and . We establish the following results without requiring additional regularity conditions: (1) the augmented Lagrangian dual function is -smooth everywhere; and (2) the solution to exists for any dual variable , where is the augmented parameter and is the augmented Lagrangian. These findings significantly relax the strong assumptions commonly imposed in existing literature to guarantee similar properties.

###### Index Terms:

Convex optimization, augmented Lagrangian dual, smoothness, existence of solutions.## I Introduction

In this paper, we consider the general linearly constrained optimization problem:

| (P1) | ||||
| s.t. |

where is a convex but possibly nonsmooth function, , and . Without loss of generality, we assume that the solution of [P1](#S1.Ex1) exists. The augmented Lagrangian method (ALM), originally proposed by Hestenes [[1](#bib.bib1)] and Powell [[2](#bib.bib2)], remains a cornerstone algorithm for solving [P1](#S1.Ex1). Its iterative scheme is given by

| (1) | ||||
| (2) |

where is the dual variable, is the augmented parameter, and the augmented Lagrangian is defined as

| (3) |

One convenient approach for analyzing the iteration complexity of (inexact) ALM111In inexact ALM, the subproblem in [1](#S1.E1) is allowed to be solved inexactly. [[3](#bib.bib3), [4](#bib.bib4)] lies in interpreting it as (inexact) gradient descent (GD) [[5](#bib.bib5), [6](#bib.bib6)] applied to the augmented Lagrangian dual problem of [P1](#S1.Ex1):

| (4) |

where the augmented Lagrangian dual function is defined as

| (5) |

with . Then, the convergence and outer iteration complexity of ALM can be easily established by applying the convergence results of GD. Since the convergence of GD depends critically on the objective function’s smoothness and convexity, establishing the smoothness of (which is always concave) becomes pivotal.

Existing Results and Limitations. For the special case where with being a compact convex set and continuous convex, the Weierstrass’ theorem [[7](#bib.bib7), Proposition A.8] guarantees the existence of solutions to for any , thus implying . The -smoothness of then follows directly from [[8](#bib.bib8), Theorem 1] (see [[4](#bib.bib4), Proposition 1]). An alternative approach for establishing the smoothness of involves demonstrating the invariance of over the solution set of and then applying the Danskin’s Theorem [[7](#bib.bib7), Proposition B.22(b)] (refer to [[9](#bib.bib9), Lemmas 2.1 and 2.2]). However, this analysis fails when is not bounded. In such cases, additional assumptions are necessary to ensure the existence of solutions to ; for instance, is coercive222We say a function is coercive if . (which holds if is coercive). Even with these assumptions, we cannot straightforwardly apply [[8](#bib.bib8), Theorem 1] or the Danskin’s Theorem to establish the smoothness of .

The situation becomes even more complex when does not conform to the specific form mentioned above, and we only assume that is closed proper333We say a function is proper if for all and . convex. To ensure the existence of solutions to and the smoothness of , we may need to introduce additional assumptions. For example, assuming that is strongly convex or that has full column rank. In this scenario, is strongly convex, leading to a singleton solution set for , and the smoothness of can be established using results on the Fenchel conjugate from [[10](#bib.bib10), Lecture 5]. However, these assumptions are too restrictive, limiting the applicability of the results. Thus, we are interested in whether it is possible to establish the aforementioned results for general closed proper convex functions and without imposing additional assumptions.

Our Contributions. This paper resolves this gap by proving that for any closed proper convex :

-
1.
The augmented Lagrangian dual function is -smooth everywhere.

-
2.
The solution to exists for any .


These results reveal an interesting fact: the augmented Lagrangian dual function is generally smooth in convex optimization, significantly broadening the theoretical foundation of ALM. Consequently, convergence rates and iteration complexity bounds for both standard and accelerated (inexact) ALM variants [[11](#bib.bib11), [12](#bib.bib12), [13](#bib.bib13)] can now be rigorously established for any problem reducible to [P1](#S1.Ex1).

## II Preliminaries

### II-A Notations

We use the standard inner product and the standard Euclidean norm for vectors, and the standard spectral norm for matrices. For a function , denotes its (effective) domain, denotes its subdifferential at , denotes the proximal operator of with , and denote its Fenchel conjugate and Fenchel biconjugate respectively, and denotes its Moreau envelope (or Moreau-Yosida regularization) with . For a set , denotes its interior, denotes its relative interior, and denotes its indicator function.

### II-B Convex Analysis

The following lemma demonstrates the smoothness of the Moreau envelope of any closed proper convex function.

###### Lemma 1.

[[14](#bib.bib14), Theorem 3 of Lecture 26]
Assume that is closed proper convex. Then: (1) ; (2) is continuously differentiable on and ; (3) is convex and -smooth.

###### Lemma 2.

[[15](#bib.bib15), Corollary E.1.4.4]
Assume that is closed proper convex, we have

| (6) |

The following two lemmas pertain to subdifferential calculus. Specifically, [Lemma 3](#Thmlemma3) can be easily derived from [[16](#bib.bib16), Theorems 23.8] by utilizing two key facts: (1) , and (2) if [[16](#bib.bib16), Theorem 6.2].

###### Lemma 3.

Assume that is proper convex and is convex, then .

###### Lemma 4.

[[14](#bib.bib14), Proposition 8 of Lecture 24]
Assume that is closed proper convex, , and . Let , we have

| (7) |

## III Theoretical Results

Our main results are presented in the following theorem, which demonstrates that is -smooth under the sole assumption that is closed proper convex.

###### Theorem 1.

Assume that is closed proper convex. Then: (1) ; (2) is concave and -smooth; (3) For any , there exists at least one solution of . Moreover, holds for any solution .

###### Remark 1.

Theorem [1](#Thmtheorem1) reveals that the augmented Lagrangian dual function of [P1](#S1.Ex1) is smooth everywhere under the only assumption that is closed proper convex. This result is significantly more general than existing results, which require stronger assumptions, such as , where is a compact convex set and is a continuous convex function [[4](#bib.bib4), [9](#bib.bib9)].

Before proving [Theorem 1](#Thmtheorem1), we first establish the equivalence between and , where

| (8) |

is the Moreau envelope of , and

| (9) |

is the standard Lagrangian dual function of [P1](#S1.Ex1).

###### Lemma 5.

Assume that is closed proper convex, then , i.e., for any .

###### Proof.

Let

| (10) |

we have

| (11) |

We first prove that

| (12) |

holds for any . Define , we can easily obtain its Fenchel conjugate: . Clearly and . Let , it is obvious that and is close proper convex. It follows that

| (13) | ||||

According to [[15](#bib.bib15), Proposition E.1.3.1], we have

| (14) |

It follows that

| (15) | ||||

Recall that and are both close proper convex. By applying [[16](#bib.bib16), Corollary 31.2.1] to [13](#S3.E13) and [15](#S3.E15), we can conclude that [12](#S3.E12) holds if

| (16) |

Since is proper, , then [[16](#bib.bib16), Theorem 6.2]. Additionally, since , [16](#S3.E16) holds, and consequently, [12](#S3.E12) also holds.
Note that

| (17) |

Combining [11](#S3.E11), [12](#S3.E12) and [13](#S3.E13), we can finally obtain

| (18) | ||||

∎

Proof of [Theorem 1](#Thmtheorem1).
According to [Lemmas 1](#Thmlemma1) and [5](#Thmlemma5), we can immediately obtain (1) and (2). A direct result of (1) is that . As is closed proper convex, so is , which implies that is also closed proper convex [[15](#bib.bib15), Theorem E.1.1.2]. Then, applying [Lemma 3](#Thmlemma3) and [Lemma 4](#Thmlemma4) to [5](#S1.E5) gives

| (19) |

From (2) we know that is differentiable everywhere, hence [19](#S3.E19) implies two facts: (1) ; (2) has only one element. Let be any element in , we have . By [Lemma 2](#Thmlemma2), we have

| (20) |

which implies that is a solution to , as established by [Lemma 3](#Thmlemma3) and [[16](#bib.bib16), Theorem 27.1].
∎

## IV Conclusion

In this paper, we establish the smoothness of the augmented Lagrangian dual function and the existence of solutions to for any for [P1](#S1.Ex1), under the only assumption that is closed proper convex. These results significantly relax the strong assumptions typically imposed in existing literature to ensure similar properties.

## References

-
[1]
M. R. Hestenes, “Multiplier and gradient methods,”
*Journal of Optimization Theory and Applications*, vol. 4, no. 5, pp. 303–320, 1969. -
[2]
M. J. Powell, “A method for nonlinear constraints in minimization problems,”
*Optimization*, pp. 283–298, 1969. -
[3]
V. Nedelcu, I. Necoara, and Q. Tran-Dinh, “Computational complexity of inexact
gradient augmented lagrangian methods: Application to constrained mpc,”
*SIAM Journal on Control and Optimization*, vol. 52, no. 5, pp. 3109–3134, 2014. -
[4]
G. Lan and R. D. Monteiro, “Iteration-complexity of first-order augmented
lagrangian methods for convex programming,”
*Mathematical Programming*, vol. 155, no. 1, pp. 511–547, 2016. -
[5]
O. Devolder, F. Glineur, and Y. Nesterov, “First-order methods of smooth
convex optimization with inexact oracle,”
*Mathematical Programming*, vol. 146, no. 1, pp. 37–75, 2014. -
[6]
M. Schmidt, N. Roux, and F. Bach, “Convergence rates of inexact
proximal-gradient methods for convex optimization,”
*Advances in Neural Information Processing Systems*, vol. 24, 2011. -
[7]
D. P. Bertsekas,
*Nonlinear Programming*. Athena Scientific, 2016, vol. 4. -
[8]
Y. Nesterov, “Smooth minimization of non-smooth functions,”
*Mathematical Programming*, vol. 103, pp. 127–152, 2005. -
[9]
M. Hong and Z.-Q. Luo, “On the linear convergence of the alternating direction
method of multipliers,”
*Mathematical Programming*, vol. 162, no. 1, pp. 165–199, 2017. -
[10]
L. Vandenberghe,
*Optimization Methods for Large-Scale Systems*. Lecture Slides, UCLA, 2022. [Online]. Available:[https://www.seas.ucla.edu/~vandenbe/236C](https://www.seas.ucla.edu/~vandenbe/236C) -
[11]
Y. Nesterov,
*Lectures on Convex Optimization*. Springer, 2018, vol. 137. -
[12]
B. He and X. Yuan, “On the acceleration of augmented lagrangian method for
linearly constrained optimization,”
*Optimization Online*, vol. 3, 2010. -
[13]
M. Kang, S. Yun, H. Woo, and M. Kang, “Accelerated bregman method for linearly
constrained–minimization,”
*Journal of Scientific Computing*, vol. 56, no. 3, pp. 515–534, 2013. -
[14]
D. Davis,
*Mathematical Programming I*. Lecture Notes, Cornell University, 2016. [Online]. Available:[https://people.orie.cornell.edu/dsd95/orie63002016.html](https://people.orie.cornell.edu/dsd95/orie63002016.html) -
[15]
J.-B. Hiriart-Urruty and C. Lemaréchal,
*Fundamentals of Convex Analysis*. Springer Science & Business Media, 2004. -
[16]
R. T. Rockafellar,
*Convex Analysis*. Princeton University Press, 1970.