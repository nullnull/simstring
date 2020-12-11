# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.searcher import Searcher
from simstring.database.dict import DictDatabase
from simstring.measure.cosine import CosineMeasure
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor

class TestSearcher(TestCase):
    strings = ['a', 'ab', 'abc', 'abcd', 'abcde']

    def setUp(self):
        db = DictDatabase(CharacterNgramFeatureExtractor(2))
        for string in self.strings:
            db.add(string)
        self.searcher = Searcher(db, CosineMeasure())

    def test_search1(self):
        self.assertEqual(self.searcher.search('a', 1.0), ['a'])

    def test_search2(self):
        self.assertEqual(self.searcher.search('ab', 0.5), ['ab', 'abc', 'abcd'])
        self.assertEqual(self.searcher.search('abc', 1.0), ['abc'])
        self.assertEqual(self.searcher.search('abc', 0.9), ['abc'])

    def test_search3(self):
        self.assertEqual(self.searcher.search('abc', 1.0), ['abc'])
        self.assertEqual(self.searcher.search('abc', 0.9), ['abc'])

    def test_search4(self):
        self.assertEqual(self.searcher.search('abcd', 1.0), ['abcd'])
        self.assertEqual(self.searcher.search('abcd', 0.9), ['abcd'])