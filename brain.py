from telegram_api.telegram_api import TelegramAPI
import threading


class Brain(TelegramAPI):

    def __init__(self):
        TelegramAPI.__init__(self)

    def run(self):

        messages = self.get_messages()



        threading.Timer(5, self.run).start()
