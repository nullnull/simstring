# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.database.dict import DictDatabase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor

class TestDict(TestCase):
    strings = ['a', 'ab', 'abc', 'abcd', 'abcde']

    def setUp(self):
        self.db = DictDatabase(CharacterNgramFeatureExtractor(2))
        for string in self.strings:
            self.db.add(string)

    def test_strings(self):
        self.assertEqual(self.db.strings, self.strings)

    def test_min_feature_size(self):
        self.assertEqual(self.db.min_feature_size(), min(map(lambda x: len(x) + 1, self.strings)))

    def test_max_feature_size(self):
        self.assertEqual(self.db.max_feature_size(), max(map(lambda x: len(x) + 1, self.strings)))

    def test_lookup_strings_by_feature_set_size_and_feature(self):
        self.assertEqual(self.db.lookup_strings_by_feature_set_size_and_feature(4, 'ab'), set(['abc']))
        self.assertEqual(self.db.lookup_strings_by_feature_set_size_and_feature(3, 'ab'), set(['ab']))
        self.assertEqual(self.db.lookup_strings_by_feature_set_size_and_feature(2, 'ab'), set([]))
