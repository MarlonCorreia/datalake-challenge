from pydantic import BaseModel

class Object_json(BaseModel):
    id: int
    name: str

    def check_cache(self):
        if self.id is 4:
            return True
        else:
            return False