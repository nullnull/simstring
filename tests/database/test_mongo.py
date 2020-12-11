from unittest import TestCase
from simstring.database.mongo import MongoDatabase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
import pytest


@pytest.mark.skip(reason="Currently not testing on Mongo")
class TestDict(TestCase):
    strings = ['a', 'ab', 'abc', 'abcd', 'abcde']

    def setUp(self):
        self.db = MongoDatabase(CharacterNgramFeatureExtractor(2), database='simstring-test')
        self.db.reset_collection()
        for string in self.strings:
            self.db.add(string)

    def test_strings(self):
        self.assertEqual(self.db.all(), self.strings)

    def test_lookup_strings_by_feature_set_size_and_feature(self):
        self.assertEqual(self.db.lookup_strings_by_feature_set_size_and_feature(4, 'ab'), set(['abc']))
        self.assertEqual(self.db.lookup_strings_by_feature_set_size_and_feature(3, 'ab'), set(['ab']))
        self.assertEqual(self.db.lookup_strings_by_feature_set_size_and_feature(2, 'ab'), set())
