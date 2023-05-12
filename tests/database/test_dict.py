# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.database.dict import DictDatabase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
import pickle
import os


class TestDict(TestCase):
    strings = ["a", "ab", "abc", "abcd", "abcde"]

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
            self.db.lookup_strings_by_feature_set_size_and_feature(4, "ab_1"),
            set(["abc"]),
        )
        self.assertEqual(
            self.db.lookup_strings_by_feature_set_size_and_feature(3, "ab_1"),
            set(["ab"]),
        )
        self.assertEqual(
            self.db.lookup_strings_by_feature_set_size_and_feature(2, "ab_1"), set([])
        )

    def test_json_save(self):
        with open("test.pkl", "wb") as f:
            self.db.to_pickle(f)

        with open("test.pkl", "rb") as f:
            data2 = pickle.load(f)

        new = DictDatabase.from_dict(data2)
        # self.assertEqual(self.db , new)
        self.assertEqual(self.db._min_feature_size, new._min_feature_size)
        self.assertEqual(self.db._max_feature_size, new._max_feature_size)
        self.assertEqual(
            self.db.feature_extractor.__class__, new.feature_extractor.__class__
        )
        self.assertEqual(self.db.feature_extractor.n, new.feature_extractor.n)
        self.assertEqual(
            self.db.feature_set_size_to_string_map, new.feature_set_size_to_string_map
        )
        self.assertEqual(
            self.db.feature_set_size_and_feature_to_string_map,
            new.feature_set_size_and_feature_to_string_map,
        )

        os.remove("test.pkl")
