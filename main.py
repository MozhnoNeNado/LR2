import requests
import time
import json

def Site():
    return requests.get("https://blockchain.info/ru/ticker").text

a = input("Введите валюту: ")

while True:
    d = json.loads(Site())
    d2 = d[a]
    print(d2['buy'])
    time.sleep(5)





