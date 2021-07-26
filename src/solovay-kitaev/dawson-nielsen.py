# this is just a template for [DN05]
# see section 3 specifically...

from numpy import prod

def Basic_Approximation(U):
    pass

def GC_Decompose(U):
    pass

def Solovay_Kitaev(U, depth):
    if depth == 0:
        return Basic_Approximation(U)
    else:
        prev_U = Solovay_Kitaev(U, depth-1)
        V, W = GC_Decompose(prod(U, prev_U.conj().T))
        prev_V = Solovay_Kitaev(V, depth-1)
        prev_W = Solovay_Kitaev(W, depth-1)
        return prod(prod(prod(prev_V, prev_W),
                         prod(prev_V.conj().T, prev_W.conj().T)),
                    prev_U)


