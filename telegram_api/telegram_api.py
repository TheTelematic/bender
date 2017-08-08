import requests
import json

TELEGRAM__BOT_API_URL = 'https://api.telegram.org/bot'
API_TOKEN = '107989381:AAELyekLkl9EMzneRxHkqOF89fSQitltI2M'


class Brain:

    def __init__(self):
        pass

    @staticmethod
    def get_me():

        r = requests.get(TELEGRAM__BOT_API_URL + API_TOKEN + '/getMe')

        return json.loads(r.text)

    def get_messages(self):
        pass
