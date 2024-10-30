# test_utils.py

import hashlib
import random
import unittest

import numpy as np

class TestCase(unittest.TestCase):
    def assertColumns(self, df, columns):
        self.assertTrue(hasattr(df, "columns"), msg=f"Data frame does not have columns attribute. Type = {type(df)}.")

        for column in columns:
            with self.subTest(column = column):
                self.assertIn(column, df.columns)

    def assertValues(self, a, *, expected_projections=None, expected_sum=None):
        a = np.asarray(a)

        for v in a:
            self.assertIsNotNone(v)
            self.assertFalse(isinstance(v, str), msg="Found string value where numbers expected.")
                
        if expected_sum is not None:
            self.assertAlmostEqual(np.sum(a), expected_sum, msg=f"Sum does not match expected sum {expected_sum}")

        num_projections = len(expected_projections) if expected_projections else min(a.size, 10)
            
        a = a.reshape(-1)
        r = random.Random(len(a))
        s = (len(a), num_projections)
        projection_matrix = [r.random() for _ in range(s[0] * s[1])]
        projection_matrix = np.reshape(projection_matrix, s)
        projections = np.matmul(a, projection_matrix)

        if expected_projections is None:
            print("PROJECTIONS", list(map(float, projections)))

        self.assertTrue(expected_projections is not None, msg="test incomplete")
        self.assertTrue(np.allclose(projections, expected_projections),
                        msg="Array values are incorrect.")

    def assertShape(self, a, *, expected_dimensions=None, expected_projections=None):
        self.assertTrue(hasattr(a, "shape"), msg=f"Array/data frame does not have a shape. Type = {type(a)}.")

        shape = a.shape
        if expected_dimensions is not None:
            self.assertEqual(len(shape), expected_dimensions, msg=f"Shape does not match expected number of dimensions ({expected_dimensions:d}");

        if expected_projections is not None:
            projection_matrix = [[17, 23, 19, 37],
                                 [97, 79, 83, 73],
                                 [61, 71, 43, 53],
                                 [31, 41, 47, 59]]
            projection_matrix = np.asarray(projection_matrix)
            projection_matrix = projection_matrix[:len(shape),
                                                  :len(shape)]

            projections = np.matmul(shape, projection_matrix)
            self.assertTrue(np.array_equal(projections, expected_projections), msg=f"Shape {shape!r} is incorrect.")

    def assertString(self, s, *, expected_hash=None, msg=None):
        s_hashed = hashlib.sha256(s.encode()).hexdigest()
        self.assertEqual(s_hashed, expected_hash, msg=msg)
