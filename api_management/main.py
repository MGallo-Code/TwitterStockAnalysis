import os
from dotenv import load_dotenv, dotenv_values
from TwitRequest import TwitRequest

load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")

requester = TwitRequest(bearer_token)

res = requester.get("tweets", {"ids": "1261326399320715264,1278347468690915330"})
data = res.json()
print(res.json())

# Handle the data
if "data" in data:
    for tweet in data["data"]:
        print(f"Tweet ID: {tweet['id']}, Text: {tweet['text']}")

# Handle the errors
if "errors" in data:
    for error in data["errors"]:
        print(f"Error for Tweet ID {error['value']}: {error['detail']}")