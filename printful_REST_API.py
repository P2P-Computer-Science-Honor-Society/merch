import requests
import datetime as dt
import pytz
import json
import pandas as pd
from requests.api import head

class Printful_Account():
    def __init__(self, keys_file_name):
        with open(keys_file_name, "r") as keys_file:
            keys = json.load(keys_file)
            self.printful_api_key = keys["PRINTFUL_API_KEY"]
            self.headers = {
                "Authorization": "Basic " + self.printful_api_key,
            }
        self.base_url = "https://api.printful.com"

    def do_get(self, url):
        return requests.get(url, headers=self.headers)


    def get_products(self):
        url = self.base_url + "/store/products"
        response = self.do_get(url)
        return response

    def get_file(self, id):
        url = self.base_url + "/files/%s" % id
        response = self.do_get(url)
        return response

    def get_printful_products(self):
        url = self.base_url + "/products"
        return self.do_get(url)
    
    def get_printful_product(self, id):
        url = self.base_url + "/products/%s" % id
        return self.do_get(url)

    def create_sync_product(self, payload):
        url = self.base_url + "/store/products"
        response = requests.post(url, json=payload, headers=self.headers)
        return response

    def create_product_mockup(self, id, payload):
        url = self.base_url + "/mockup-generator/create-task/%s" % id
        response = requests.post(url, json=payload, headers=self.headers)
        return response


printful = Printful_Account("printful_config.json")

# print(printful.get_products().json())

# print(printful.get_file(368212732).json())

# printful_products = printful.get_printful_products().json()['result']

# df = pd.DataFrame(printful_products)
# df.to_csv("prtinfulprods.csv")
# df = pd.read_csv("prtinfulprods.csv")
# df = df[df['type'] == "T-SHIRT"]
# print(df.columns)
# df = df[["id", "type", "image", "variant_count"]]
# for row in df.iterrows():
#     print(row[1].id, row[1].image, row[1].variant_count)

# product = pd.DataFrame(printful.get_printful_product(5).json()['result']['variants'])
# print(product)
# print(product.columns)

payload = {
  "sync_product": {
    "external_id": "4235234213",
    "name": "T-shirt",
    "thumbnail": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.guim.co.uk%2Fimg%2Fmedia%2F26392d05302e02f7bf4eb143bb84c8097d09144b%2F446_167_3683_2210%2Fmaster%2F3683.jpg%3Fwidth%3D1200%26height%3D1200%26quality%3D85%26auto%3Dformat%26fit%3Dcrop%26s%3D49ed3252c0b2ffb49cf8b508892e452d&imgrefurl=https%3A%2F%2Fwww.theguardian.com%2Flifeandstyle%2F2020%2Fsep%2F05%2Fwhat-cats-mean-by-miaow-japans-pet-guru-knows-just-what-your-feline-friend-wants&tbnid=BBEQz5BdOWu86M&vet=12ahUKEwj98Yv229D0AhUYAJ0JHbcWA_wQMygBegUIARCHAg..i&docid=V4qL_jTRbB2FuM&w=1200&h=1200&itg=1&q=cat&ved=2ahUKEwj98Yv229D0AhUYAJ0JHbcWA_wQMygBegUIARCHAg",
    "is_ignored": False
  },
  "sync_variants": [
    {
      "external_id": "12312414",
      "variant_id": 130,
      "retail_price": 29.99,
      "is_ignored": False,
      "sku": "SKU1234",
      "files": [
        {
            "id": 368212732
        }
      ],
      "options": [
        {
          "id": "embroidery_type",
          "value": "flat"
        }
      ]
    }
  ]
}

response = printful.create_sync_product(payload)
print(response)
print(response.json())

# payload = {
#   "variant_ids": [
#     4012,
#     4013,
#     4014,
#     4017,
#     4018,
#     4019
#   ],
#   "format": "jpg",
#   "width": 1000,
#   "product_options": {},
#   "option_groups": {},
#   "options": [
#     "string"
#   ],
#   "files": [
#     {
#       "placament": "front",
#       "image_url": "https://www.pixsy.com/wp-content/uploads/2021/04/ben-sweet-2LowviVHZ-E-unsplash-1.jpeg",
#       "position": {
#         "area_width": 1800,
#         "area_height": 2400,
#         "width": 1800,
#         "height": 1800,
#         "top": 300,
#         "left": 0
#       }
#     }
#   ]
# }

# response = printful.create_product_mockup(71    , payload)
# print(response)
# print(response.json())