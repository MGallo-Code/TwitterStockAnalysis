from AVRequest import AVRequest
from dotenv import load_dotenv
import os
import requests

load_dotenv()

av_key = os.getenv("ALPHA_VANTAGE_KEY")

requester = AVRequest(av_key)
data = requester.get_stock_at_date("AAPL", "2017-11-15")

print(data)