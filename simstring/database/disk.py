
from typing import Union
from .base import BaseDatabase
from collections import defaultdict

from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.feature_extractor.word_ngram import WordNgramFeatureExtractor

from io import BufferedWriter
import diskcache as dc
from multiprocessing import Pool, cpu_count

from functools import lru_cache

import os

FeatureExtractor = Union[
            CharacterNgramFeatureExtractor, WordNgramFeatureExtractor
        ]

class DiskDatabase(BaseDatabase):
    def __init__(
        self,
        feature_extractor: FeatureExtractor,
        path:str= 'tmp'
    ):
        self.feature_extractor = feature_extractor
        self.feature_set_size_to_string_map: dc.Cache = dc.Cache(os.path.join(path,'feature_set_size_to_string_map'))
        self.feature_set_size_and_feature_to_string_map: dc.Cache = dc.Cache(os.path.join(path,'feature_set_size_and_feature_to_string_map'))
        self.path = path

    @staticmethod
    def _make_key(size: int, feature: str) -> str:
        return f"{size}-{feature}"

    def add_feature_set_size_and_feature_to_string_map(self, size, feature, string)-> None:
        key = self._make_key(size, feature)
        with self.feature_set_size_and_feature_to_string_map.transact():
            if key in self.feature_set_size_and_feature_to_string_map:
                d = self.feature_set_size_and_feature_to_string_map[key]
                if string in d:
                    return
            else:
                d = set()

            d.add(string)
            self.feature_set_size_and_feature_to_string_map[key] = d
    
    def get_feature_set_size_and_feature_to_string_map(self, size: int, feature: str
    ) -> set[str]:
        try:
            return self.feature_set_size_and_feature_to_string_map[self._make_key(size,feature)]
        except KeyError:
            return set() 

    def add(self, string: str) -> None:
        features = self.feature_extractor.features(string)

        size = len(features)
        with self.feature_set_size_to_string_map.transact():  
            if size not in self.feature_set_size_to_string_map:
                size_to_string_map = set()
            else:
                size_to_string_map = self.feature_set_size_to_string_map[size]

            size_to_string_map.add(string)
            self.feature_set_size_to_string_map[size] = size_to_string_map
        
        for feature in features:
            self.add_feature_set_size_and_feature_to_string_map(size, feature, string)

    def all(self) -> list[str]:
        strings = []
        for k in self.feature_set_size_to_string_map.iterkeys():
            strings.extend(self.feature_set_size_to_string_map[k])
        return strings

    def lookup_strings_by_feature_set_size_and_feature(
        self, size: int, feature: str
    ) -> set[str]:
        return self.get_feature_set_size_and_feature_to_string_map(size,feature)