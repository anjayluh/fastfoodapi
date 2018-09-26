from flask import Flask, request
import requests
from app.api import *
import unittest



class TestOrdersUsingRequests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    '''Test if order doesn't works'''
    def test_abort_if_order_doesnt_exist(self):
        response = self.client.get('/v1/orders/order10')
        self.assertEqual(response.status_code, 404)

    #Test if input order is empty
    def test_post_empty_order(self):
        response = self.client.post('/v1/orders', data={'order': " "})
        self.assertEqual(response.status_code, 400)
        print(response.status_code)

    def test_get_order_id(self):
        my_orders = "Noodles"
        its_price= 3000
        response = self.client.post('/v1/orders', data={'order': my_orders, 'price': its_price})
        response = self.client.get('/v1/orders/order1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('order1', orders)
        print(response.status_code)
        # print(orders)

    #test get all orders
    def test_get_orders(self):
        response = self.client.post('/v1/orders', data={'order': "Fried fish", 'price': "20000"})
        response = self.client.post('/v1/orders', data={'order': "Chicken Briyani", 'price': "10000"})
        response = self.client.get('/v1/orders')
        self.assertEqual(response.status_code, 200)
        print(response.status_code)

    #test put order
    def test_put_order(self):
        response = self.client.post('/v1/orders', data={'order': "Home baked chicken samosas", 'price': "5000"})
        self.assertEqual(response.status_code, 201)
        self.assertIn('order3', orders)
        print(response.status_code)

    #test post order
    def test_post_order(self):
        response = self.client.post('/v1/orders', data={'order': "French toast", 'price': "5000"})
        self.assertEqual(response.status_code, 201)
        self.assertIn('order1', orders)
        print(response.status_code)

    
    #test delete
    def test_delete_order(self):
        response = self.client.post('/v1/orders', data={'order': "French toast", 'price': "5000"})
        response = self.client.delete('/v1/orders/order1')
        print(response.__dict__)
        self.assertEqual(response.status_code, 204)
        print(response.status_code)
        

if __name__ == "__main__":
    unittest.main()
    #Order = Order()
