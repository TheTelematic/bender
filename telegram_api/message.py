class Message:
    def __init__(self, message_id, date, chat, text):
        """
        :param message_id: Unique message identifier inside this chat
        :type message_id: Integer
        :param date: Date the message was sent in Unix time
        :type date: Integer
        :param chat: Conversation the message belongs to
        :type chat: Chat
        :param text: For text messages, the actual UTF-8 text of the message, 0-4096 characters.
        :type text: String
        """
        self.message_id = message_id
        self.date = date
        self.chat = chat
        self.text = text

    def __str__(self):
        return str(self.message_id) + ':' + self.text + ' | ' + str(self.date) + ' - ' + str(self.chat)
