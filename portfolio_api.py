
# https://finnhub.io/

import requests
import datetime, time
import csv, itertools
import pandas as pd

from class_Unixtime import unixtime

stock_data = input("* 포트폴리오 회사 입력 ex)AAPL,PG,XOM : ").split(',')

df_list = []

def getdatetime(input_value, df_list):
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
    df_list.append(df['t'].values.tolist())
        
def getstockdata(input_value, df_list):
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
    df_list.append(df['c'].values.tolist())
    #df_list.insert(0, df['c'].values.tolist() )
    
getdatetime(stock_data[0], df_list)
for input_value in stock_data:
    getstockdata(input_value, df_list)

w = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(w, delimiter=',', quotechar='|')
wr.writerow(['date', stock_data])
wr.writerows(list(itertools.zip_longest(*df_list, fillvalue='')))
    
w.close()

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

# Read in price data
df_total = pd.read_csv("output.csv", parse_dates=True, index_col="date")
print(df_total)

# Calculate expected returns and sample covariance
mu = expected_returns.mean_historical_return(df_total)
S = risk_models.sample_cov(df_total)

# Optimise for maximal Sharpe ratio
ef = EfficientFrontier(mu, S)
raw_weights = ef.max_sharpe()
cleaned_weights = ef.clean_weights()
ef.save_weights_to_file("output_weights.csv")  # saves to file
print(cleaned_weights)
ef.portfolio_performance(verbose = True)