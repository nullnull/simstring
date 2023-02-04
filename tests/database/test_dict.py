# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.database.dict import DictDatabase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
import pickle

class TestDict(TestCase):
    strings = ['a', 'ab', 'abc', 'abcd', 'abcde']

    def setUp(self):
        self.db = DictDatabase(CharacterNgramFeatureExtractor(2))
        for string in self.strings:
            self.db.add(string)

    def test_strings(self):
        self.assertEqual(self.db.strings, self.strings)

    # def test_min_feature_size(self):
    #     self.assertEqual(self.db.min_feature_size(), min(map(lambda x: len(x) + 1, self.strings)))

    # def test_max_feature_size(self):
    #     self.assertEqual(self.db.max_feature_size(), max(map(lambda x: len(x) + 1, self.strings)))

    def test_lookup_strings_by_feature_set_size_and_feature(self):
        self.assertEqual(
            self.db.lookup_strings_by_feature_set_size_and_feature(4, 'ab_1'), 
            set(['abc'])
            )
        self.assertEqual(self.db.lookup_strings_by_feature_set_size_and_feature(3, 'ab_1'), set(['ab']))
        self.assertEqual(self.db.lookup_strings_by_feature_set_size_and_feature(2, 'ab_1'), set([]))

    def test_json_save(self):
        data = self.db.to_pickle()
        assert data == b"\x80\x04\x95\xb8\x02\x00\x00\x00\x00\x00\x00}\x94(\x8c\x11feature_extractor\x94\x8c!CharacterNgramFeatureExtractor(2...8f\x94(h\t\x90\x8c\x04e$_1\x94\x8f\x94(h\t\x90uu\x8c\x11_min_feature_size\x94K\x02\x8c\x11_max_feature_size\x94K\x06u."
        with open("test.pkl", "wb") as f:
            f.write(data)
            # pickle.dump(data, f)

        with open("test.pkl", "rb") as f:
            data2 =  pickle.load(f)

        new = DictDatabase.from_json(data2)
        assert self.db == new
