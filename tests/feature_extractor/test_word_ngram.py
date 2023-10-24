# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.feature_extractor.word_ngram import WordNgramFeatureExtractor



class TestNgram(TestCase):
    def test_features(self):
        
        self.assertEqual(
            WordNgramFeatureExtractor().features("abcd"),
            [(" ", "abcd"), ("abcd", " ")],
        )
        self.assertEqual(
            WordNgramFeatureExtractor(2).features("hello world"),
            [(" ", "hello"), ("hello", "world"), ("world", " ")],
        )
        self.assertEqual(
            WordNgramFeatureExtractor(3).features("hello world"),
            [(" ", "hello", "world"), ("hello", "world", " ")],
        )
      