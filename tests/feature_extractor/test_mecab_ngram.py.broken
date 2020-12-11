# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.feature_extractor.mecab_ngram import MecabNgramFeatureExtractor

class TestNgram(TestCase):
    def test_features(self):
        # Japanese
        self.assertEqual(
            MecabNgramFeatureExtractor().features(u'大迫半端ないって'),
            [(' ', '大迫'), ('大迫', '半端'), ('半端', 'ない'), ('ない', 'って'), ('って', ' ')]
        )
        self.assertEqual(
            MecabNgramFeatureExtractor(3).features(u'後ろ向きのボールめっちゃトラップするもん'),
            [(' ', '後ろ向き', 'の'), ('後ろ向き', 'の', 'ボール'), ('の', 'ボール', 'めっちゃ'), ('ボール', 'めっちゃ', 'トラップ'), ('めっちゃ', 'トラップ', 'する'), ('トラップ', 'する', 'もん'), ('する', 'もん', ' ')]
        )
