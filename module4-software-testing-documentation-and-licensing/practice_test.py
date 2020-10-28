#!/usr/bin/env python

# Create Unittests for both modules
# Make sure each class/method includes a docstring
# Make sure entire script conforms to PEP8 guidelines
# To test, run the script in the terminal.


# Standard Python Library
import unittest

# Local Imports
from puppy import Puppy, Leech
from arithmetic import SimpleOperations, Complex


case1 = SimpleOperations(3, 2)
case2 = Complex(3, 2)
case3 = Puppy('James', 5)
case4 = Leech('Jonathan', 10, True)


class ArithmeticTest(unittest.TestCase):
    """A test to ensure that the math functions operate correctly"""
    def test_simple(self):
        ans1 = case1.add()
        ans2 = case1.multiply()
        self.assertEqual(case1.a, 3)
        self.assertEqual(case1.b, 2)
        self.assertEqual(ans1, 5)
        self.assertEqual(ans2, 6)

    def test_complex(self):
        ans3 = case2.nth_root()
        ans4 = case2.exponentiation()
        self.assertEqual(case2.a, 3)
        self.assertEqual(case2.b, 2)
        self.assertEqual(ans3, 1.7321)
        self.assertEqual(ans4, 9)


class PuppyTest(unittest.TestCase):
    """A test to ensure that the puppy class operates as intended"""
    def test_puppy(self):
        self.assertEqual(case3.age, 5)
        self.assertEqual(case3.name, 'James')
    
    def test_leech(self):
        self.assertEqual(case4.is_hypoallergenic, True)
        self.assertEqual(case4.name, 'Jonathan')
        self.assertEqual(case4.age, 10)


if __name__ == "__main__":
    unittest.main()
