import ptbot
from dotenv import load_dotenv
import os
import random
from pytimeparse import parse

load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN') 
TG_CHAT_ID = os.getenv('TG_CHAT_ID')

def wait(chat_id, question):
    bot.create_timer(5, choose, author_id=chat_id, message=question)

def choose(author_id, message):
    bot.send_message(author_id, 'Время вышло')

    
bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(wait)
bot.run_bot()


