from bs4 import BeautifulSoup
import requests
import pandas as pd
from prettyprinter import pprint

url = 'https://coinmarketcap.com/'
r = requests.get(url)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
tbody = soup.tbody
trs = tbody.contents

prices = {}
for tr in trs[:10]:
    name,price,percent = tr.contents[2:5]
    fixed_name = name.p.string
    fixed_price = price.a.string
    dynamic_percent = percent.span.text

    prices[fixed_name] = fixed_price, dynamic_percent

    print(prices)

prices.get("Bitcoin")

