from flask import Response, json
from flask.views import MethodView


class MainRoute(MethodView):

    def __init__(self):
        pass

    @classmethod
    def _generate_response(cls, input_data=None):
        if input_data is None:
            resp = dict(status=1, content='Method Not Implemented!')
        else:
            resp = dict(status=0, content=input_data)
        return Response(json.dumps(resp))

    def get(self):
        return 'Yeah, it is working'

    def post(self):
        return 'Hello from POST method'

    def get_route(self):
        return '/'