import requests
from pprint import pprint
import finnhub
import finnhub.exceptions as esc
import json
import os

with open('static/symbols.json') as f:
    data = json.load(f)

api_key = os.environ.get('FINN_HUB_API_KEY')

# Setup client
finnhub_client = finnhub.Client(api_key=api_key)


def search_symbol(symbol):
    for item in data:
        if symbol.lower() == item['symbol'].lower():
            return item
    return None



def stock_get_quote(symbol):
    try:
        res = finnhub_client.quote(symbol=symbol)
        return res
    except esc.FinnhubAPIException:
        print(f"API limit reached wait 60 sec")
    except esc.FinnhubRequestException:
        print("FinnhubAPIException. Lets try after some time")

    return {}


def get_stock_details(symbol):
    stock = {}
    profile = finnhub_client.company_profile(symbol=symbol)
    stock['description'] = profile['name']
    stock['quote'] = finnhub_client.quote(symbol=symbol)
    stock['company_info'] = profile['description']
    stock['exchange'] = profile['exchange']
    stock['url'] = profile['weburl']
    stock['symbol'] = symbol
    stock['currency'] = profile['currency']
    return stock


def get_stock_cards(stocks):
    stock_names = []
    for stock in stocks:
        d = {'name': search_symbol(stock)['description'],
             'symbol': stock,
             'quote': finnhub_client.quote(stock)}
        stock_names.append(d)

    return stock_names


def search_stocks(name):
    if name:
        query_list = []

        for stock in data:
            if name.lower() in stock['description'].lower():
                query_list.append(stock['symbol'])

        stock_list = get_stock_cards(query_list)
        return stock_list
    else:
        return []


def get_popular_stocks():
    popular_stock_symbols = [
        'TSLA',
        'AAPL',
        'AMZN',
        'NFLX',
        'MSFT'
    ]

    stock_list = get_stock_cards(popular_stock_symbols)
    return stock_list
