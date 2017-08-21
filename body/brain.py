from body import answers, converter
from body import eyes
from body.memory import *
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

        eyes.print_blue("Welcome to Bender bot!", bold=True)

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

            text, method = self.process_command(message.text)

            method(chat_id, text)

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

    def process_command(self, text):

        splitted_commands = text.split(' ')

        if splitted_commands[0] == COMMAND_TALK:

            return answers.RandomAnswer.get(), self.send_message

        elif splitted_commands[0] == COMMAND_NEW:
            return subconscient.get_new(), self.send_message

        elif splitted_commands[0] == COMMAND_START:

            help = COMMAND_TALK + ' -> ' + HELP_TALK + '\n'
            help += COMMAND_NEW + ' -> ' + HELP_NEW + '\n'
            help += COMMAND_YOUTUBE2MP3 + ' -> ' + HELP_YOUTUBE2MP3 + '\n'

            return help, self.send_message

        elif splitted_commands[0] == COMMAND_YOUTUBE2MP3:
            if len(splitted_commands) == 1:
                return 'Debe de especificar la url del video junto al comando (separado por un espacio)', \
                       self.send_message

            url_videos = splitted_commands[1].split('\n')

            urls_audios = converter.youtube2mp3(url_videos)

            return urls_audios, self.send_audios

        return UNKNOWN_COMMAND, self.send_message

    def worker_shell(self):

        before_command = ''

        while 1:
            command = ''
            try:
                eyes.print_green('> ', newline='')
                command = raw_input()
            except EOFError:
                self.graceful_shutdown = True

            if command == '':
                command = before_command

            if command == 'skip' or command == 'go':
                eyes.print_warning("Skipping messages")
                self.last_update_id += 1
                print self.last_update_id
            elif command == 'exit' or command == 'q':
                eyes.print_warning('Exiting...')
                self.graceful_shutdown = True
                break

            before_command = command

    def send_audios(self, chat_id, audios):

        for audio in audios:

            self.send_message(chat_id=chat_id, text=audio['title'])

            # self.send_audio(chat_id=chat_id, url=audio['link'])  # Da un error 400

            self.send_message(chat_id=chat_id, text=audio['link'])
