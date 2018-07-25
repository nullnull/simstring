# coding: utf-8

import os, sys
sys.path.append(os.getcwd())
from benchmarker import Benchmarker

from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.mongo import MongoDatabase
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

SEARCH_COUNT_LIMIT = 10**4

def output_similar_strings_of_each_line(path, Database):
    number_of_lines = len(open(path).readlines())

    with Benchmarker(width=20) as bench:
        db = Database(CharacterNgramFeatureExtractor(2))
        @bench("initialize database({0} lines)".format(number_of_lines))
        def _(bm):
            with open(path, 'r') as lines:
                for line in lines:
                    strings = line.rstrip('\r\n')
                    db.add(strings)

        @bench("search text({0} times)".format(min(number_of_lines, SEARCH_COUNT_LIMIT)))
        def _(bm):
            searcher = Searcher(db, CosineMeasure())
            with open(path, 'r') as lines:
                for i, line in enumerate(lines):
                    if i >= SEARCH_COUNT_LIMIT:
                        break
                    strings = line.rstrip('\r\n')
                    result = searcher.search(strings, 0.8)

print('benchmark for using dict as database')
output_similar_strings_of_each_line('./dev/data/company_names.txt', DictDatabase)
print('benchmark for using Mongo as database')
output_similar_strings_of_each_line('./dev/data/company_names.txt', MongoDatabase)
