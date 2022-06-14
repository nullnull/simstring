import math
from typing import Iterable

from .base import BaseMeasure


class DiceMeasure(BaseMeasure):
    def min_feature_size(self, query_size: int, alpha: float) -> int:
        return int(math.ceil(alpha * 1.0 / (2 - alpha) * query_size))

    def max_feature_size(self, query_size: int, alpha: float) -> int:
        return int(math.floor((2 - alpha) * query_size * 1.0 / alpha))

    def minimum_common_feature_count(
        self, query_size: int, y_size: int, alpha: float
    ) -> int:
        return int(math.ceil(0.5 * alpha * query_size * y_size))

    def similarity(self, X: Iterable[str], Y: Iterable[str]) -> float:
        return len(set(X) & set(Y)) * 2.0 / (len(set(X)) + len(set(Y)))
