# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor

class TestNgram(TestCase):
    def test_features(self):
        self.assertEqual(CharacterNgramFeatureExtractor().features('abcde'), ['$a_1', 'ab_1', 'bc_1', 'cd_1', 'de_1', 'e$_1'])
        self.assertEqual(CharacterNgramFeatureExtractor(3).features('abcde'), ['$$a_1', '$ab_1', 'abc_1', 'bcd_1', 'cde_1', 'de$_1', 'e$$_1'])
        self.assertEqual(CharacterNgramFeatureExtractor().features(u'あいうえお'),['$あ_1', 'あい_1', 'いう_1', 'うえ_1', 'えお_1', 'お$_1'])  # Japanese
