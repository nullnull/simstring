
from simstring.database.dict import DictDatabase
from simstring.feature_extractor.ngram import NgramFeatureExtractor
from simstring.searcher import Searcher
from simstring.measure.cosine import CosineMeasure

x = NgramFeatureExtractor();
print x.features("aiueo")

#
# db = SimpleDatabase(NgramFeatureExtractor())
# db.add("hoo")
#
# searcher = Searcher(db, CosineMeasure())
# searcher.search('hoo', 1.0)
