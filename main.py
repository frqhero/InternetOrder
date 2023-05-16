from environs import Env
import json
import requests


def get_payload_from_txt():
    with open('internet_order.json', 'r') as file:
        obj = json.load(file)
    return obj


def make_internet_order_request(username, password):
    url = 'http://82.202.230.202:2028/utd_sandbox4/hs/v2/internet_order'
    payload = get_payload_from_txt()
    response = requests.post(url, json=payload, auth=(username, password))
    1


def main():
    env = Env()
    env.read_env()
    api_username = env('API_USERNAME')
    api_password = env('API_PASSWORD')
    make_internet_order_request(
        api_username,
        api_password
    )

if __name__ == '__main__':
    main()
