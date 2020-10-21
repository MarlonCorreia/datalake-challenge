import redis

r = redis.Redis() #redis running locally, you can specify service HOST, PORT by adding it inside the brackets, example (host={ip}, port={port})

def insert_cache(id, images):
    r.set(id, images)

def update_in_cache(id, images):
    r.set(id, images)

def get_all_keys():
    return r.scan_iter()

