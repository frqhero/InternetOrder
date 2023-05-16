import json
import unittest

from environs import Env
import requests


class TestInternetOrder(unittest.TestCase):

    def setUp(self):
        env = Env()
        env.read_env()
        self.api_username = env('API_USERNAME')
        self.api_password = env('API_PASSWORD')
        self.url = env('API_URL')
        with open('internet_order.json', 'r') as file:
            self.payload = json.load(file)

    def test_bank_card(self):
        self.payload.pop('bank_card')
        response = requests.post(
            self.url,
            json=self.payload,
            auth=(self.api_username, self.api_password)
        )
        self.assertEqual(
            response.status_code,
            500,
            'Status code should be 500 as required field is omitted'
        )
        self.assertIn(
            'Отсутствует обязательное поле bank_card',
            response.text,
        )
        self.payload['bank_card'] = 1
        response = requests.post(
            self.url,
            json=self.payload,
            auth=(self.api_username, self.api_password)
        )
        self.assertEqual(
            response.status_code,
            500,
            'Status code should be 500 as bank_card type should be boolean'
        )
        self.assertIn(
            'Тип значения ключа bank_card не булево',
            response.text,
        )

    def test_customer_name(self):
        self.payload.pop('customer_name')
        response = requests.post(
            self.url,
            json=self.payload,
            auth=(self.api_username, self.api_password)
        )
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'Отсутствует обязательное поле customer_name',
            response.text,
        )
        self.payload['customer_name'] = 1
        response = requests.post(
            self.url,
            json=self.payload,
            auth=(self.api_username, self.api_password)
        )
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'Тип значения ключа customer_name не строка',
            response.text,
        )
        self.payload['customer_name'] = ''
        response = requests.post(
            self.url,
            json=self.payload,
            auth=(self.api_username, self.api_password)
        )
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'Имя клиента не должно быть пустым',
            response.text,
        )


if __name__ == '__main__':
    unittest.main()
