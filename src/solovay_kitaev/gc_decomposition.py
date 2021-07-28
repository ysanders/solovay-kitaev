import numpy as np
from scipy.optimize import root_scalar
from scipy.linalg import schur

I   = np.identity(2)
X   = np.array([[0, 1], [1, 0]])
Y   = np.array([[0, -1j], [1j, 0]])
Z   = np.array([[1, 0], [0, -1]])
S   = np.array([[1, 0], [0, 1j]])
Sdg = np.array([[1, 0], [0, -1j]])
T   = np.array([[1, 0], [0, (1+1j) / np.sqrt(2)]])
Tdg = np.array([[1, 0], [0, (1+1j) / np.sqrt(2)]])

def V(phi):
    return np.cos(phi/2) * I - 1j * np.sin(phi/2) * X

def W(phi):
    return np.cos(phi/2) * I - 1j * np.sin(phi/2) * Y

def group_commutator(V, W):
    return V @ W @ V.conj().T @ W.conj().T

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
