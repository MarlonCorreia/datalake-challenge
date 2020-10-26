import json
import hashlib
from cache import check_if_in_cache

class Object_json():

    def __init__(self, json_body):
        self.json_body = json_body

    def dump_json(self):
        dumped_json = json.dumps(self.json_body, sort_keys = True).encode("utf-8")
        
        return dumped_json

    def check_cache(self):
        body = self.get_body_hash()
        bool_status = check_if_in_cache(body)

        return bool_status

    def get_body_hash(self):
        dumped_json = self.dump_json()
        
        hash_json = hashlib.sha1(dumped_json).hexdigest()

        return hash_json