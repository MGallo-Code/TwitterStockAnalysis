import requests

class TwitRequest():
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token
    
    def get(self, url, params=None, headers=None):
        url = "https://api.twitter.com/2/" + url
        if headers is None:
            headers = {}
        headers["Authorization"] = f"Bearer {self.bearer_token}"
        return requests.get(url, headers=headers, params=params)

    def post(self, url, params=None, headers=None):
        url = "https://api.twitter.com/2/" + url
        if headers is None:
            headers = {}
        headers["Authorization"] = f"Bearer {self.bearer_token}"
        return requests.post(url, headers=headers, params=params)