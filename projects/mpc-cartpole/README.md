# MPC Cart-Pole Demo

**Goal:** Implement a simple linear MPC for the cart-pole (inverted pendulum) and compare with LQR.

## Contents
- `notebook.ipynb` — tutorial (in `notebooks/01_MPC/`)
- `src/` — small helper modules
- `run_demo.py` — script to run a simple simulation and save plots

## Quick run
```bash
conda activate control-hub
python projects/mpc-cartpole/run_demo.py
```

## Notes
This is a lightweight demo suitable for GitHub pages as a showcase. For a more advanced MPC use `do-mpc` with CasADi.
