import ptbot
from dotenv import load_dotenv
import os
import random
from pytimeparse import parse

load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN') 
TG_CHAT_ID = os.getenv('TG_CHAT_ID')


def wait(chat_id, question):
    parsing = parse(question)
    bot.create_countdown(parsing, notify_progress, author_id=chat_id)
    message_id = bot.send_message(TG_CHAT_ID, "Моё сообщение")
    bot.create_timer(parsing, choose, author_id=chat_id)
    print('ID сообщения', message_id)


def notify_progress(secs_left, author_id):
    # message_id = bot.send_message(author_id, "Осталось {} секунд!".format(secs_left))
    bot.update_message(author_id, message_id, "Осталось {} секунд!".format(secs_left))



def choose(author_id):
    bot.send_message(author_id, 'Время вышло')




bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(wait)
bot.run_bot()

