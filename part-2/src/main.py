from jsonstream import loads 
import sys
import requests
from product import Product
import time

_productId = 'productId'  #json tag for product id
_images = 'image' #json tag for image
_maxImages = 3 #Number of maximum images for which product

def start():
    with open(sys.argv[1]) as json_dump:
        final = loads(json_dump.read())

        lista_final = list(final)

        for product_json in lista_final:
            if not Product.check_if_id_in_cache(product_json[_productId]):
                product_id_not_cached(product_json[_productId], product_json[_images])   

            elif len(Product.get_all_images_from_id(product_json[_productId])) < _maxImages:
                product_id_cached(product_json[_productId], product_json[_images])                    

        write_output_json()
        return

def product_id_cached(id, image):
    image_list = Product.get_all_images_from_id(id)
    product = Product(id, image_list)

    if product.check_if_image_in_list(image):
        return
    elif product.image_status(image):
         product.append_to_image_list(image)
         product.update_object_in_cache()
    return

def product_id_not_cached(id, image):
    product = Product(id, image)

    if product.image_status(image):
        product.inset_object_in_cache()

    return

def write_output_json():
    with open('src/dump/output.json', 'w') as output_file:
        for key in Product.get_all_keys_from_cache():
            product = Product(key.decode('utf-8'), Product.get_all_images_from_id(key))
            output_file.write(product.jsonfy())
            output_file.write('\n')

    return

def check_args_passes():
    try:
        sys.argv[1]
        return True
    except:
        print("Please, pass a json file as argument, example: python main.py input.json")


if __name__ == "__main__":
     if check_args_passes():
        start_time = time.time()
        start()
        print("--- %s seconds ---" % (time.time() - start_time))