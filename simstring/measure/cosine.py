import math
from .base import BaseMeasure

class CosineMeasure(BaseMeasure):
    def min_feature_size(self, query_size, alpha):
        return int(math.ceil(alpha * alpha * query_size))

    def max_feature_size(self, query_size, alpha):
        return int(math.floor(query_size * 1.0 / (alpha * alpha)))

    def minimum_common_feature_count(self, query_size, y_size, alpha):
        return int(math.ceil(alpha * math.sqrt(query_size * y_size)))

    def similarity(self, X, Y):
        return len(set(X) & set(Y)) * 1.0 / math.sqrt(len(set(X)) * len(set(Y)))
