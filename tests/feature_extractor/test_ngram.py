# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.feature_extractor.ngram import NgramFeatureExtractor

class TestNgram(TestCase):
    def test_features(self):
        self.assertEqual(NgramFeatureExtractor().features('abcde'), [' a', 'ab', 'bc', 'cd', 'de', 'e '])
        self.assertEqual(NgramFeatureExtractor(3).features('abcde'), [' ab', 'abc', 'bcd', 'cde', 'de '])
        self.assertEqual(NgramFeatureExtractor(4).features('abcde'), [' abc', 'abcd', 'bcde', 'cde '])
        self.assertEqual(NgramFeatureExtractor(5).features('abcde'), [' abcd', 'abcde', 'bcde '])
        self.assertEqual(NgramFeatureExtractor().features(u'あいうえお'), [' あ', 'あい', 'いう', 'うえ', 'えお', 'お '])  # Japanese
