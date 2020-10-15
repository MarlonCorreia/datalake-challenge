from pydantic import BaseModel
from typing import List
import json
import hashlib
from cache import check_if_in_cache

class Object_json(BaseModel):
    id: int
    name: str

    def check_cache(self):
        body = self.get_body_hash()
        bool_status = check_if_in_cache(body)

        return bool_status

    def jsonfy(self):
        json_format = {
            "id": self.id,
            "name": self.name
        }

        dumped_json = json.dumps(json_format, sort_keys = True).encode("utf-8")
        
        return dumped_json

    def get_body_hash(self):
        dumped_json = self.jsonfy()
        
        hash_json = hashlib.sha1(dumped_json).hexdigest()

        return hash_json