SENTINAL_CHAR = " "  # non breaking space

class BaseFeatureExtractor:
    def features(self, _string):
        raise NotImplementedError()

    def _each_cons(self, xs, n):
        return [xs[i:i+n] for i in range(len(xs)-n+1)]

    def _words_ngram(self, words, n, SENTINAL_CHAR):
        return [tuple(x) for x in self._each_cons([SENTINAL_CHAR] + words + [SENTINAL_CHAR], n)]
