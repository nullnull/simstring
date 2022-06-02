# coding: utf-8

import os, sys
sys.path.append(os.getcwd())
import numpy as np

from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
# from simstring.database.mongo import MongoDatabase
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

def output_similar_strings_of_each_line(path):
    strings = []
    with open(path, 'r') as lines:
        for line in lines:
            strings.append(line.rstrip('\r\n'))


    db = DictDatabase(CharacterNgramFeatureExtractor(2))
    for string in strings:
        db.add(string)

            
    searcher = Searcher(db, CosineMeasure())
    for string in strings:
        result = searcher.search(string, 0.8)
        print("\t".join([string, ",".join(result)]))

output_similar_strings_of_each_line('./dev/data/company_names.txt')
