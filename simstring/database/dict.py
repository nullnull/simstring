from collections import defaultdict
from typing import List, Set, Dict, Type
from .base import BaseDatabase
import pickle


def defaultdict_set():
    return defaultdict(set)


class DictDatabase(BaseDatabase):
    def __init__(self, feature_extractor):
        self.feature_extractor = feature_extractor
        self.strings: List[str] = []
        self.feature_set_size_to_string_map: Dict[int, Set[str]] = defaultdict(
            set
        )  # 3.10 and up only
        self.feature_set_size_and_feature_to_string_map: dict = defaultdict(
            defaultdict_set
        )

    def add(self, string: str):
        features = self.feature_extractor.features(string)
        size = len(features)

        self.strings.append(string)
        self.feature_set_size_to_string_map[size].add(string)

        for feature in features:
            self.feature_set_size_and_feature_to_string_map[size][feature].add(string)

    def all(self) -> List[str]:
        return self.strings

    def lookup_strings_by_feature_set_size_and_feature(
        self, size: int, feature: str
    ) -> Set[str]:
        return self.feature_set_size_and_feature_to_string_map[size][feature]

    def min_feature_size(self) -> int:
        return min(self.feature_set_size_to_string_map.keys())

    def max_feature_size(self) -> int:
        return max(self.feature_set_size_to_string_map.keys())

    # def __getstate__(self):
    #     """To pickle the object"""
    #     return self.__dict__

    # def __setstate__(self, d):
    #     """To unpickle the object"""
    #     self.__dict__ = d

    def save(self, filename: str):
        """Save the database to a file as defined by filename.

        Args:
            filename: Filename to save the db at. Should include file extention.

        Returns:
            None
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename: str) -> "DictDatabase":
        """Load db from a file

        Args:
            filename (str): Name of the file to load

        Returns:
            DictDatabase: the db
        """
        with open(filename, "rb") as f:
            db = pickle.load(f)
        return db

    def dumps(self) -> bytes:
        """Generate pickle byte stream

        Returns:
            _type_: _description_
        """
        return pickle.dumps(self)

    @staticmethod
    def loads(binary_data: bytes) -> "DictDatabase":
        """Load a binary string representing a database

        Initially only unpickles the data

        Args:
            binary_data (str): String of data to unpickle

        Returns:
            Model object
        """
        return pickle.loads(binary_data)
