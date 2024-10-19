#!/usr/bin/env python3

import inspect
import unittest
import homework

import numpy as np


class P8TestCase(unittest.TestCase):
    def test_p8(self):
        self.assertTrue(hasattr(homework, "p8"), "Variable p8 is missing.")

        p8 = homework.p8
        self.assertFalse(isinstance(p8, type(Ellipsis)), "Variable p8 was not set.")

        def check(x, output_expected):
            x = np.asarray(x)
            output_expected = np.asarray(output_expected)

            with self.subTest(x=x):
                output = p8(x)
                self.assertIsNotNone(output)
                output = np.asarray(output)

                self.assertEqual(output.shape, output_expected.shape)
                self.assertTrue((output == output_expected).all())

        check([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 5, 9])
        check(np.ones((3, 3)), np.ones(3))
        check(np.zeros((4, 4)), np.zeros(4))


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
