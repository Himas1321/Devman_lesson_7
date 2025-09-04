import ptbot
from dotenv import load_dotenv
import os
import random
from pytimeparse import parse


load_dotenv()


TG_TOKEN = os.getenv('TG_TOKEN') 
TG_CHAT_ID = os.getenv('TG_CHAT_ID')
BOT = ptbot.Bot(TG_TOKEN)


def reply(chat_id, question):
    parsing = parse(question)
    message_id = BOT.send_message(chat_id, "Запуск таймера")
    BOT.create_countdown(parsing, notify, chat_id=chat_id, 
                         message_id=message_id, parsing=parsing)
    BOT.create_timer(parsing, choose, chat_id=chat_id)


def notify(secs_left, chat_id, message_id, parsing):
    BOT.update_message(chat_id, message_id, "Осталось {} секунд! \n {}" .format(secs_left, render_progressbar(parsing, secs_left )))
    

def choose(chat_id):
    BOT.send_message(chat_id, 'Время вышло')


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    BOT.reply_on_message(reply)
    BOT.run_bot()
    

if __name__ == '__main__':
    main()

