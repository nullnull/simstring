# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.measure.overlap import OverlapMeasure
from sys import maxsize

class TestOverlap(TestCase):
    measure = OverlapMeasure()

    def test_min_feature_size(self):
        self.assertEqual(self.measure.min_feature_size(5, 1.0), 1)
        self.assertEqual(self.measure.min_feature_size(5, 0.5), 1)

    def test_max_feature_size(self):
        self.assertEqual(self.measure.max_feature_size(5, 1.0), maxsize)
        self.assertEqual(self.measure.max_feature_size(5, 0.5), maxsize)

    def test_minimum_common_feature_count(self):
        self.assertEqual(self.measure.minimum_common_feature_count(5, 5, 1.0), 5)
        self.assertEqual(self.measure.minimum_common_feature_count(5, 20, 1.0), 5)
        self.assertEqual(self.measure.minimum_common_feature_count(5, 5, 0.5), 3)

    def test_similarity(self):
        x = [1, 2, 3]
        y = [1, 2, 3, 4]
        self.assertEqual(round(self.measure.similarity(x, x), 2), 3)
        self.assertEqual(round(self.measure.similarity(x, y), 2), 3)

        z = [1, 1, 2, 3]
        self.assertEqual(round(self.measure.similarity(z, z), 2), 3)
