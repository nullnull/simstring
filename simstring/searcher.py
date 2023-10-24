# -*- coding:utf-8 -*-
from collections import defaultdict, OrderedDict
from typing import OrderedDict as OrderedDictType


class Searcher:
    def __init__(self, db, measure) -> None:
        """Searcher class

        This is the main way of interacting with the simsting search.

        Args:
            db (database): A database, can be a dict or mongo one as defined by the `database` modeule
            measure (measure): The similarity measure as defined by `measure`
        """
        self.db = db
        self.measure = measure
        self.feature_extractor = db.feature_extractor
        self.lookup_strings_result: dict = defaultdict(dict)

    def search(self, query_string: str, alpha: float) -> list[str]:
        features = self.feature_extractor.features(query_string)
        lf = len(features)
        min_feature_size = self.measure.min_feature_size(lf, alpha)
        max_feature_size = self.measure.max_feature_size(lf, alpha)
        results = []

        for candidate_feature_size in range(min_feature_size, max_feature_size + 1):
            tau = self.__min_overlap(lf, candidate_feature_size, alpha)
            results.extend(self.__overlap_join(features, tau, candidate_feature_size))
        return results

    def ranked_search(
        self, query_string: str, alpha: float
    ) -> OrderedDictType[str, float]:
        """Find matches for sting returning multiple ranked matches.

        Args:
            query_string (str): string to match
            alpha (float): min similarity

        Returns:
            OrderedDict[str, float]: Matched string with similarity
        """
        results = self.search(query_string, alpha)
        features = self.feature_extractor.features(query_string)
        results_with_score = list(
            map(
                lambda x: [
                    self.measure.similarity(
                        features, self.feature_extractor.features(x)
                    ),
                    x,
                ],
                results,
            )
        )
        return OrderedDict(
            (
                (name, score)
                for score, name in sorted(
                    results_with_score, key=lambda x: (-x[0], x[1])
                )
            )
        )

    def __min_overlap(
        self, query_size: int, candidate_feature_size: int, alpha: float
    ) -> int:
        return self.measure.minimum_common_feature_count(
            query_size, candidate_feature_size, alpha
        )

    def __overlap_join(
        self, features: list[str], tau: int, candidate_feature_size: int
    ) -> list[str]:
        query_feature_size = len(features)

        features_mapped_to_lookup_strings_sets = {
            x: self.__lookup_strings_by_feature_set_size_and_feature(
                candidate_feature_size, x
            )
            for x in features
        }

        features.sort(key=lambda x: len(features_mapped_to_lookup_strings_sets[x]))

        # candidate_string_to_matched_count : dict[str,int] = defaultdict(int) # Only in 3.10 and later
        candidate_string_to_matched_count: dict[str, int] = dict()
        results = []
        for feature in features[0 : query_feature_size - tau + 1]:
            for s in features_mapped_to_lookup_strings_sets[feature]:
                if s not in candidate_string_to_matched_count:
                    candidate_string_to_matched_count[s] = 0
                candidate_string_to_matched_count[s] += 1

        # The next loop does not run for tau = 1, hence candidates are never checked, while all satisfies the criteria
        if tau == 1:
            results = list(candidate_string_to_matched_count.keys())

        for (
            candidate,
            candidate_match_count,
        ) in candidate_string_to_matched_count.items():
            for i in range(query_feature_size - tau + 1, query_feature_size):
                feature = features[i]
                if candidate in features_mapped_to_lookup_strings_sets[feature]:
                    candidate_match_count += 1
                if candidate_match_count >= tau:
                    results.append(candidate)
                    break
                remaining_feature_count = query_feature_size - i - 1
                if candidate_match_count + remaining_feature_count < tau:
                    break

        return results

    def __lookup_strings_by_feature_set_size_and_feature(
        self, feature_size: int, feature: str
    ) -> set[str]:
        if feature not in self.lookup_strings_result[feature_size]:
            self.lookup_strings_result[feature_size][
                feature
            ] = self.db.lookup_strings_by_feature_set_size_and_feature(
                feature_size, feature
            )
        return self.lookup_strings_result[feature_size][feature]
