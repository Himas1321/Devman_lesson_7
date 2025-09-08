import ptbot
from dotenv import load_dotenv
import os
import random
from pytimeparse import parse


def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(reply, bot=bot)
    bot.run_bot()
   
def reply(chat_id, question, **bot):
    
    parsing = parse(question)
    message_id = bot.send_message(chat_id, "Запуск таймера")
    bot.create_countdown(bot, parsing, notify, chat_id=chat_id, 
                         message_id=message_id, parsing=parsing)
    bot.create_timer(parsing, choose, chat_id=chat_id)


def notify(secs_left, chat_id, message_id, parsing,**bot):
    bot.update_message(chat_id, message_id, "Осталось {} секунд! \n {}" .format(secs_left, render_progressbar(parsing, secs_left )))
    

def choose(chat_id, **bot):
    bot.send_message(chat_id, 'Время вышло')


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)



if __name__ == '__main__':
    main()


