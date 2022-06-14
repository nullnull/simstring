# coding: utf-8

import os, sys

sys.path.append(os.getcwd())
import numpy as np

from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure import CosineMeasure, OverlapMeasure, LeftOverlapMeasure

# from simstring.database.mongo import MongoDatabase
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher
import numpy as np

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

    db.save("companies.db")

    dbl = DictDatabase.load("companies.db")

    searcher = Searcher(dbl, measure)
    profiler.start()

    for string in strings:
        result = searcher.search(string, 0.8)
        # result = [str(np.round(x[0], 5)) + ' ' + x[1] for x in searcher.ranked_search(string, 0.8)]
        # print("\t".join([string, ",".join(result)]))

    profiler.stop()

    profiler.print()
    profiler.open_in_browser()


measure = CosineMeasure()
output_similar_strings_of_each_line("./data/company_names.txt", measure)

measure = OverlapMeasure()
output_similar_strings_of_each_line("./data/company_names.txt", measure)

measure = LeftOverlapMeasure()
output_similar_strings_of_each_line("./data/company_names.txt", measure)
