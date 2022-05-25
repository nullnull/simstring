class BaseDatabase:
    def __init__(self, feature_extractor):
        raise NotImplementedError

    def add(self, string):
        raise NotImplementedError

    def min_feature_size(self):
        raise NotImplementedError

    def max_feature_size(self):
        raise NotImplementedError

    def lookup_strings_by_feature_set_size_and_feature(self, size, feature):
        raise NotImplementedError
