import ptbot
from dotenv import load_dotenv
import os
import random
from pytimeparse import parse

load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN') 
TG_CHAT_ID = os.getenv('TG_CHAT_ID')

bot = ptbot.Bot(TG_TOKEN)


def wait(chat_id, question):
    parsing = parse(question)
    message_id = bot.send_message(chat_id, "Моё сообщение")
    bot.create_countdown(parsing, notify_progress,
                        chat_id=chat_id, message_id=message_id)
    bot.create_timer(parsing, choose, chat_id=chat_id)


def notify_progress(secs_left, chat_id, message_id):
    bot.update_message(chat_id, message_id, "Осталось {} секунд!".format(secs_left))
   


def choose(chat_id):
    bot.send_message(chat_id, 'Время вышло')


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    bot.reply_on_message(wait)
    bot.run_bot()


if __name__ == '__main__':
    main()


