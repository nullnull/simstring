from .base import BaseFeatureExtractor, SENTINAL_CHAR

class CharacterNgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, n=2):
        self.n = n

    def features(self, string):
        return self._each_cons(SENTINAL_CHAR + string + SENTINAL_CHAR, self.n)
