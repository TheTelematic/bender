import requests
import json


class TelegramAPI:

    def __init__(self):
        pass

    def get_me(self):

        return self._get_response('getMe')

    def get_messages(self):
        return self._get_response('getUpdates')

    def _get_response(self, method, **kwargs):
        """Make a request of the method and get a response from Telegram

        :param method: Method to send
        :param kwargs: Extra parameters
        :return:
        """

        return self._get_result(json.loads(self._do_request(method, **kwargs)))

    @staticmethod
    def _get_result(response):

        if response['ok']:
            return response['result']
        else:
            raise Exception('**ERROR**\nError code: {}\nDescription:{}\n'.format(response['error_code']))

    TELEGRAM__BOT_API_URL = 'https://api.telegram.org/bot'
    API_TOKEN = '107989381:AAELyekLkl9EMzneRxHkqOF89fSQitltI2M'

    def _do_request(self, method, **kwargs):
        """Do a request to the Telegram Bot API

        :param method: Method to send
        :param kwargs: Extra parameters
        :return:
        """

        return requests.get(self.TELEGRAM__BOT_API_URL + self.API_TOKEN + '/' + method).text
