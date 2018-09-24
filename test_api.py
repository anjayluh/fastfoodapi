from api import *
import unittest
from flask import Flask, request
import requests
import json

class TestOrdersUsingRequests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_abort_if_order_doesnt_exist(self):
        response = self.client.get('/v1/orders/order10')
        self.assertEqual(response.status_code, 404)
    def test_get_order_id(self):
        response = self.client.get('/v1/orders/order1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('order1', orders)
        print(response.status_code)
    #test get all orders
    def test_get_orders(self):
        response = self.client.get('/v1/orders')
        self.assertEqual(response.status_code, 200)
        print(response.status_code)

    #test post id
    def test_put_order(self):
        order = {'order3':{'my_order': "Large size pizza"}}
        response = self.client.put('/v1/orders/<order>')
        self.assertEqual(response.status_code, 201)
        self.assertIn('order3', orders)
        print(response.status_code)

    #test post order
    def test_post_order(self):
        orders = {'order3':{'my_order': "Noodles"}}
        response = self.client.post('http://127.0.0.1:5000/v1/orders')
        self.assertEqual(response.status_code, 201)
        self.assertIn('order3', orders)
        print(response.status_code)
    
    #test delete
    def test_delete_order(self):
        response = self.client.delete('http://127.0.0.1:5000/v1/orders/order0')
        print(response)
        self.assertEqual(response.status_code, 204)
        print(response.status_code)
        

if __name__ == "__main__":
    unittest.main()
    #Order = Order()
