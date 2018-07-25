import math
from .base import BaseMeasure

class DiceMeasure(BaseMeasure):
    def min_feature_size(self, query_size, alpha):
        return int(math.ceil(alpha * 1.0 / (2 - alpha) * query_size))

    def max_feature_size(self, query_size, alpha):
        return int(math.floor((2 - alpha) * query_size * 1.0 / alpha))

    def minimum_common_feature_count(self, query_size, y_size, alpha):
        return int(math.ceil(0.5 * alpha * query_size * y_size))

    def similarity(self, X, Y):
        return len(set(X) & set(Y)) * 2.0 / (len(set(X)) + len(set(Y)))
