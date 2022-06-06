## Import Dependencies
from re import X
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from datetime import datetime

## Generate url object
url = 'https://race.spartan.com/en/race/profile/515428'
## Call the webpage using Requests
request = requests.get(url)
## Parse the webpage with Soup
soup = BeautifulSoup(request.text, 'html.parser')

## Access the <tbody> class of the tree
tbody = soup.tbody
## Access the contents of the body and assign to object
trs = tbody.contents

## Empty Dictionary for the Events
events = {}

## Loop each Table Data(td) and extract information
for td in trs:
    ## Try and Except for nonetype objects (No information)
    try:
        info = td.find_all('td')
        event = str(info[0].text).replace("\n","").strip().split('  ')[-1]
        date = str(info[0].text).replace("\n","").strip().split('  ')[0]
        time = str(info[5].text).replace("\n","").strip()
        ## Empty variable to allow for no garbage collection
        info = ''
        ## Append the event to the dictionary
        events[event] = date , time
    except:
        pass


## Generate an array
## list(events.items())[0][1][1] - TIME
## list(events.items())[0][1] - BOTH VALUES
## list(events.items())[0][1][0] - DATE
## list(events.items())[0][0] - EVENT

