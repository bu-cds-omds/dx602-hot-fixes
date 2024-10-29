#!/usr/bin/env python3

import inspect
import homework

import test_utils


class P6TestCase(test_utils.TestCase):
    def test_p6(self):
        self.assertTrue(hasattr(homework, "p6"), "Variable p6 is missing.")

        p6 = homework.p6
        self.assertFalse(isinstance(p6, type(Ellipsis)), "Variable p6 was not set.")

        self.assertValues(p6, expected_projections=[9.002404355530881])


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
