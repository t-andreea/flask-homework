from flask import request
from classes.add import AddOperate
from routes.main_route import MainRoute



class Add(MainRoute):

    def __init__(self):
        pass

    def _generate_response(self, input_data):
        super()._generate_response(input_data=input_data)

    def post(self):
        a = request.form['nr1']
        b = request.form['nr2']
        a = int(a)
        b = int(b)
        s = AddOperate(a, b)
        input_data = s.add()
        return input_data

    def get_route(self):
        return '/add'