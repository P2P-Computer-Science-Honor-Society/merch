import requests
import datetime as dt
import pytz
import json
import pandas as pd

class Printful_Account():
    def __init__(self, keys_file_name):
        with open(keys_file_name, "r") as keys_file:
            keys = json.load(keys_file)
            self.printful_api_key = keys["PRINTFUL_API_KEY"]
            self.headers = {
                "Authorization": "Basic " + self.printful_api_key,
            }
        self.base_url = "https://api.printful.com"

    def get_products(self):
        url = self.base_url + "/store/products"
        response = requests.get(url, headers=self.headers)
        return response

printful = Printful_Account("printful_config.json")

print(printful.get_products().json())