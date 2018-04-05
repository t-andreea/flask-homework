from flask import request
from classes.add import AddOperate
from routes.main_route import MainRoute



class Add(MainRoute):

    def __init__(self):
        super().__init__()

    def _generate_response(self, input_data=None):
        return super()._generate_response(input_data)

    def post(self):
        a = int(request.form['nr1'])
        b = int(request.form['nr2'])
        s = AddOperate(a, b)
        return self._generate_response(s.add())

    def get_route(self):
        return '/add'