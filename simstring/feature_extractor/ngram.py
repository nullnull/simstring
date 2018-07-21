from base import BaseFeatureExtractor

SENTINAL_CHAR = " "  # non breaking space

def each_cons(x, size):
    return [x[i:i+size] for i in range(len(x)-size+1)]

class NgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, n=2):
        self.n = n

    def features(self, string):
        return each_cons(SENTINAL_CHAR + string + SENTINAL_CHAR, self.n)
