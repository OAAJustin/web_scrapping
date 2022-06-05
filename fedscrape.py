from bs4 import BeautifulSoup
import requests

url = 'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'
request = requests.get(url)
print(request.text)