from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

url = 'https://race.spartan.com'
request = requests.get(url)
print(request.text)
web_page = BeautifulSoup(url.text, 'html.parser')