import math
from .base import BaseMeasure

class JaccardMeasure(BaseMeasure):
    def min_feature_size(self, query_size, alpha):
        return int(math.ceil(alpha * query_size))

    def max_feature_size(self, query_size, alpha):
        return int(math.floor(query_size / alpha))

    def minimum_common_feature_count(self, query_size, y_size, alpha):
        return int(math.ceil(alpha * (query_size + y_size) * 1.0 / (1 + alpha)))

    def similarity(self, X, Y):
        return len(set(X) & set(Y)) * 1.0 / len(set(X) | set(Y))
