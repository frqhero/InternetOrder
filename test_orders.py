import json
import unittest

from environs import Env
import requests


class TestInternetOrderValidation(unittest.TestCase):
    def setUp(self):
        env = Env()
        env.read_env()
        self.api_username = env('API_USERNAME')
        self.api_password = env('API_PASSWORD')
        self.url = env('API_URL')

    def get_response(self):
        return requests.post(
            self.url,
            json=self.payload,
            auth=(self.api_username, self.api_password)
        )

    def test_cash(self):
        with open('order_templates/cash.json', 'r') as file:
            self.payload = json.load(file)
        response = self.get_response()
        1

    def test_card(self):
        with open('order_templates/card.json', 'r') as file:
            self.payload = json.load(file)
        response = self.get_response()
        1

    def test_discount_card(self):
        with open('order_templates/discount_card.json', 'r') as file:
            self.payload = json.load(file)
        response = self.get_response()
        1

if __name__ == '__main__':
    unittest.main()
