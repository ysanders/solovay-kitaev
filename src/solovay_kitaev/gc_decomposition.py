import numpy as np 
from scipy.optimize import root_scalar
from scipy.linalg import schur

import numpy as np
from scipy.optimize import root_scalar
from numpy import array
from scipy.linalg import schur
from solovay_kitaev.gates.paulis import pauli_x, pauli_y, pauli_z


def dag(matrix : array):
    '''
    dag
    Performs a conjugate transpose on the matrix
    '''
    return matrix.conj().T


def unitary_phase(phi):
    '''
        TODO Yuval
    '''
    # [DN05, Eq. (10)]
    return 2 * np.arcsin(
        2 * (np.sin(phi/2) ** 2) * np.sqrt(
            1 - np.sin(phi/2) ** 4
        )
    )

def invert_unitary_phase(theta):
    '''
        TODO Yuval
    '''
    # Inversion of the theta function
    # warning: this function is NOT VECTORISED
    def fn(phi):
        return unitary_phase(phi) - theta
    solution = root_scalar(fn, bracket=[0, np.pi/2])
    return solution.root


def gc_decompose(unitary, determinant_error=1e-6):
    '''
        TODO Yuval
    '''

    #  GC_decompose requires an input with determinant 1.
    assert(np.abs(np.linalg.det(unitary) - 1) < determinant_error)

    eigen_values, _ = np.linalg.eig(unitary)
    coefficient_of_identity = np.real(eigen_values[0])
    output_phase = invert_unitary_phase(2 * np.arccos(coefficient_of_identity))
    
    left_transform = np.cos(output_phase / 2) * identity - 1j * np.sin(output_phase / 2) * pauli_x
    right_transform = np.cos(output_phase / 2) * identity - 1j * np.sin(output_phase / 2) * pauli_y

    group_commutator = left_transform @ right_transform @ dag(left_transform) @ dag(right_transform)

    _, schur_unitary = schur(unitary)
    _, schur_group_commutator = schur(group_commutator)
    similary_transform = schur_group_commutator.conj().T @ schur_unitary

    left_transform = similary_transform @ left_transform @ dag(similary_transform)
    right_transform =  similary_transform @ right_transform @ dag(similary_transform)
    return left_transform, right_transform
