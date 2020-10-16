from fastapi import FastAPI, status, HTTPException, Request, Body
from typing import List, Dict, Any
from classes import Object_json

app = FastAPI()


#@app.post("/post/")
#async def create_item(object: List[Object_json]):
#    main_object = object[0]
#    return_status = main_object.check_cache()
#
#    if return_status is True:
#        raise HTTPException(status_code=403, detail="Same body request")

#    return main_object

@app.post("/post/")
async def create_item(request = Body(...)):
    object_json = Object_json(request)

    if object_json.check_cache():
        raise HTTPException(status_code=403, detail="Same body request")

    return request