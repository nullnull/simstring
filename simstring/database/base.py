class BaseDatabase:
    def __init__(self, feature_extractor):
        raise 'Not Implemented'

    def add(self, string):
        raise 'Not Implemented'

    def min_feature_size(self):
        raise 'Not Implemented'

    def max_feature_size(self):
        raise 'Not Implemented'

    def lookup_strings_by_feature_set_size_and_feature(self, size, feature):
        raise 'Not Implemented'
