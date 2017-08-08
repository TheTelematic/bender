from telegram_api.telegram_api import Brain

me = Brain.get_me()

print me['ok']
