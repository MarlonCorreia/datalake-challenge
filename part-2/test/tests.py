import sys
sys.path.insert(0, '../src')

import unittest
import json
from product import Product

class Test_product_class(unittest.TestCase):

    def setUp(self):
        self.id = 1
        self.images = ['http://localhost:4567/images/67410.png', 'http://localhost:4567/images/60249.png']
        self.product = Product(self.id, self.images)
        self.image_in_list = 'http://localhost:4567/images/60249.png'
        self.image_not_in_list = 'http://localhost:4567/images/58449.png'

    def test_image_in_list(self):
        in_list = self.product.check_if_image_in_list(self.image_in_list)
        not_in_list = self.product.check_if_image_in_list(self.image_not_in_list) 

        self.assertEqual(in_list, True)
        self.assertEqual(not_in_list, False)

    def test_jsonfy(self):
        json_expected = {}
        json_expected['productId'] = self.id
        json_expected['images'] = self.images
        dumped_json = json.dumps(json_expected)

        self.assertEqual(self.product.jsonfy(), dumped_json)

    def test_append(self):
        expected = ['http://localhost:4567/images/67410.png', 'http://localhost:4567/images/60249.png','http://localhost:4567/images/28170.png']
        self.product.append_to_image_list(expected[2])
        self.assertEqual(self.product.images, expected)


if __name__ == '__main__':
    unittest.main() 
