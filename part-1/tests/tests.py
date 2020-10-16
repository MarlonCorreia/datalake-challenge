import sys
sys.path.insert(0, '../src')
import unittest
from classes import Object_json
import hashlib
import json

class Test_Json(unittest.TestCase):

    def test_hash(self):
        json_body = {"id": 1, "name": "name"}
        object_json = Object_json(json_body)

        hash_object = object_json.get_body_hash()

        self.assertEqual(hash_object, '53ae3ca6bc2b6ffb442890ee5def77d9d9df0417')

if __name__ == '__main__':
    unittest.main()
