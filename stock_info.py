import requests
import datetime


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "YKMLVQPWUGJ6ZHUE"

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = today - datetime.timedelta(days=2)


class APILimitError(Exception):
    """raised when the API call limit is reached"""
    pass


class StockData:
    """
    This class is used to get the stock data from the API call to "https://www.alphavantage.co/query"\n
    Required parameters to call the class:\n
    stock (str) : name of the stock to get the data of.
    """
    def __init__(self, stock: str):
        self.api_call_valid = True
        stock_parameters = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': stock,
            'apikey': STOCK_API_KEY,
        }
        response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
        response.raise_for_status()
        try:
            if 'Information' in response.json():
                raise APILimitError
            else:
                self.stock_data = response.json()['Time Series (Daily)']
        except APILimitError:
            self.api_call_valid = False
            print('Standard API rate limit is 25 requests per day. Please subscribe to any of the premium plans '
                  'at https://www.alphavantage.co/premium/ to instantly remove all daily rate limits.')

    def get_stock_data(self, day: int = 1) -> dict:
        """
        Fetches the data related to the stock of previous dates.\n
        Optional parameter:\n
        day(int): number of days prior to today
          (of when you need the data)
            default value: 1 (returns yesterday's data)
        :return: (type)dict - returns the list of stock data {open_price: type(float),
                                                                day_high: type(float), day_low: type(float),
                                                                close_price: type(float)}
        """
        if self.api_call_valid:
            try:
                req_date = today - datetime.timedelta(days=day)
                data_dict = {
                    'open_price': float(self.stock_data[str(req_date)]['1. open']),
                    'day_high': float(self.stock_data[str(req_date)]['2. high']),
                    'day_low': float(self.stock_data[str(req_date)]['3. low']),
                    'close_price': float(self.stock_data[str(req_date)]['4. close']),
                }
                return data_dict
            except KeyError:
                return {'Error': 'Invalid date input given to the get_stock_data method of the StockData class'}
        else:
            return {'Error': 'API limit reached. Try again tomorrow.'}
