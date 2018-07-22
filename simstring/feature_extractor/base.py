class BaseFeatureExtractor:
    def features(self, _string):
        raise NotImplementedError()

    def _each_cons(self, xs, n):
        return [xs[i:i+n] for i in range(len(xs)-n+1)]
