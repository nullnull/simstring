from collections import defaultdict
from .base import BaseDatabase

def defaultdict_set():
    return defaultdict(set)

class DictDatabase(BaseDatabase):
    def __init__(self, feature_extractor):
        self.feature_extractor = feature_extractor
        self.strings = []
        self.feature_set_size_to_string_map = defaultdict(set)
        self.feature_set_size_and_feature_to_string_map = defaultdict(defaultdict_set)

    def add(self, string):
        features = self.feature_extractor.features(string)
        size = len(features)

        self.strings.append(string)
        self.feature_set_size_to_string_map[size].add(string)
        for feature in features:
            self.feature_set_size_and_feature_to_string_map[size][feature].add(string)

    def all(self):
        return self.strings

    def lookup_strings_by_feature_set_size_and_feature(self, size, feature):
        return self.feature_set_size_and_feature_to_string_map[size][feature]

    def min_feature_size(self):
        return min(self.feature_set_size_to_string_map.keys())

    def max_feature_size(self):
        return max(self.feature_set_size_to_string_map.keys())
