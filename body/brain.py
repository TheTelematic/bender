from body import answers
from body.memory import COMMAND_TALK, UNKNOWN_COMMAND
from telegram_api.telegram_api import TelegramAPI
import threading

from telegram_api.update import Update


class Brain(TelegramAPI):
    updates = []
    last_update_id = 0

    def __init__(self):
        TelegramAPI.__init__(self)

    def run(self):
        self.process_messages()

        threading.Timer(2, self.run).start()

    def process_messages(self):
        updates_json = self.get_updates(offset=self.last_update_id)

        for update in updates_json:
            up = Update(update)

            self.updates.append(up)

            print up

            self.last_update_id = up.update_id + 1

            self.get_answer(up.message)

    def get_answer(self, message):

        chat_id = message.chat['id']

        if message.text[0] == '/':

            text = self.process_command(message.text)

        else:

            text = self._get_text_message(message.chat)

        self.send_message(chat_id=chat_id, text=text)

    @staticmethod
    def _get_text_message(chat):
        text = "Hello {}".format(chat['first_name'])

        if chat['username'] == 'civico92':
            text += ', nano mola mas'

        elif chat['username'] == 'TheTelematic':
            text = 'Hey Boss!'

        return text

    @staticmethod
    def process_command(text):

        if text == COMMAND_TALK:

            return answers.RandomAnswer.get()

        return UNKNOWN_COMMAND
