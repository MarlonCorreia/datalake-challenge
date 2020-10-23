import redis

r = redis.Redis() #redis running locally, you can specify service HOST, PORT by adding it inside the brackets, example (host={ip}, port={port})


def insert_cache(id, images):
    r.lpush(id, *images)

def update_in_cache(id, images):
    r.delete(id)
    r.lpush(id, *images)

def get_images_from_id(id):
    utf_list = []
    for image in r.lrange(id, 0, -1):
        utf_list.append(image.decode('utf-8'))
    return utf_list

def check_if_exists(id):
    return r.exists(id)

def get_all_keys():
    return r.scan_iter()


