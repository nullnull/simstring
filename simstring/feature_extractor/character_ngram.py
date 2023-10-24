from .base import BaseFeatureExtractor, SENTINAL_CHAR


class CharacterNgramFeatureExtractor(BaseFeatureExtractor):
    def __init__(self, n: int = 2, endmarker: str="$"):
        self.n = n
        self.endmarker = endmarker

    def features(self, string: str) -> list[str]:
        xs = self.endmarker * (self.n - 1) + string + self.endmarker * (self.n - 1) 
        list_of_ngrams = [xs[i : i + self.n] for i in range(len(xs) - self.n + 1)]

        return self.uniquify_list(list_of_ngrams)

    def __define__(self) -> str:
        "Custom representation string"
        return f"CharacterNgramFeatureExtractor({self.n})"
