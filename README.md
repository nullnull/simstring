# simstring
[![PyPI - Status](https://img.shields.io/pypi/status/simstring-pure.svg)](https://pypi.org/project/simstring-pure/)
[![PyPI version](https://badge.fury.io/py/simstring-pure.svg)](https://badge.fury.io/py/simstring-pure)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/simstring-pure.svg)](https://pypi.org/project/simstring-pure/0.0.1/)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![CircleCI](https://circleci.com/gh/nullnull/simstring.svg?style=svg)](https://circleci.com/gh/nullnull/simstring)
[![Maintainability](https://api.codeclimate.com/v1/badges/66eb2018262f03ece8a3/maintainability)](https://codeclimate.com/github/nullnull/simstring/maintainability)


A Python implementation of the [SimString](http://www.chokkan.org/software/simstring/index.html.en), a simple and efficient algorithm for approximate string matching.

## Features
With this library, you can extract strings/texts which has certain similarity from large amount of strings/texts. It will help you when you develop applications related to language processing.

This library supports variety of similarity functions such as Cossine similarity, Jaccard similarity, and supports Word N-gram and Character N-gram as features. You can also implement your own feature extractor easily.

SimString has the following features:

* Fast algorithm for approximate string retrieval.
* 100% exact retrieval. Although some algorithms allow misses (false positives) for faster query response, SimString is guaranteed to achieve 100% correct retrieval with fast query response.
* Unicode support.
* Extensibility. You can implement your own feature extractor easily.
* Japanese support. [MeCab](http://taku910.github.io/mecab/)を使った形態素Nグラムをサポートしています。

[Please see this paper for more details](http://www.aclweb.org/anthology/C10-1096).


## Install
```
pip install simstring-pure
```

## Usage
```python
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

db = DictDatabase(CharacterNgramFeatureExtractor(2))
db.add('foo')
db.add('bar')
db.add('fooo')

searcher = Searcher(db, CosineMeasure())
results = searcher.search('foo', 0.8)
print(results)
# => ['foo', 'fooo']
```

If you want to use other feature, measure, and database, simply replace these classes. You can replace these classes easily by your own classes if you want.

```python
from simstring.feature_extractor.word_ngram import WordNgramFeatureExtractor
from simstring.measure.jaccard import JaccardMeasure
from simstring.database.mongo import MongoDatabase
from simstring.searcher import Searcher

db = MongoDatabase(WordNgramFeatureExtractor(2))
db.add('You are so cool.')

searcher = Searcher(db, JaccardMeasure())
results = searcher.search('You are cool.', 0.8)
print(results)
```

## Supported String Similarity Measures
- Cosine
- Dice
- Jaccard

## Run Tests
```
docker-compose run main bash -c 'source activate simstring && python -m unittest discover tests'
```

## Benchmark
* About 1ms to search strings from 5797 strings(company names).
* About 14ms to search strings from 235544 strings(unabridged dictionary).

#### search from `dev/data/company_names.txt`
```
$ python dev/benchmark.py
benchmark for using dict as database
## benchmarker:         release 4.0.1 (for python)
## python version:      3.7.0
## python compiler:     GCC 7.2.0
## python platform:     Linux-4.9.87-linuxkit-aufs-x86_64-with-debian-9.4
## python executable:   /opt/conda/envs/simstring/bin/python
## cpu model:           Intel(R) Core(TM) i7-6567U CPU @ 3.30GHz  # 3300.000 MHz
## parameters:          loop=1, cycle=1, extra=0

##                        real    (total    = user    + sys)
initialize database(5797 lines)    0.1227    0.1200    0.1200    0.0000
search text(5797 times)    6.9719    6.9400    6.8900    0.0500

## Ranking                real
initialize database(5797 lines)    0.1227  (100.0) ********************
search text(5797 times)    6.9719  (  1.8)

## Matrix                 real    [01]    [02]
[01] initialize database(5797 lines)    0.1227   100.0  5680.9
[02] search text(5797 times)    6.9719     1.8   100.0

benchmark for using Mongo as database
## benchmarker:         release 4.0.1 (for python)
## python version:      3.7.0
## python compiler:     GCC 7.2.0
## python platform:     Linux-4.9.87-linuxkit-aufs-x86_64-with-debian-9.4
## python executable:   /opt/conda/envs/simstring/bin/python
## cpu model:           Intel(R) Core(TM) i7-6567U CPU @ 3.30GHz  # 3300.000 MHz
## parameters:          loop=1, cycle=1, extra=0

##                        real    (total    = user    + sys)
initialize database(5797 lines)    4.5762    2.4900    1.9200    0.5700
search text(5797 times)  177.8401   60.9100   47.2500   13.6600

## Ranking                real
initialize database(5797 lines)    4.5762  (100.0) ********************
search text(5797 times)  177.8401  (  2.6) *

## Matrix                 real    [01]    [02]
[01] initialize database(5797 lines)    4.5762   100.0  3886.2
[02] search text(5797 times)  177.8401     2.6   100.0
```

#### search from `dev/data/unabridged_dictionary.txt`
```
$ python dev/benchmark.py
benchmark for using dict as database
## benchmarker:         release 4.0.1 (for python)
## python version:      3.7.0
## python compiler:     GCC 7.2.0
## python platform:     Linux-4.9.87-linuxkit-aufs-x86_64-with-debian-9.4
## python executable:   /opt/conda/envs/simstring/bin/python
## cpu model:           Intel(R) Core(TM) i7-6567U CPU @ 3.30GHz  # 3300.000 MHz
## parameters:          loop=1, cycle=1, extra=0

##                        real    (total    = user    + sys)
initialize database(235544 lines)    2.2576    2.2300    2.1200    0.1100
search text(10000 times)  141.0302  140.6400  139.9600    0.6800

## Ranking                real
initialize database(235544 lines)    2.2576  (100.0) ********************
search text(10000 times)  141.0302  (  1.6)

## Matrix                 real    [01]    [02]
[01] initialize database(235544 lines)    2.2576   100.0  6246.8
[02] search text(10000 times)  141.0302     1.6   100.0
```
