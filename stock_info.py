import requests
import datetime


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "YKMLVQPWUGJ6ZHUE"

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = today - datetime.timedelta(days=2)


class StockData:
    """
    This class is used to get the stock data from the API call to "https://www.alphavantage.co/query"\n
    Required parameters to call the class:\n
    stock (str) : name of the stock to get the data of.
    """
    def __init__(self, stock: str):
        stock_parameters = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': stock,
            'apikey': STOCK_API_KEY,
        }
        response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
        response.raise_for_status()
        self.stock_data = response.json()['Time Series (Daily)']

    def get_stock_closing_data(self, day: int = 1):
        """
        Fetches the closing value of the stock of previous dates.\n
        Optional parameter:\n
        day(int): number of days prior to today
          (of when you need the data)
            default value: 1 (returns yesterday's data)
        :return: (type)float
        """
        try:
            req_date = today - datetime.timedelta(days=day)
            data = float(self.stock_data[str(req_date)]['4. close'])
            return data
        except KeyError:
            print("Invalid date input given to the get_stock_closing_data method of the StockData class")
