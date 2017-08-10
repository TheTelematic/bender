import json

import requests

from body.secrets import TOKEN_API_MASHAPE


class RandomAnswer:

    def __init__(self):
        pass

    @staticmethod
    def get():
        response = requests.post('https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies',
                                 data={
                                     "X-Mashape-Key": TOKEN_API_MASHAPE,
                                     "Content-Type": "application/x-www-form-urlencoded",
                                     "Accept": "application/json"
                                 }).text

        quote = json.loads(response)

        print quote
        return quote
