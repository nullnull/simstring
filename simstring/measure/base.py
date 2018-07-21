class BaseMeasure:
    def min_feature_size(self, _query_size, _alpha):
        raise 'Not Implemented'

    def max_feature_size(self, _query_size, _alpha):
        raise 'Not Implemented'

    def minimum_common_feature_count(self, _query_size, _y_size, _alpha):
        raise 'Not Implemented'

    def similarity(self, X, Y):
        raise 'Not Implemented'
