from fastapi import FastAPI, status, HTTPException
from typing import List
from classes import Object_json

app = FastAPI()


@app.post("/post/")
async def create_item(object: List[Object_json]):
    main_object = object[0]
    return_status = main_object.check_cache()

    if return_status is True:
        raise HTTPException(status_code=403, detail="Same body request")

    return main_object