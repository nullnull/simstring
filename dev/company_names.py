# coding: utf-8

import os, sys
sys.path.append(os.getcwd())

from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.mongo import MongoDatabase
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

def output_similar_strings_of_each_line(path):
    db = DictDatabase(CharacterNgramFeatureExtractor(2))
    with open(path, 'r') as lines:
        for line in lines:
            strings = line.rstrip('\r\n')
            db.add(strings)

    searcher = Searcher(db, CosineMeasure())
    with open(path, 'r') as lines:
        for line in lines:
            strings = line.rstrip('\r\n')
            result = [str(round(x[0], 5)) + ' ' + x[1] for x in searcher.ranked_search(strings, 0.8)]
            print("\t".join([strings, ",".join(result)]))

output_similar_strings_of_each_line('./dev/data/company_names.txt')
