import requests

class AVRequest():
    def __init__(self, key):
        self.stock_url = f"https://www.alphavantage.co/query?apikey={key}&datatype=json"
    
    def get_stocks_since_date(self, symbol, date, func="TIME_SERIES_DAILY"):
        # DATE IS YYYY-MM-DD
        url = self.stock_url + f"&function={func}&symbol={symbol}&date={date}"
        return requests.get(url).json()