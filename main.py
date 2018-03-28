from flask import Flask

from classes.add import AddOperate
from classes.decrease import DecreaseOperate
from classes.division import DivisionOperate
from classes.product import ProductOperate

# sum = AddOperate(3,5)
# dif = DecreaseOperate(7,5)
# prod = ProductOperate(3,5)
# div = DivisionOperate(5,7)
#
# print(sum.add())
# print(dif.decrease())
# print(prod.product())
# print(div.division())
from routes.add_route import Add
from routes.main_route import MainRoute

app = Flask(__name__)

routes = [
    MainRoute(),
    Add()
]

for route in routes:
    app.add_url_rule(route.get_route(), view_func=route.as_view(route.get_route()))

app.run()