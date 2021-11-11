import pprint

import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
import tasks

token = ""
updater=Updater(token=token,use_context=True)

dispatcher=updater.dispatcher

def start(update,context):
    """대화방이 처음 열리면 자동으로 호출"""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="안녕 나는 커비야 반가워!"
    )
def echo(update, context):
    received_text:str =update.message.text

    if tasks.ya.check_available(received_text):
        response_text = tasks.ya.make_response(received_text)
    elif tasks.naver_search_avilable(received_text):
        resource_text = tasks.naver_search.make_response(received_text)
    else:
        reply_text="지원하지 않는 명령입니다"

    #tasks.naver_search(query)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=resource_text)

start_handler=CommandHandler("start",start)
dispatcher.add_handler(start_handler)

echo_handler=MessageHandler(
    Filters.text&(~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)
updater.start_polling()