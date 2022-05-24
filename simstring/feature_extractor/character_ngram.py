from .base import BaseFeatureExtractor, SENTINAL_CHAR
from typing import List

class CharacterNgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, n:int=2):
        self.n = n

    def features(self, string:str) -> List[str]:
        return self._each_cons(SENTINAL_CHAR + string + SENTINAL_CHAR, self.n)
