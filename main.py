from flask import Flask

from routes.add_route import Add
from routes.decrease_route import Decrease
from routes.division_route import Division
from routes.main_route import MainRoute
from routes.product_route import Product


app = Flask(__name__)

routes = [
    MainRoute(),
    Add(),
    Division(),
    Product(),
    Decrease()
]

for route in routes:
    app.add_url_rule(route.get_route(), view_func=route.as_view(route.get_route()))

app.run()