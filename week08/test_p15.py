#!/usr/bin/env python3

import inspect
import math
import unittest
import homework

import pandas as pd


class P15TestCase(unittest.TestCase):
    def test_p15(self):
        self.assertTrue(hasattr(homework, "p15"), "Variable p15 is missing.")

        p15 = homework.p15
        self.assertFalse(isinstance(p15, type(Ellipsis)), "Variable p15 was not set.")

        def check(df):
            output = p15(df)

            total_bytes = output * len(df)
            total_bytes_expected = []
            total_bytes_expected.append(sum(df.memory_usage()))
            total_bytes_expected.append(sum(df.memory_usage(deep=True)))

            self.assertTrue(any(math.isclose(total_bytes, e) for e in total_bytes_expected), msg="total bytes does not match any expected calculations")

        def check_tsv(filename):
            with self.subTest(filename=filename):
                return check(pd.read_csv(filename, sep="\t"))

        check_tsv("abalone.tsv")
        check_tsv("boston-TMAX.tsv")


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
