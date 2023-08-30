# coding: utf-8
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.measure.overlap import OverlapMeasure, LeftOverlapMeasure

from simstring.database.dict import DictDatabase
from simstring.database.disk import DiskDatabase
from simstring.searcher import Searcher
from tqdm import tqdm
from time import time
from multiprocessing import Pool, cpu_count

from pyinstrument import Profiler

profiler = Profiler()


def output_similar_strings_of_each_line(path, measures, db_cls):
    strings = []
    with open(path, "r") as lines:
        for line in lines:
            strings.append(line.rstrip("\r\n").strip().lower())
    
    db = make_db(db_cls, strings[:10_000])
    # profiler.print()

    for measure in measures:
        searcher = Searcher(db, measure)

        for string in strings:
            result = searcher.search(string, 0.8)

        print(result)
        print(db_cls.__name__, measure.__class__.__name__)


def make_db(db_cls, strings):
    db = db_cls(CharacterNgramFeatureExtractor(2))
    # profiler.start()
    start = time()
    print('started')

    # for string in tqdm(strings):
    #     db.add(string)
    with Pool(8) as p:  
       p.map(db.add,strings)
    # profiler.stop()
    print(time()-start)
    # profiler.print()
    return db

if __name__ =="__main__":
    file = "dev/data/company_names.txt"
    # file = "dev/data/unabridged_dictionary.txt"
    # file = "dev/data/addresses.csv"
    # measures =  [CosineMeasure(), OverlapMeasure(), LeftOverlapMeasure()]
    measures =  [CosineMeasure()]
    for db_cls in [DiskDatabase]:
        output_similar_strings_of_each_line(file, measures, db_cls)

    # for db_cls in [DictDatabase,DiskDatabase]:
    #         output_similar_strings_of_each_line("dev/data/unabridged_dictionary2.txt", measures, db_cls)
    # with open("profiler_add.html","w") as file:
    #     file.write(profiler.output_html())