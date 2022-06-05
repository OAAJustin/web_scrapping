## Import Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = requests.get("https://www.accuweather.com/")
print(url)
doc = BeautifulSoup(url.text, 'html.parser')
print(doc)