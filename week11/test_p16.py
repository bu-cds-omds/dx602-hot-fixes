#!/usr/bin/env python3

import inspect
import homework

import test_utils


class P16TestCase(test_utils.TestCase):
    def test_p16(self):
        self.assertTrue(hasattr(homework, "p16"), "Variable p16 is missing.")

        p16 = homework.p16
        self.assertFalse(isinstance(p16, type(Ellipsis)), "Variable p16 was not set.")

        self.assertEqual(p16.shape, (5,))
        self.assertValues(p16, expected_projections=[12.461358898012791, 3.1540433778485216, 8.926668216435397, 8.287339857213568, 11.109244312746868])


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
