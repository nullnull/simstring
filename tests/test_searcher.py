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
        self.assertEqual(self.searcher.search('ab', 1.0), ['ab'])
        self.assertEqual(self.searcher.search('ab', 0.9), ['ab'])

    def test_search3(self):
        self.assertEqual(self.searcher.search('abc', 1.0), ['abc'])
        self.assertEqual(self.searcher.search('abc', 0.9), ['abc'])

    def test_search4(self):
        self.assertEqual(self.searcher.search('abcd', 1.0), ['abcd'])
        self.assertEqual(self.searcher.search('abcd', 0.9), ['abcd'])


    def test_ranked_search(self):
        self.assertEqual(self.searcher.ranked_search('abcd', 1.0), [(1.0, 'abcd')] )
        self.assertEqual(self.searcher.ranked_search('ab', 0.4), [(1.0, 'ab'), (0.5773502691896258, 'abc'), (0.5163977794943222, 'abcd'), (0.47140452079103173, 'abcde')])


class TestRankedSearch(TestCase):
    def setUp(self) -> None:
        db = DictDatabase(CharacterNgramFeatureExtractor(2))
        db.add('foo')
        db.add('bar')
        db.add('fooo')
        db.add('food')
        db.add('fool')
        db.add('follow')
        self.searcher = Searcher(db, CosineMeasure())

    def test_ranked_search_example1(self):
        results = self.searcher.ranked_search('fo', 0.5)
        goal = [(0.8660254037844387, 'foo'), (0.8660254037844387, 'fooo'), (0.5163977794943222, 'food'), (0.5163977794943222, 'fool')]
        self.assertEqual(results, goal)    

    def test_ranked_search_example2(self):
        results = self.searcher.ranked_search('fo', 0.6)
        goal = [(0.8660254037844387, 'foo'), (0.8660254037844387, 'fooo')]
        self.assertEqual(results, goal)    
