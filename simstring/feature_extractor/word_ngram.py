from .base import BaseFeatureExtractor

SENTINAL_CHAR = " "  # non breaking space

class WordNgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, n=2, splitter=" "):
        self.n = n
        self.splitter = splitter

    def features(self, text):
        # Split text by white space.
        # If you want to extract words from text in more complicated way or using your favorite library like NLTK, please implement in your own.
        words = text.split(self.splitter)
        return self._words_ngram(words, self.n, SENTINAL_CHAR)
