import json
from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})


@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computer_orders():
    match request.method:
        case 'GET':
            return jsonify(retrieve_orders()), 200
        case 'POST':
            return jsonify(create_order(request.json)), 201
    return Exception('Unsupported HTTP request type.')

if __name__ == '__main__':
    app.run()
