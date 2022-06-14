import math
from typing import Iterable
from .base import BaseMeasure


class OverlapMeasure(BaseMeasure):
    def __init__(self, db=None, maxsize: int = 100) -> None:
        super().__init__()
        if db:
            self.maxsize = db.max_feature_size()
        else:
            self.maxsize = maxsize

    def min_feature_size(self, query_size, alpha) -> int:
        # return 1 # Not sure the below isn't sufficient
        return math.floor(query_size * alpha) or 1

    def max_feature_size(self, query_size, alpha) -> int:
        return self.maxsize

    def minimum_common_feature_count(
        self, query_size: int, y_size: int, alpha: float
    ) -> int:
        return int(math.ceil(alpha * min(query_size, y_size)))

    def similarity(self, X: Iterable[str], Y: Iterable[str]) -> int:
        return min(len(set(X)), len(set(Y)))


class LeftOverlapMeasure(BaseMeasure):
    def __init__(self, db=None, maxsize: int = 100) -> None:
        super().__init__()
        if db:
            self.maxsize = db.max_feature_size()
        else:
            self.maxsize = maxsize

    def min_feature_size(self, query_size, alpha) -> int:
        return math.floor(query_size * alpha) or 1

    def max_feature_size(self, query_size, alpha) -> int:
        return self.maxsize

    def minimum_common_feature_count(
        self, query_size: int, y_size: int, alpha: float
    ) -> int:
        return math.floor(query_size * alpha) or 1

    def similarity(self, X: Iterable[str], Y: Iterable[str]) -> float:
        return 1 - len(set(X) - set(Y)) / len(set(X))
