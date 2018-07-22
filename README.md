# simstring
A Python implementation of the SimString, a simple and efficient algorithm for approximate string matching.

## References
- SimString website: http://www.chokkan.org/software/simstring/
- SimString reference implementation (C++): https://github.com/chokkan/simstring
- SimString paper: http://www.aclweb.org/anthology/C10-1096

## Install
```
pip install simstring
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
python -m unittest discover tests
```
n
