import sys

from body import answers
from body.memory import COMMAND_TALK, UNKNOWN_COMMAND, COMMAND_NEW
from body import subconscient

import threading

from telegram_api.telegram_api import TelegramAPI
from telegram_api.update import Update


class Brain(TelegramAPI):
    updates = []
    last_update_id = 0

    def __init__(self):
        TelegramAPI.__init__(self)
        self.graceful_shutdown = False

        print "Welcome to Bender bot!"

        threading.Thread(target=self.worker_shell).start()

    def run(self):
        if self.graceful_shutdown:
            exit(0)

        self.process_messages()

        threading.Timer(2, self.run).start()

    def process_messages(self):

        log = open('log.txt', mode='a')

        updates_json = self.get_updates(offset=self.last_update_id)

        for update in updates_json:
            up = Update(update)

            self.updates.append(up)

            log.write(up.__str__())
            log.flush()

            self.last_update_id = up.update_id + 1

            # print "LAST UPDATE ID:", self.last_update_id

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

        elif text == COMMAND_NEW:
            return subconscient.get_new()

        return UNKNOWN_COMMAND

    def worker_shell(self):
        before_command = ''
        while 1:
            command = ''
            try:
                command = raw_input('> ')
            except EOFError:
                self.graceful_shutdown = True

            if command == '':
                command = before_command

            if command == 'skip' or command == 'go':
                print "Skipping messages"
                self.last_update_id += 1
                print self.last_update_id
            elif command == 'exit' or command == 'q':
                print 'Exiting...'
                self.graceful_shutdown = True
                break

            before_command = command
