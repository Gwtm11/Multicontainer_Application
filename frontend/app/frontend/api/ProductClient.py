import requests
import os
import json

class ProductClient:

    @staticmethod
    def get_product(slug):
        response = requests.request(method="GET", url='http://'+os.getenv('PRODUCT_SERVICE')+'/api/product/' + slug)
        product = response.json()
        return product

    @staticmethod
    def get_products():
        url = 'http://'+os.getenv('PRODUCT_SERVICE')+'/api/products'
        print(url,'*********************************')
        r = requests.get(url)
        products = r.json()
        return products
