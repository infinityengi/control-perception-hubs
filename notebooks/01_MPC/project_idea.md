## Model-Based Predictive Control (MPC)

**1. Notebook:** *MPC for cart-pole (linear MPC)*

* Tools: Python, CasADi or osqp + cvxpy, Matplotlib
* What to show: linearize dynamics, set up QP MPC, compare with LQR, visualize trajectories.
* Learning outcome: formulation of finite-horizon optimization, constraints handling.

**2. Project:** *Nonlinear MPC with do-mpc for a mobile robot*

* Tools: `do-mpc` (Python), CasADi, RViz for visualization (optional)
* Tasks: implement obstacle avoidance, constraints, replanning; include notebook + small sim.

**Repo helpers:** do-mpc, CasADi, pyMPC, OSQP.