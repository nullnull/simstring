from .base import BaseFeatureExtractor, SENTINAL_CHAR

class CharacterNgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, n=2, try_new=False):
        self.n = n
        self.try_new = try_new

    def features(self, string):
        if self.try_new:
            list_of_ngram = self._each_cons('$' * (self.n - 1) + string + '$' * (self.n - 1), self.n)
            return self.uniquify_list(list_of_ngram) 
        else:
            return self._each_cons(SENTINAL_CHAR + string + SENTINAL_CHAR, self.n)
