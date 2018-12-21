from simstring.measure.base import BaseMeasure
from sys import maxsize
import math

class OverlapMeasure(BaseMeasure):
    def min_feature_size(self, query_size, alpha):
        return 1

    def max_feature_size(self, query_size, alpha):
        return maxsize

    def minimum_common_feature_count(self, query_size, y_size, alpha):
        print(query_size, y_size, alpha)
        return int(math.ceil(alpha * min(query_size, y_size)))

    def similarity(self, X, Y):
        return min(len(set(X)), len(set(Y)))
