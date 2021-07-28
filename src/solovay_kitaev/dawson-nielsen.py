# this is just a template for [DN05]
# see section 3 specifically...

from numpy import prod
from numpy import array

def group_commutator(V, W):
    return prod(prod(V, W), prod(V.conj().T, W.conj().T))

def basic_approximation(U):
    pass

def GC_Decompose(U):
    pass

def solovay_kitaev(
        unitary: array,
        depth: int,
        gates = None : list # TODO import gates and include appropriate defaults, expand to *args
        ) -> array, list:
    '''
        solovay_kitaev
        Function to implement the Solovay Kitaev algorithm
        Takes in a unitary to approximate along with a maximal depth
        :: unitary : array :: The unitary to approximate
        :: depth   : int   :: The maximum depth of the approximation
        :: gates   : array :: The set of basis gates
        Returns the approximation of the unitary along with a 
        list of the gates that provide the approxmiation
    '''
    if depth == 0:
        return Basic_Approximation(unitary)
    else:
        previous_unitary = Solovay_Kitaev(unitary, depth-1)
        V, W = GC_Decompose(prod(unitary, previous_unitary.conj().T))
        prev_V = Solovay_Kitaev(V, depth-1)
        prev_W = Solovay_Kitaev(W, depth-1)
        return prod(group_commutator(prev_V, prev_W),  previous_unitary)
