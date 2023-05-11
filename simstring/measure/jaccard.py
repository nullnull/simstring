import math
from typing import Iterable


class JaccardMeasure:
    def min_feature_size(self, query_size: int, alpha: float) -> int:
        return int(math.ceil(alpha * query_size))

    def max_feature_size(self, query_size: int, alpha: float) -> int:
        return int(math.floor(query_size / alpha))

    def minimum_common_feature_count(
        self, query_size: int, y_size: int, alpha: float
    ) -> int:
        return int(math.ceil(alpha * (query_size + y_size) * 1.0 / (1 + alpha)))

    def similarity(self, X: Iterable[str], Y: Iterable[str]) -> float:
        return len(set(X) & set(Y)) * 1.0 / len(set(X) | set(Y))
