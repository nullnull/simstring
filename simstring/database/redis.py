
from typing import List, Set, Dict, Union
from .base import BaseDatabase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.feature_extractor.word_ngram import WordNgramFeatureExtractor

from io import BufferedWriter
from redis import Redis
from fakeredis import FakeRedis
from functools import lru_cache

import os

FeatureExtractor = Union[
            CharacterNgramFeatureExtractor, WordNgramFeatureExtractor
        ]

class RedisDatabase(BaseDatabase):
    def __init__(
        self,
        feature_extractor: FeatureExtractor,
        redis_connection: Union[Redis,FakeRedis] = FakeRedis

    ):
        self.feature_extractor = feature_extractor
        self.feature_set_size_to_string_map = redis_connection(db=0, decode_responses=True)
        self.feature_set_size_and_feature_to_string_map = redis_connection(db=1, decode_responses=True)
        self._min_feature_size = 9999999
        self._max_feature_size = 0


    @staticmethod
    def _make_key(size: int, feature: str) -> str:
        return f"{size}-{feature}"

    def add(self, string: str) -> None:
        features = self.feature_extractor.features(string)
        size = len(features)
        self.feature_set_size_to_string_map.sadd(size, string)
        
        self._min_feature_size = min(self._min_feature_size, size)
        self._max_feature_size = max(self._max_feature_size, size)

        for feature in features:
            self.feature_set_size_and_feature_to_string_map.sadd(self._make_key(size, feature), string)

    def all(self) -> List[str]:
        strings = []
        for k in self.feature_set_size_to_string_map.keys():
            strings.extend(self.feature_set_size_to_string_map.smembers(k))
        return strings

    def lookup_strings_by_feature_set_size_and_feature(
        self, size: int, feature: str
    ) -> Set[str]:
        return self.feature_set_size_and_feature_to_string_map.smembers(self._make_key(size, feature))

    def min_feature_size(self) -> int:
        return self._min_feature_size

    def max_feature_size(self) -> int:
        return self._max_feature_size



