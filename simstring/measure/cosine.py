import math
from typing import Iterable
from .base import BaseMeasure


class CosineMeasure(BaseMeasure):
    def min_feature_size(self, query_size: int, alpha: float) -> int:
        return int(math.ceil(alpha * alpha * query_size))

    def max_feature_size(self, query_size: int, alpha: float) -> int:
        return int(math.floor(query_size / (alpha * alpha)))

    def minimum_common_feature_count(
        self, query_size: int, y_size: int, alpha: float
    ) -> int:
        return int(math.ceil(alpha * math.sqrt(query_size * y_size)))

    def similarity(self, X: Iterable[str], Y: Iterable[str]) -> float:
        return len(set(X) & set(Y)) / math.sqrt(len(set(X)) * len(set(Y)))
