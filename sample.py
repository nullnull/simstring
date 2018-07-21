# coding: utf8

from simstring.feature_extractor.ngram import NgramFeatureExtractor
feature_extractor = NgramFeatureExtractor(2)
print feature_extractor.features(u"あいうえお")

from simstring.measure.cosine import CosineMeasure
measure = CosineMeasure()

query_size = 10
alpha = 0.8
y_size = 5
X = 'aiueo'
Y = 'aiueo'
print measure.min_feature_size(query_size, alpha)
print measure.max_feature_size(query_size, alpha)
print measure.minimum_common_feature_count(query_size, y_size, alpha)
print measure.similarity(X, Y)

from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher


#
# db = SimpleDatabase(NgramFeatureExtractor())
# db.add("hoo")
#
# searcher = Searcher(db, CosineMeasure())
# searcher.search('hoo', 1.0)
