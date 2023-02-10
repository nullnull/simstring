# coding: utf-8

import os, sys

import numpy as np

from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.cosine import (
    CosineMeasure,
)  # , OverlapMeasure, LeftOverlapMeasure

# from simstring.database.mongo import MongoDatabase
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

from pyinstrument import Profiler

profiler = Profiler()


def output_similar_strings_of_each_line(path, measure):
    strings = []
    with open(path, "r") as lines:
        for line in lines:
            strings.append(line.rstrip("\r\n"))

    db = DictDatabase(CharacterNgramFeatureExtractor(2))
    for string in strings:
        db.add(string)

    # db.save("companies.db")

    # dbl = DictDatabase.load("companies.db")

    searcher = Searcher(db, measure)
    profiler.start()

    for string in strings:
        result = searcher.search(string, 0.8)
        # result = [str(np.round(x[0], 5)) + ' ' + x[1] for x in searcher.ranked_search(string, 0.8)]
        # print("\t".join([string, ",".join(result)]))

    profiler.stop()
    print(result)
    profiler.print()
    # profiler.open_in_browser()


measure = CosineMeasure()
output_similar_strings_of_each_line("dev/data/company_names.txt", measure)

# measure = OverlapMeasure()
# output_similar_strings_of_each_line("dev/data/company_names.txt", measure)

# measure = LeftOverlapMeasure()
# output_similar_strings_of_each_line("./data/company_names.txt", measure)
