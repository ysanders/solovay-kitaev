import unittest
from numpy import array, eye 

from solovay_kitaev.basic_approximation import basic_approximation_generator
from solovay_kitaev.gates import cliffords

class TestBasicApproximation(unittest.TestCase):

    def test_empty(self):
        try:
            for i in basic_approximation_generator():
                print(i)
        except IndexError:
            pass

    def test_simple(self):
        gates = cliffords.clifford_generators
        gates.append(eye(2)) # Add the identity
        base_cases = list(basic_approximation_generator(*gates, depth=1))

        for case in base_cases:
            gate_found = False
            for gate in gates:
                if (gate == case[0]).all():
                    gate_found = True
                    break
            assert(gate_found)

        return

            

if __name__ == "__main__":
    unittest.main()
