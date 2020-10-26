from cache import insert_cache, update_in_cache, check_if_exists, get_images_from_id, get_all_keys
import json
import requests

class Product():

    def __init__(self,id, images):
        self.id = id
        if type(images) != list:
            lista = []
            lista.append(images)
            self.images = lista
        else:
            self.images = images
    
    def append_to_image_list(self, new_image):
        self.images.append(new_image)

    def check_if_image_in_list(self, new_image):
        if new_image in self.images:
            return True
        return False

    def inset_object_in_cache(self):
        insert_cache(self.id, self.images)

    def update_object_in_cache(self):
        update_in_cache(self.id, self.images)

    def jsonfy(self):
        json_format = {}
        json_format["productId"] = self.id
        json_format["images"] = self.images

        return json.dumps(json_format)

    def image_status(self, new_image):
        r = requests.get(new_image)
    
        if r.status_code == 200:
            return True
        return False

    @staticmethod
    def check_if_id_in_cache(id):
        return check_if_exists(id)
    
    @staticmethod
    def get_all_images_from_id(id):
        return get_images_from_id(id)

    @staticmethod
    def get_all_keys_from_cache():
        return get_all_keys()

