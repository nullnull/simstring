# coding: utf8

from simstring.feature_extractor.ngram import NgramFeatureExtractor
feature_extractor = NgramFeatureExtractor(2)
features = feature_extractor.features("aiueo")
print features

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
db = DictDatabase(feature_extractor)

db.add('aiueo')
db.add('aiueoo')
db.add('aiueooo')
print db.strings
print db.min_feature_size
print db.max_feature_size
print db.lookup_strings_by_feature_set_size_and_feature(5, features[0])


from simstring.searcher import Searcher


#
# db = SimpleDatabase(NgramFeatureExtractor())
# db.add("hoo")
#
# searcher = Searcher(db, CosineMeasure())
# searcher.search('hoo', 1.0)
