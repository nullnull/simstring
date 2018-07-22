# coding: utf-8

from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.feature_extractor.word_ngram import WordNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.mongo import MongoDatabase
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

text = "You are so cool."

db = MongoDatabase(WordNgramFeatureExtractor(2))
db.reset_collection()
db.add(text)
db.add('You are not so cool')
db.add('Who is cool?')
print(db.all_documents())

searcher = Searcher(db, CosineMeasure())
xs = searcher.search(text, 0.8)
print(xs)
