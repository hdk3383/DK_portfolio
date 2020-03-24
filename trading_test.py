# https://finnhub.io/

import requests
import datetime, time
import csv, itertools
import pandas as pd
import sys
import json

from class_Unixtime import unixtime
     
input_value = 'AAPL'
# URL
Url = 'https://finnhub.io/api/v1'

# Candle : https://finnhub.io/docs/api#stock-candles 
_resoultion = '&resolution=D' # Day 기준
_from = '&from=' + unixtime.get180beforeUnixtime()
_to = '&to=' + unixtime.getTodayUnixtime()
Candle = '/stock/candle?symbol=' + input_value + _resoultion + _from + _to

indicators = '/scan/technical-indicator?symbol=AAPL&resolution=D'

# API_toekn
API_key = 'bp8akf7rh5r8okvp0vk0'
API_token = '&token=' + API_key

full_url = Url + Candle + API_token
indicators_url = Url + indicators + API_token

request = requests.get(full_url)
request = request.json()

request2 = requests.get(indicators_url)
request2 = request2.json()

df = pd.DataFrame.from_dict(request)
df2 = pd.DataFrame.from_dict(request2)

print(df2)

    