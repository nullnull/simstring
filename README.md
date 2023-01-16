# simstring
[![PyPI - Status](https://img.shields.io/pypi/status/simstring-fast.svg)](https://pypi.org/project/simstring-fast/)
[![PyPI version](https://badge.fury.io/py/simstring-fast.svg)](https://badge.fury.io/py/simstring-fast)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/simstring-fast)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

A Python implementation of the [SimString](http://www.chokkan.org/software/simstring/index.html.en), a simple and efficient algorithm for approximate string matching.

Docs are [here](https://banking-circle-advanced-analytics.github.io/simstring-fast/)

## Features
With this library, you can extract strings/texts which has certain similarity from large amount of strings/texts. It will help you when you develop applications related to language processing.

This library supports variety of similarity functions such as Cossine similarity, Jaccard similarity, and supports Word N-gram and Character N-gram as features. You can also implement your own feature extractor easily.

SimString has the following features:

* Fast algorithm for approximate string retrieval.
* 100% exact retrieval. Although some algorithms allow misses (false positives) for faster query response, SimString is guaranteed to achieve 100% correct retrieval with fast query response.
* Unicode support.
* Extensibility. You can implement your own feature extractor easily.
* no japanese support
[Please see this paper for more details](http://www.aclweb.org/anthology/C10-1096).


## Install
```
pip install simstring-fast
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
from simstring.measure import JaccardMeasure
from simstring.database import DictDatabase
from simstring.searcher import Searcher

db = DictDatabase(WordNgramFeatureExtractor(2))
db.add('You are so cool.')

searcher = Searcher(db, JaccardMeasure())
results = searcher.search('You are cool.', 0.8)
print(results)
```

## Supported String Similarity Measures
- Cosine
- Dice
- Jaccard
- Overlap