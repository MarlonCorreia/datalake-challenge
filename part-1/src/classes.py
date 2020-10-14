from pydantic import BaseModel
import json
import hashlib

class Object_json(BaseModel):
    id: int
    name: str

    def check_cache(self):
        if self.id == 4:
            return True
        else:
            return False

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