import sys
sys.path.insert(0, '../src')
import unittest
from classes import Object_json
from cache import fake_redis_insert_cache, fake_redis_check_if_in_cache
import hashlib
import json

class Test_Json_class(unittest.TestCase):

    def setUp(self):
        self.json_body = {"id": 1, "name": "name"}
        self.expected_hash = '53ae3ca6bc2b6ffb442890ee5def77d9d9df0417'
        self.dumped_json = json.dumps(self.json_body, sort_keys = True).encode("utf-8")

    def test_hash(self):
        """Testing hashing creation in class method"""

        object_json = Object_json(self.json_body)
        hash_object = object_json.get_body_hash()

        self.assertEqual(hash_object, self.expected_hash)
    
    def test_dumped_json(self):
        """Testing json.dumps in class method"""
        
        object_json = Object_json(self.json_body)
        response = object_json.dump_json()

        self.assertEqual(response, self.dumped_json)


class Test_redis(unittest.TestCase):
    
    def setUp(self):
        self.hash_not_cached_check_test = '53ae3ca6bc2b6ffb442890ee5def77d9d9df0417'
        self.hash_not_cached_insert_test = '3c14176035a9903556a0655650226d0a38685067'
        self.hash_cached = 'f359629516959b5346e9ae2bf5383f18dbeff6fb'
        fake_redis_insert_cache('f359629516959b5346e9ae2bf5383f18dbeff6fb')

    def test_insert(self):
        """Testing inser methodo in fake redis"""

        fake_redis_insert_cache(self.hash_not_cached_insert_test)
        response = fake_redis_check_if_in_cache(self.hash_not_cached_insert_test)
        
        self.assertEqual(response, True)

    def test_check_cache_case_1(self):
        """Case 1: passing hash that is not cached"""

        response = fake_redis_check_if_in_cache(self.hash_not_cached_check_test)

        self.assertEqual(response, False)

    
    def test_check_cache_case_2(self):
        """Case 1: passing hash that is cached"""

        response = fake_redis_check_if_in_cache(self.hash_cached)

        self.assertEqual(response, True)


if __name__ == '__main__':
    unittest.main() 
