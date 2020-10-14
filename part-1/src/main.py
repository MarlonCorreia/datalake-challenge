from fastapi import FastAPI, status, HTTPException
from classes import Object_json

app = FastAPI()


@app.post("/post/")
async def create_item(object: Object_json):
    return_status = object.check_cache()

    if return_status is True:
        raise HTTPException(status_code=403, detail="Same body request")

    return object