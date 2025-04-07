#!/usr/bin/env python3

import unittest

import test_utils


class P16TestCase(test_utils.TestCase):
    def test_p16(self):
        self.assertArrayByName(
            "p16",
            expected_shape=(5,),
            expected_projections=[
                12.461358898012791,
                3.1540433778485216,
                8.926668216435397,
                8.287339857213568,
                11.109244312746868,
            ],
            require_array=True,
        )


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
