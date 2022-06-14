import os
from pymongo import MongoClient
from .base import BaseDatabase


class MongoDatabase(BaseDatabase):
    def __init__(
        self,
        feature_extractor,
        host=(os.environ["MONGO_HOST"] if "MONGO_HOST" in os.environ else "localhost"),
        port=27017,
        database="simstring",
    ):
        self.feature_extractor = feature_extractor

        client = MongoClient(host, port)
        db = client[database]
        self.collection = db.strings
        self.ensure_index()

    def add(self, string):
        features = self.feature_extractor.features(string)
        self.collection.insert_one(
            {"string": string, "features": features, "size": len(features)}
        )

    def all(self):
        return list(map(lambda x: x["string"], self.all_documents()))

    def all_documents(self):
        return list(self.collection.find())

    def ensure_index(self):
        self.collection.create_index("size")
        self.collection.create_index("features")

    def lookup_strings_by_feature_set_size_and_feature(self, size, feature):
        documents = list(self.collection.find({"size": size, "features": feature}))
        return set(list(map(lambda x: x["string"], documents)))

    def reset_collection(self):
        self.collection.remove()
        self.ensure_index()
