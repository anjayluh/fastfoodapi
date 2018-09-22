from .api import *
import unittest
from flask import Flask, request
import requests
import json


class TestOrdersUsingRequests(unittest.TestCase):
    def test_abort_if_order_doesnt_exist(self):
        response = requests.get('http://localhost:5000/v1/orders/order10')
        self.assertEqual(response.status_code, 404)
    def test_get_order_id(self):
        response = requests.get('http://localhost:5000/v1/orders/order1')
        self.assertEqual(response.status_code, 200)
        print(response.status_code)
    #test get all orders
    def test_get_orders(self):
        response = requests.get('http://localhost:5000/v1/orders')
        self.assertEqual(response.status_code, 200)
        print(response.status_code)

    #test post id
    def test_put_order(self):
        order = {'order9':{'my_order': "Large size pizza"}}
        response = requests.put('http://127.0.0.1:5000/v1/orders/<order>')
        self.assertEqual(response.status_code, 201)
        print(response.status_code)

    #test post order
    def test_post_order(self):
        orders = {'order3':{'my_order': "Noodles"}}
        response = requests.post('http://127.0.0.1:5000/v1/orders')
        self.assertEqual(response.status_code, 201)
        print(response.status_code)
    
    #test delete
    def test_delete_order(self):
        response = requests.delete('http://127.0.0.1:5000/v1/orders/order0')
        print(response)
        self.assertEqual(response.status_code, 204)
        print(response.status_code)

    #test delete
    '''def test_delete(self):'''
if __name__ == "__main__":
    unittest.main()
    #Order = Order()