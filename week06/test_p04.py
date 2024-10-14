#!/usr/bin/env python3

import inspect
import unittest
import homework

import numpy as np


class P4TestCase(unittest.TestCase):
    def test_p4(self):
        self.assertTrue(hasattr(homework, "p4"), "Variable p4 is missing.")

        p4 = homework.p4
        self.assertFalse(isinstance(p4, type(...)), "Variable p4 was not set...")

        def check(input, output_expected):
            with self.subTest(input=input):
                output = p4(input)
                self.assertIsNotNone(output)
                self.assertIsInstance(output, bool)
                self.assertEqual(output, output_expected)

        check(np.array([]), False)
        check(np.zeros(0), False)
        check(np.zeros((1000, 1000)), True)
        check(np.zeros(100000), False)
        check(np.zeros(120000), False)
        check(np.zeros(1000000), True)


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
