import datetime

from message import Message


class Update:
    """

        update_id: The update's unique identifier. Update identifiers start from a certain positive number and increase
                    sequentially

        message: New incoming message of any kind - text, photo, sticker, etc.

    """
    def __init__(self, update_message):
        """
        :param update_message: Update received in JSON format
        :type update_message: Dict
        """
        if 'document' in update_message['message'] \
                or 'sticker' in update_message['message'] or 'audio' in update_message['message']:

            self.update_id = update_message['update_id']
            self.message = Message(message_id=update_message['message']['message_id'],
                                   date=update_message['message']['date'], chat=update_message['message']['chat'],
                                   text='Media found, this is not supported yet.')
        else:
            self.update_id = update_message['update_id']
            self.message = Message(message_id=update_message['message']['message_id'],
                                   date=update_message['message']['date'], chat=update_message['message']['chat'],
                                   text=update_message['message']['text'])

    def __str__(self):
        return '{}[{}] {}\n'.format(datetime.datetime.now().__str__(), self.update_id, self.message.__str__()
                                    .encode('unicode-escape'))
