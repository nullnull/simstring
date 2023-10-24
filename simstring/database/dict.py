from collections import defaultdict
from typing import Union
from .base import BaseDatabase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.feature_extractor.word_ngram import WordNgramFeatureExtractor
import pickle
import ast
from io import BufferedWriter


def defaultdict_set():
    return defaultdict(set)


class DictDatabase(BaseDatabase):
    def __init__(
        self,
        feature_extractor: Union[
            CharacterNgramFeatureExtractor, WordNgramFeatureExtractor
        ],
    ):
        self.feature_extractor = feature_extractor
        self.strings: list[str] = []
        self.feature_set_size_to_string_map: dict[int, set[str]] = dict()
        self.feature_set_size_and_feature_to_string_map: dict = defaultdict(
            defaultdict_set
        )
        self._min_feature_size = 9999999
        self._max_feature_size = 0

    def add(self, string: str) -> None:
        features = self.feature_extractor.features(string)
        size = len(features)

        self.strings.append(string)

        if size not in self.feature_set_size_to_string_map:
            self.feature_set_size_to_string_map[size] = set()

        self.feature_set_size_to_string_map[size].add(string)

        for feature in features:
            self.feature_set_size_and_feature_to_string_map[size][feature].add(string)

    def all(self) -> list[str]:
        return self.strings

    def lookup_strings_by_feature_set_size_and_feature(
        self, size: int, feature: str
    ) -> set[str]:
        return self.feature_set_size_and_feature_to_string_map[size][feature]

    def to_pickle(self, f: BufferedWriter) -> None:
        """Hack to get object savable with mypyc

        Save a db object to pickle with:

        >>> with open("test.pkl", "wb") as f:
        ...     db.to_pickle(f)

        Args:
            f (BufferedWriter): File object writer, where to save the data
        """
        data = {
            "feature_extractor": self.feature_extractor.__define__(),
            "strings": self.strings,
            "feature_set_size_to_string_map": self.feature_set_size_to_string_map,
            "feature_set_size_and_feature_to_string_map": self.feature_set_size_and_feature_to_string_map,
            "_min_feature_size": self._min_feature_size,
            "_max_feature_size": self._max_feature_size,
        }
        pickle.dump(data, f)

    @staticmethod
    def from_dict(data: dict) -> "DictDatabase":
        """Hack to get object loadable with mypyc

        Careful, this runs eval on data["feature_extractor"], so only use pickles you trust.

        Load a saved DB as a dict and then instatiate an object from that dict:

        Example:
        >>> with open("test.pkl", "rb") as f:
        ...     data = pickle.load(f)

        >>> new = DictDatabase.from_dict(data)

        Args:
            data (dict): A dictionary as created by `to_pickle`

        """
        obj = DictDatabase(eval(data["feature_extractor"]))
        obj.strings = data["strings"]
        obj.feature_set_size_to_string_map.update(
            data["feature_set_size_to_string_map"]
        )
        obj.feature_set_size_and_feature_to_string_map.update(
            data["feature_set_size_and_feature_to_string_map"]
        )
        obj._min_feature_size = data["_min_feature_size"]
        obj._max_feature_size = data["_max_feature_size"]
        return obj

    def save(self, filename: str) -> None:
        """Save the database to a file as defined by filename.

        Args:
            filename: Filename to save the db at. Should include file extension.

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
