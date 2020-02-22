
import requests
import datetime, time
import csv, itertools
import pandas as pd

from class_Unixtime import unixtime

input_value = 'PG'

df_list = []


# URL
Url = 'https://finnhub.io/api/v1/stock'

# Candle : https://finnhub.io/docs/api#stock-candles 
_resoultion = '&resolution=D' # Day 기준
_from = '&from=' + unixtime.get180beforeUnixtime()
_to = '&to=' + unixtime.getTodayUnixtime()
Candle = '/candle?symbol=' + input_value + _resoultion + _from + _to

# API_toekn
API_key = 'bp8akf7rh5r8okvp0vk0'
API_token = '&token=' + API_key

full_url = Url + Candle + API_token

request = requests.get(full_url)
request = request.json()

df = pd.DataFrame.from_dict(request)

df_new = df['t'].values.tolist()
df_list.append(df['t'].values.tolist())

datetime_new = []
for date in df_new:
    date = datetime.datetime.fromtimestamp(date)
    date = date.isoformat()
    datetime_new.append(date)

print(datetime_new)

