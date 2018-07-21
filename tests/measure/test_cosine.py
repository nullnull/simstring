# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.measure.cosine import CosineMeasure

class TestCosine(TestCase):
    measure = CosineMeasure()

    def test_min_feature_size(self):
        self.assertEqual(self.measure.min_feature_size(5, 1.0), 5)
        self.assertEqual(self.measure.min_feature_size(5, 0.5), 2)

    def test_max_feature_size(self):
        self.assertEqual(self.measure.max_feature_size(5, 1.0), 5)
        self.assertEqual(self.measure.max_feature_size(5, 0.5), 20)

    def test_minimum_common_feature_count(self):
        self.assertEqual(self.measure.minimum_common_feature_count(5, 5, 1.0), 5)
        self.assertEqual(self.measure.minimum_common_feature_count(5, 20, 1.0), 10)
        self.assertEqual(self.measure.minimum_common_feature_count(5, 5, 0.5), 3)

    def test_similarity(self):
        x = [1, 2, 3]
        y = [1, 2, 3, 4]
        self.assertEqual(round(self.measure.similarity(x, x), 2), 1.0)
        self.assertEqual(round(self.measure.similarity(x, y), 2), 0.87)
