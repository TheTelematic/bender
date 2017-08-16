import unirest as unirest

from body.secrets import TOKEN_API_MASHAPE


class RandomAnswer:

    def __init__(self):
        pass

    @staticmethod
    def get():

        url = 'https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies&count=1'

        payload = {'X-Mashape-Key': TOKEN_API_MASHAPE, 'Content-Type': "application/x-www-form-urlencoded",
                   'Accept': 'application/json'}

        response = unirest.post(url=url, headers=payload)

        quote = response.body

        return quote['quote'] + ' - __' + quote['author'] + '__'
