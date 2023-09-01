# -*- coding:utf-8 -*-

from unittest import TestCase
from simstring.database.dict import DictDatabase
from simstring.database.disk import DiskDatabase
from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
import os
import shutil
from multiprocessing import Pool, cpu_count


from faker import Faker
import random
from tqdm import tqdm

class TestComparability(TestCase):
    f = Faker()
    Faker.seed(0)

    def setUp(self):
        self.strings = [self.f.name().replace('-',' ') for _ in range(100)]

        self.dict_db = DictDatabase(CharacterNgramFeatureExtractor(2))
        for string in self.strings:
            self.dict_db.add(string)

        self.disk_db =  DiskDatabase(CharacterNgramFeatureExtractor(2), path=f"tmp_db_for_tests-{random.randint(1000,10000)}")

        with  Pool(processes=8) as pool:
            for _ in tqdm(pool.imap_unordered(self.disk_db.add, self.strings), total=len(self.strings)):
                pass

    def tearDown(self) -> None:
        try:
            shutil.rmtree(self.disk_db.path)
        except:
            pass
        return super().tearDown()
    
    def test_strings(self):
        self.assertEqual(set(self.dict_db.all()), set(self.disk_db.all()))


    def test_equivalence_disk_to_dict(self):
        for key in self.disk_db.feature_set_size_to_string_map.iterkeys():
            self.assertEqual(self.dict_db.feature_set_size_to_string_map[key], self.disk_db.feature_set_size_to_string_map[key])

        for key in self.disk_db.feature_set_size_and_feature_to_string_map.iterkeys():
            disk_val = self.disk_db.feature_set_size_and_feature_to_string_map[key]
            k1, k2 = key.split('-')
            dict_val = self.dict_db.feature_set_size_and_feature_to_string_map[int(k1)][k2]
            self.assertEqual(disk_val, dict_val)


    def test_equivalence_dict_to_disk(self):
        for size, value in self.dict_db.feature_set_size_and_feature_to_string_map.items():
            for feature, dict_value in value.items():
                disk_value = self.disk_db.get_feature_set_size_and_feature_to_string_map(size, feature)
                self.assertEqual(dict_value, disk_value)

        for size, string_set in self.dict_db.feature_set_size_to_string_map.items():
            self.assertEqual(string_set, self.disk_db.feature_set_size_to_string_map[size])
