from typing import Dict, List
from collections import defaultdict

SENTINAL_CHAR = " "  # non breaking space


class BaseFeatureExtractor:
    def features(self, string: str) -> List[str]:
        raise NotImplementedError()

    def _each_cons(self, xs, n: int) -> List[str]:
        return [xs[i : i + n] for i in range(len(xs) - n + 1)]

    def _words_ngram(self, words: List[str], n: int, SENTINAL_CHAR: str):
        return [
            tuple(x)
            for x in self._each_cons([SENTINAL_CHAR] + words + [SENTINAL_CHAR], n)
        ]

    def uniquify_list(self, non_unique_list: List[str]) -> List[str]:
        """Function to ensure a list has only unique values

            All values get "_n" appended where n is the number that entry occured
        Args:
            non_unique_list (list): list to be uniquefied

        Returns:
            list: uniquified list

        Example:
            ['a', 'b', 'a'] -> ['a_1', 'b_1', 'a_2']

        """
        counter: Dict[str, int] = defaultdict(int)
        unique_list = []
        for val in non_unique_list:
            counter[val] += 1
            unique_list.append(f"{val}_{counter[val]}")

        return unique_list

    def __define__(self) -> str:
        "Custom representation string"
        raise NotImplementedError()
