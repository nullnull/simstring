# coding: utf8

from simstring.feature_extractor.ngram import NgramFeatureExtractor
feature_extractor = NgramFeatureExtractor(2);
print feature_extractor.features(u"あいうえお")

from simstring.measure.cosine import CosineMeasure


from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher


#
# db = SimpleDatabase(NgramFeatureExtractor())
# db.add("hoo")
#
# searcher = Searcher(db, CosineMeasure())
# searcher.search('hoo', 1.0)
