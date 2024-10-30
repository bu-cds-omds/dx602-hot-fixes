#!/usr/bin/env python3

import inspect
import homework

import test_utils


class P9TestCase(test_utils.TestCase):
    def test_p9(self):
        self.assertTrue(hasattr(homework, "p9"), "Variable p9 is missing.")

        p9 = homework.p9
        self.assertFalse(isinstance(p9, type(Ellipsis)), "Variable p9 was not set.")

        self.assertTrue(all(isinstance(i, str) for i in p9.index), msg="p9 index should be strings for species.")
        self.assertEqual(set(p9.index), {"Adelie Penguin (Pygoscelis adeliae)", "Chinstrap penguin (Pygoscelis antarctica)", "Gentoo penguin (Pygoscelis papua)"})
        
        self.assertEqual(p9.size, 3)

        p9 = p9.sort_index()
        self.assertValues(
            p9,
            expected_projections=[
                78.87001689531311,
                229.11798910429337,
                92.84904552028829,
            ],
        )


############################################################
# startup handling #########################################
############################################################

if __name__ == "__main__":
    unittest.main()
