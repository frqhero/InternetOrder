from uuid import uuid4
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

    def get_response(self):
        return requests.post(
            self.url,
            json=self.payload,
            auth=(self.api_username, self.api_password)
        )

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
            'customer_name не должно быть пустым',
            response.text,
        )

    def test_delivery_address(self):
        self.payload.pop('delivery_address')
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
            'Отсутствует обязательное поле delivery_address',
            response.text,
        )
        self.payload['delivery_address'] = 1
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
            'Тип значения ключа delivery_address не строка',
            response.text,
        )
        self.payload['delivery_address'] = ''
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
            'delivery_address не должно быть пустым',
            response.text,
        )

    def test_order_date(self):
        self.payload.pop('order_date')
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
            'Отсутствует обязательное поле order_date',
            response.text,
        )
        self.payload['order_date'] = 1
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
            'Тип значения ключа order_date не строка',
            response.text,
        )
        self.payload['order_date'] = ''
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
            'order_date не должно быть пустым',
            response.text,
        )
        self.payload['order_date'] = '2023-04-17T21:45:3'
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
            'Не удалось order_date преобразовать в дату',
            response.text,
        )

    def test_order_number(self):
        self.payload.pop('order_number')
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
            'Отсутствует обязательное поле order_number',
            response.text,
        )
        self.payload['order_number'] = '6'
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
            'Тип значения ключа order_number не число',
            response.text,
        )

    def test_data(self):
        self.payload.pop('data')
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
            'Отсутствует обязательное поле data',
            response.text,
        )
        self.payload['data'] = '6'
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
            'Тип значения ключа data не массив',
            response.text,
        )
        self.payload['data'] = []
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
            'Массив data пустой',
            response.text,
        )

    def test_series_objects(self):
        series_object = self.payload['data'][0]
        series_object_copy = series_object.copy()
        series_object.pop('series')
        response = self.get_response()
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'Отсутствует обязательное поле series',
            response.text,
        )
        series_object['series'] = series_object_copy['series']
        series_object.pop('price')
        response = self.get_response()
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'Отсутствует обязательное поле price',
            response.text,
        )
        series_object['price'] = series_object_copy['price']
        series_object['series'] = 1
        response = self.get_response()
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'Тип значения ключа series не строка',
            response.text,
        )
        series_object['series'] = series_object_copy['series']
        series_object['price'] = '1'
        response = self.get_response()
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'Тип значения ключа price не число',
            response.text,
        )
        series_object['price'] = series_object_copy['price']
        series_object['series'] = ''
        response = self.get_response()
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'series не должно быть пустым',
            response.text,
        )
        series_object['series'] = str(uuid4())
        response = self.get_response()
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'Не найдена серия по гуиду',
            response.text,
        )

    def test_delivery_price(self):
        self.payload['delivery_price'] = ''
        response = self.get_response()
        self.assertEqual(
            response.status_code,
            500,
        )
        self.assertIn(
            'Тип значения ключа delivery_price не число',
            response.text,
        )


if __name__ == '__main__':
    unittest.main()
