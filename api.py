import os
import requests
import ssl
import sys
import time

from collections import defaultdict

import matplotlib.pyplot as plt

from PIL import Image
from io import BytesIO

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

class Storage:

    def __init__(self):
        pass

    def query(self, name):
        return 24 * 60 * 7
storage = Storage()


def image(data):
    region = "southeastasia"
    subscription_key = "189b640227c94a6f87975cc09e2f3f12"
    endpoint = "https://hackahon.cognitiveservices.azure.com/"
    analyze_url = endpoint + "vision/v3.0/analyze"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Objects'}

    response = requests.post(analyze_url, headers=headers, params=params, data=data)
    response.raise_for_status()

    m = {}
    for obj in response.json()['objects']:
        print(obj)
        if 'parent' in obj and obj['parent']['object'] in set(['Fruit', 'Vegetable']):
            name = obj['object']
            item = m.setdefault(obj['object'], {
                'name': name,
                'count': 0,
                'expireTime': storage.query(name),
            })
            item['count'] += 1

    return list(m.values())


def barcode(code):
    url = 'http://jisutxmcx.market.alicloudapi.com/barcode2/query?barcode={}'.format(code)
    print(url)

    headers = {
        'Authorization': 'APPCODE a5059cdecc4a45b79fbdcce0f86e2a12',
        'Content-Type': 'application/json; charset=UTF-8',
    }
    r = requests.request('GET', url, headers=headers)
    r.raise_for_status()
    item = r.json()['result']
    name = item['name']

    return {
        'name': name,
        'count': 1,
        'expireTime': storage.query(name),
    }


if __name__ == '__main__':
    barcode("06917878036526")