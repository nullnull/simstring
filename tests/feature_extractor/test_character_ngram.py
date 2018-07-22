# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor

class TestNgram(TestCase):
    def test_features(self):
        self.assertEqual(CharacterNgramFeatureExtractor().features('abcde'), [' a', 'ab', 'bc', 'cd', 'de', 'e '])
        self.assertEqual(CharacterNgramFeatureExtractor(3).features('abcde'), [' ab', 'abc', 'bcd', 'cde', 'de '])
        self.assertEqual(CharacterNgramFeatureExtractor(4).features('abcde'), [' abc', 'abcd', 'bcde', 'cde '])
        self.assertEqual(CharacterNgramFeatureExtractor(5).features('abcde'), [' abcd', 'abcde', 'bcde '])
        self.assertEqual(CharacterNgramFeatureExtractor().features(u'あいうえお'), [' あ', 'あい', 'いう', 'うえ', 'えお', 'お '])  # Japanese
