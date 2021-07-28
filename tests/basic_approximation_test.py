import unittest
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
        pass
            

if __name__ == "__main__":
    unittest.main()
