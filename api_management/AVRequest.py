from datetime import datetime, timedelta
import requests

class AVRequest():
    def __init__(self, key):
        self.stock_url = f"https://www.alphavantage.co/query?apikey={key}&datatype=json"
    
    def get_stocks_since_date(self, symbol, date, func="TIME_SERIES_DAILY"):
        # DATE IS YYYY-MM-DD
        url = self.stock_url + f"&function={func}&symbol={symbol}&date={date}"
        return requests.get(url).json()
    
    def get_1000_news_since_date(self, tickers, date):
        tickers_str = tickers[0]
        if len(tickers) > 1:
            tickers_str = ",".join(tickers)
        # DATE IS YYYYMMDDTHHMM
        url = self.stock_url + f"&function=NEWS_SENTIMENT&time_from={date}&tickers={tickers_str}&limit=1000"
        return requests.get(url).json()

    def get_news_since_date(self, tickers, year, month, day):
        curr_date = datetime.today().strftime('%Y%m%d')

        # day before the given date
        start_date = datetime(year, month, day) - timedelta(days=1)
        last_date = start_date.strftime('%Y%m%dT0000')

        news = {}

        # Keep looping while last news date is before current date
        #   because limited to 1000 per req
        while int(last_date.split('T')[0]) < int(curr_date):
            # parse the last news item date and increment it by 1 day
            last_news_date = datetime.strptime(last_news_item_date_str, '%Y%m%dT%H%M')
            next_date = last_news_date + timedelta(days=1)
            # update last_date for next request
            last_date = next_date.strftime('%Y%m%dT0000')

            # Fetch news since last_date
            fetched_news = self.get_1000_news_since_date(last_date, tickers)

            # break if no more news found
            if not fetched_news:
                break

            # add new news
            news = news + fetched_news

            # get last date YYYYMMDDTHHMM
            last_news_item_date_str = fetched_news[0]['date']

        return news