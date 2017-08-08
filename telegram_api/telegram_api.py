import requests
import json


class TelegramAPI:

    TELEGRAM__BOT_API_URL = 'https://api.telegram.org/bot'
    API_TOKEN = '107989381:AAELyekLkl9EMzneRxHkqOF89fSQitltI2M'

    def __init__(self):
        pass

    def get_me(self):

        r = requests.get(self.TELEGRAM__BOT_API_URL + self.API_TOKEN + '/getMe')

        return self._get_result(json.loads(r.text))

    def get_messages(self):
        pass

    @staticmethod
    def _get_result(response):

        if response['ok']:
            return response['result']
        else:
            return response['error_code'], response['description']
