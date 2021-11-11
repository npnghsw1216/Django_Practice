import os
import sys
import time
import pprint

import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
import tasks

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    print("TELEGRAM_TOKEN 환경변수를 지정해주세요.",file=sys.stderr)
    sys.exit(1) # 종료 상태값을 1로 지정하고, 프로그램 종료


updater=Updater(token=TELEGRAM_TOKEN,use_context=True)
dispatcher=updater.dispatcher

def start(update,context):
    """대화방이 처음 열리면 자동으로 호출"""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi! 에이치 아이~"
    )
def echo(update, context):
    received_text:str =update.message.text

    if tasks.ya.check_available(received_text):
        response_text = tasks.ya.make_response(received_text)
    elif tasks.naver_search.check_available(received_text):
        response_text = tasks.naver_search.make_response(received_text)
    elif tasks.daum_search.check_available(received_text):
        response_text = tasks.daum_search.make_response(received_text)
    elif tasks.covid.check_available(received_text):
        response_text = tasks.covid.make_response(received_text)
    elif tasks.who_are_you.check_available(received_text):
        response_text = tasks.who_are_you.make_response(received_text)
    elif tasks.time.check_available(received_text):
        response_text = tasks.time.make_response()
    else:
        response_text="지원하지 않는 명령입니다"

    #tasks.naver_search(query)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response_text)

start_handler=CommandHandler("start",start)
dispatcher.add_handler(start_handler)

echo_handler=MessageHandler(
    Filters.text&(~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)
updater.start_polling()