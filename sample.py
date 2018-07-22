# coding: utf-8

from simstring.feature_extractor.ngram import NgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.mongo import MongoDatabase
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

string = "aiueo"

db = MongoDatabase(NgramFeatureExtractor(2))
db.reset_collection()
db.add(string)
db.add('aiueoo')
db.add('aiueooo')
print(db.all_documents())

searcher = Searcher(db, CosineMeasure())
xs = searcher.search(string, 1.0)
print(xs)
