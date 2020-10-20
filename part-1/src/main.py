from fastapi import FastAPI, status, HTTPException, Request, Body, Header
from fastapi.testclient import TestClient
import uvicorn
from typing import List, Dict, Any, Optional
from cache import fake_redis_check_if_in_cache
from classes import Object_json
import time

app = FastAPI()

fake_token = "token_for_testing"

@app.post("/post/")
async def create_item(request = Body(...), x_token: Optional[str] = Header(None)):
    object_json = Object_json(request)

    if x_token == fake_token:
        hash_json = object_json.get_body_hash()
        if fake_redis_check_if_in_cache(hash_json):
            raise HTTPException(status_code=403, detail="Same body request")
        return request


    if object_json.check_cache():
        raise HTTPException(status_code=403, detail="Same body request")

    return request

if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')

"""Creating Test mockup for endpoints"""

client = TestClient(app)

def test_post(body_json):
    response = client.post(
        "/post/",
        headers={"X-Token": "token_for_testing"},
        json=body_json,
    )

    return response.status_code, response.json()
