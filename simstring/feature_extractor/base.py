from typing import List

SENTINAL_CHAR = " "  # non breaking space

class BaseFeatureExtractor:
    def features(self, _string):
        raise NotImplementedError()

    def _each_cons(self, xs:str, n:int) ->  List[str]:
        return [xs[i:i+n] for i in range(len(xs)-n+1)]

    def _words_ngram(self, words: List[str], n:int, SENTINAL_CHAR: str):
        return [tuple(x) for x in self._each_cons([SENTINAL_CHAR] + words + [SENTINAL_CHAR], n)]
