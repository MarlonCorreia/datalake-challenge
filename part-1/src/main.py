from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

class Object_json(BaseModel):
    id: int
    name: str

    def check_cache(self):
        if self.id is 4:
            return True
        else:
            return False

app = FastAPI()


@app.post("/post/")
async def create_item(object: Object_json):
    return_status = object.check_cache()

    if return_status is True:
        raise HTTPException(status_code=403, detail="Same body request")

    return object