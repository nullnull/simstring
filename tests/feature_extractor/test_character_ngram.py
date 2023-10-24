# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor



class TestNgram(TestCase):
    def test_features(self):
        
        self.assertEqual(
            CharacterNgramFeatureExtractor().features("abcde"),
            ["$a_1", "ab_1", "bc_1", "cd_1", "de_1", "e$_1"],
        )
        self.assertEqual(
            CharacterNgramFeatureExtractor(3).features("abcde"),
            ["$$a_1", "$ab_1", "abc_1", "bcd_1", "cde_1", "de$_1", "e$$_1"],
        )
        self.assertEqual(
            CharacterNgramFeatureExtractor().features("あいうえお"),
            ["$あ_1", "あい_1", "いう_1", "うえ_1", "えお_1", "お$_1"],
        )  # Japanese

        self.assertEqual(
            CharacterNgramFeatureExtractor().features("marc anthony"),
            ['$m_1', 'ma_1', 'ar_1', 'rc_1', 'c _1', ' a_1', 'an_1', 'nt_1', 'th_1', 'ho_1', 'on_1', 'ny_1', 'y$_1'],
        )
        self.assertEqual(
            CharacterNgramFeatureExtractor().features("anthony marc"),
            ['$a_1', 'an_1', 'nt_1', 'th_1', 'ho_1', 'on_1', 'ny_1', 'y _1', ' m_1', 'ma_1', 'ar_1', 'rc_1', 'c$_1'],
        )
    
    def test_endmarker(self):
        c_end = CharacterNgramFeatureExtractor(endmarker=" ")
        self.assertEqual(
            set(c_end.features("marc anthony")),
            set(c_end.features("anthony marc"))
        )
