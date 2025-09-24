import numpy as np
def lqr(A, B, Q, R):
    """Solve the continuous-time LQR controller (Riccati equation).
    Returns gain K such that u = -Kx.
    This is a small helper for tutorial purposes (uses scipy)."""
    from scipy import linalg
    X = linalg.solve_continuous_are(A, B, Q, R)
    K = np.linalg.inv(R) @ B.T @ X
    return K
