
class Product():

    def __init__(self,id, images):
        self.id = id
        self.images = images

    def get_list_size(self):
        return len(self.images)

    def check_if_image_in_list(self, new_image):
        if new_image in self.images
            return True
        return False

    