from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher
from time import time_ns, sleep
import faker

db = DictDatabase(CharacterNgramFeatureExtractor(2))

fake = faker.Faker(['it_IT', 'en_US'])
db.add('James Walker')

for string in range(100_000):
    db.add(fake.name())

searcher = Searcher(db, CosineMeasure())

# import cython

# if cython.compiled:
#     print("Yep, I'm compiled.")
# else:
#     print("Just a lowly interpreted script.")

start = time_ns()
results = searcher.search('Jake', 0.5)
# print(results)
results = searcher.search('James', 0.8)
# print(results)
results = searcher.search('Walker', 0.3)
# print(results)
print((time_ns()-start)/10**6)


start = time_ns()
results = searcher.search('Jake', 0.5)
# print(results)
results = searcher.search('James', 0.8)
# print(results)
results = searcher.search('Walker', 0.3)
# print(results)
print((time_ns()-start)/10**6)