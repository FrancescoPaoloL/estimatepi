import unittest
from estimate_pi import estimante_pi
from math import pi

class TestEstimantePi(unittest.TestCase):
    def test_estimated_value_within_range(self):
        n = 100000
        estimated_value_of_pi = estimante_pi(n)
        self.assertGreaterEqual(estimated_value_of_pi, 2.8, "The estimated value of pi is too low.")
        self.assertLessEqual(estimated_value_of_pi, 3.5, "The estimated value of pi is too high.")
        
    def test_accuracy(self):
        n = 100000
        estimated_value_of_pi = estimante_pi(n)
        error = abs(estimated_value_of_pi - pi)
        self.assertLessEqual(error, 0.1, "The estimated value of pi is not accurate enough.")


if __name__ == '__main__':
    unittest.main()

