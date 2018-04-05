from flask import request
from classes.product import ProductOperate
from routes.main_route import MainRoute



class Product(MainRoute):

    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)

    def post(self):
        a = int(request.form['nr1'])
        b = int(request.form['nr2'])
        p = ProductOperate(a, b)
        return self._generate_response(p.product())

    def get_route(self):
        return '/product'