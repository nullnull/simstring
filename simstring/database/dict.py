from collections import defaultdict
from typing import List, Set, Dict, Type
from .base import BaseDatabase

def defaultdict_set():
    return defaultdict(set)

class DictDatabase(BaseDatabase):
    def __init__(self, feature_extractor):
        self.feature_extractor = feature_extractor
        self.strings: List[str] = []
        self.feature_set_size_to_string_map: Dict[int, Set[str]] = defaultdict(set) # 3.10 and up only
        self.feature_set_size_and_feature_to_string_map: dict = defaultdict(defaultdict_set)

    def add(self, string: str):
        features = self.feature_extractor.features(string)
        size = len(features)

        self.strings.append(string)
        self.feature_set_size_to_string_map[size].add(string)

        for feature in features:
            self.feature_set_size_and_feature_to_string_map[size][feature].add(string)

    def all(self):
        return self.strings

    def lookup_strings_by_feature_set_size_and_feature(self, size: int, feature: str):
        return self.feature_set_size_and_feature_to_string_map[size][feature]

    def min_feature_size(self):
        return min(self.feature_set_size_to_string_map.keys())

    def max_feature_size(self):
        return max(self.feature_set_size_to_string_map.keys())
