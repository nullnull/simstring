# coding: utf8

from simstring.feature_extractor.ngram import NgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

string = "aiueo"

db = DictDatabase(NgramFeatureExtractor(2))
db.add(string)
db.add('aiueoo')
db.add('aiueooo')

searcher = Searcher(db, CosineMeasure())
xs = searcher.search(string, 1.0)

print(xs)
