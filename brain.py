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

        threading.Timer(5, self.run).start()

    def process_messages(self):
        updates_json = self.get_updates(offset=self.last_update_id)

        for update in updates_json:

            up = Update(update)

            self.updates.append(up)

            print up

            self.last_update_id = up.update_id + 1
