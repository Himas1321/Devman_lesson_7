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
    bot.create_timer(parsing, choose, chat_id=chat_id)
    


def notify_progress(secs_left, author_id):
    bot.send_message(author_id, "Осталось {} секунд!".format(secs_left))


def choose(chat_id):
    bot.send_message(chat_id, 'Время вышло')




bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(wait)
bot.run_bot()




