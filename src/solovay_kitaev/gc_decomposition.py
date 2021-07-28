import numpy as np from scipy.optimize import root_scalar
from scipy.linalg import schur

import numpy as np
from scipy.optimize import root_scalar
from scipy.linalg import schur

I   = np.identity(2)
X   = np.array([[0, 1], [1, 0]])
Y   = np.array([[0, -1j], [1j, 0]])
Z   = np.array([[1, 0], [0, -1]])

def theta(phi):
    # [DN05, Eq. (10)]
    return 2 * np.arcsin(
        2 * (np.sin(phi/2) ** 2) * np.sqrt(
            1 - np.sin(phi/2) ** 4
        )
    )

def phi(theta_arg):
    # crappy inversion of the theta function
    # warning: this function is NOT VECTORISED
    def fn(phi_arg):
        return theta(phi_arg) - theta_arg
    sol = root_scalar(fn, bracket=[0, np.pi/2])
    return sol.root

def GC_decompose(U):
    assert np.abs(np.linalg.det(U) - 1) < 10**(-6), "GC_decompose requires an input with determinant 1."
    vals, _ = np.linalg.eig(U)
    cos_theta_on_two = np.real(vals[0])
    phi_value = phi(2 * np.arccos(cos_theta_on_two))
    V = np.cos(phi_value / 2) * I - 1j * np.sin(phi_value / 2) * X
    W = np.cos(phi_value / 2) * I - 1j * np.sin(phi_value / 2) * Y
    gc = V @ W @ V.conj().T @ W.conj().T # group commutator
    _, S_U = schur(U)
    _, S_gc = schur(gc)
    S = S_gc.conj().T @ S_U
    return S @ V @ S.conj().T, S @ W @ S.conj().T
