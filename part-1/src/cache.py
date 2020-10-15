import redis

redis = redis.Redis('172.17.0.2')

def insert_cache(hash_json):
    value = redis.dbsize() 
    redis.set(hash_json, value + 1, ex=600)

def check_if_in_cache(hash_json):
    if redis.exists(hash_json):
        return True
    else:
        insert_cache(hash_json)
        return False

