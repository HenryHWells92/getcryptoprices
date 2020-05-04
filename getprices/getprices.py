# taking agalea91's ipython notebook from github and reformatting functions as a python package
# repo link: https://github.com/agalea91/cryptocompare-api.git
# original blog post: https://medium.com/@galea/cryptocompare-api-quick-start-guide-ca4430a484d4
# this package adapted by Henry Wells; last updated 1/18/2018

# importing modules and functions:

import requests
import datetime
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('fivethirtyeight')

import uuid
from IPython.display import display_javascript, display_html, display
import json

# settings for rendering of JSON-formatted data from the cryptocompare api: 

class RenderJSON(object):
    def __init__(self, json_data):
        if isinstance(json_data, dict):
            self.json_str = json.dumps(json_data)
        else:
            self.json_str = json_data
        self.uuid = str(uuid.uuid4())

    def _ipython_display_(self):
        display_html('<div id="{}" style="height: 600px; width:100%;"></div>'.format(self.uuid), raw=True)
        display_javascript("""
        require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function() {
        document.getElementById('%s').appendChild(renderjson(%s))
        });
        """ % (self.uuid, self.json_str), raw=True)



# functions for calling cryptocurrency price data:


"""Takes the symbol for a cryptocurrency (ex 'BTC', 'ETH', 'LTC') and the name of an exchange
(ex 'Gemini') and assumes 'USD' as the comparison currency. Returns the price of the crypto in USD.
Can also take a list of comparison symbols (ex if calling the price of 'BTC', compare with
['ETH', 'LTC', 'USD']"""

def price(symbol, comparison_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data


"""Returns the EOD price of the currency specified with 'symbol', measured in the currency 
specified by 'comparison_symbol'. 'limit' and 'aggregate' args used to limit the size of the dataset
and aggregate the data, respectively. Can be called with a specific exchange set as a string in the 
'exchange' arg.

Example call:
"""
def daily_price_historical(symbol, comparison_symbol, limit, aggregate, exchange='', allData='true'):
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}&allData={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate, allData)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df


"""Analagous to daily_price_historical, but for hourly prices"""
def hourly_price_historical(symbol, comparison_symbol, limit, aggregate, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df


"""Analagous to daily_price_historical, but for minute-by-minute prices"""
def minute_price_historical(symbol, comparison_symbol, limit, aggregate, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df


""" returns a list of all cryptocurrencies in the cryptocompare api, by their symbols"""
def coin_list():
    url = 'https://www.cryptocompare.com/api/data/coinlist/'
    page = requests.get(url)
    data = page.json()['Data']
    return data


"""Returns data showing a summary of recent changes in value  of the currency specified. 
'symbol_id_dict' left blank as default. Example call:

data = coin_snapshot_full_by_id('BTC', symbol_id_dict)
RenderJSON(data)
"""
def coin_snapshot_full_by_id(symbol, symbol_id_dict={}):
    if not symbol_id_dict:
        symbol_id_dict = {
            'BTC': 1182,
            'ETH': 7605,
            'LTC': 3808
        }
    symbol_id = symbol_id_dict[symbol.upper()]
    url = 'https://www.cryptocompare.com/api/data/coinsnapshotfullbyid/?id={}'\
            .format(symbol_id)
    page = requests.get(url)
    data = page.json()['Data']
    return data


"""Returns data on social media mentions of the currency specified. 'symbol_id_dict' left blank
as default. Example call:

data = live_social_status('BTC', symbol_id_dict)
RenderJSON(data)
"""
def live_social_status(symbol, symbol_id_dict={}):
    if not symbol_id_dict:
        symbol_id_dict = {
            'BTC': 1182,
            'ETH': 7605,
            'LTC': 3808
        }
    symbol_id = symbol_id_dict[symbol.upper()]
    url = 'https://www.cryptocompare.com/api/data/socialstats/?id={}'\
            .format(symbol_id)
    page = requests.get(url)
    data = page.json()['Data']
    return data
