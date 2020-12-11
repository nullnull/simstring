# -*- coding:utf-8 -*-

from collections import defaultdict
from operator import itemgetter
from typing import List


class Searcher:
    def __init__(self, db, measure) -> None:
        self.db = db
        self.measure = measure
        self.feature_extractor = db.feature_extractor
        self.lookup_strings_result = defaultdict(dict)
 
    def search(self, query_string: str, alpha: float) -> List[str]:
        features = self.feature_extractor.features(query_string)
        lf = len(features)
        min_feature_size = self.measure.min_feature_size(lf, alpha)
        max_feature_size = self.measure.max_feature_size(lf, alpha)
        results = []

        for candidate_feature_size in range(min_feature_size, max_feature_size + 1):
            tau = self.__min_overlap(lf, candidate_feature_size, alpha)
            results.extend(self.__overlap_join(features, tau, candidate_feature_size))
        return results

    def ranked_search(self, query_string: str, alpha: float) -> List[str]:
        results = self.search(query_string, alpha)
        features = self.feature_extractor.features(query_string)
        results_with_score = list(map(lambda x: [self.measure.similarity(features, self.feature_extractor.features(x)), x], results))
        return sorted(results_with_score, key=lambda x: (-x[0], x[1]))

    def __min_overlap(self, query_size, candidate_feature_size, alpha: float):
        return self.measure.minimum_common_feature_count(query_size, candidate_feature_size, alpha)
    
    def __overlap_join(self, features, tau, candidate_feature_size):
        query_feature_size = len(features)
        sorted_features = sorted(features, key=lambda x: len(self.__lookup_strings_by_feature_set_size_and_feature(candidate_feature_size, x)))
        candidate_string_to_matched_count = defaultdict(int)
        results = []
        for feature in sorted_features[0:query_feature_size - tau + 1]:
            for s in self.__lookup_strings_by_feature_set_size_and_feature(candidate_feature_size, feature):
                candidate_string_to_matched_count[s] += 1

        for s, value in candidate_string_to_matched_count.items():
            for i in range(query_feature_size - tau + 1, query_feature_size):
                feature = sorted_features[i]
                if s in self.__lookup_strings_by_feature_set_size_and_feature(candidate_feature_size, feature):
                    candidate_string_to_matched_count[s] += 1
                if candidate_string_to_matched_count[s] >= tau:
                    results.append(s)
                    break
                remaining_feature_count = query_feature_size - i - 1
                if value + remaining_feature_count < tau:
                    break
        return results

    def __lookup_strings_by_feature_set_size_and_feature(self, feature_size, feature):
        if feature not in self.lookup_strings_result[feature_size]:
            self.lookup_strings_result[feature_size][feature] = self.db.lookup_strings_by_feature_set_size_and_feature(feature_size, feature)
        return self.lookup_strings_result[feature_size][feature]
