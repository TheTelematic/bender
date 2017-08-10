import requests
import json
from parameters import TELEGRAM_BOT_API_URL, TELEGRAM_BOT_API_TOKEN


class TelegramAPI:

    def __init__(self):
        pass

    def get_me(self):

        return self._get_response('getMe')

    def get_updates(self, offset=None):
        return self._get_response('getUpdates', offset=offset)

    def send_message(self, chat_id, text, parse_mode='Markdown'):

        return self._get_response('sendMessage', chat_id=chat_id, text=text, parse_mode=parse_mode)

    """
        Private methods
    """

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
            raise Exception('**ERROR**\nError code: {}\nDescription:{}\n'.format(response['error_code'],
                                                                                 response['description']))

    @staticmethod
    def _do_request(method, **kwargs):
        """Do a request to the Telegram Bot API

        :param method: Method to send
        :param kwargs: Extra parameters
        :return:
        """
        query = TELEGRAM_BOT_API_URL + TELEGRAM_BOT_API_TOKEN + '/' + method
        payload = {}

        for key, value in kwargs.iteritems():
            payload[key] = value

        return requests.post(query, data=payload).text
