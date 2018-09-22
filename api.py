from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

orders = {
    'order0': {'milk': 'Here is your french toast'},
    'order1': {'french toast': 'Here is your french toast'},
    'order2': {'fries': 'A pack of fries'},
    'order3': {'new order': 'Your new order will come here!'},
}

def abort_if_order_doesnt_exist(order_id):
    if order_id not in orders:
        abort(404, message="Order {} doesn't exist".format(order_id))

parser = reqparse.RequestParser()
parser.add_argument('order')


# Show all orders
class Orders(Resource):
    def get(self):
        return {'orders':orders}
    def post(self):
        args = parser.parse_args()
        order_id = int(max(orders.keys()).lstrip('order')) + 1
        order_id = 'order%i' % order_id
        orders[order_id] = {'my_order': args['order']}
        return orders, 201

# shows a single order and lets you delete an order
class Order(Resource):
    def get(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        return {order_id: orders[order_id]}
    def delete(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        del orders[order_id]

        return 'Order deleted', 204
    def put(self, order_id):
        args = parser.parse_args()
        order = {'my_order': args['order']}
        orders[order_id] = order
        return order, 201

api.add_resource(Orders,'/v1/orders')
api.add_resource(Order, '/v1/orders/<string:order_id>')
if __name__ == '__main__':
    app.run(debug=True)