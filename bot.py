
import telebot

BOT_TOKEN = '7973616652:AAFmRe7VUGtJ3ARKdB5str1zi12fNtl4grM'
YOUR_CHAT_ID = 1322005220  # твой Telegram ID

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет! Напиши, пожалуйста, свой @username (или как с тобой связаться)."
    )
    # говорим боту: следующий ответ этого юзера обработать в функции get_username
    bot.register_next_step_handler(message, get_username)


def get_username(message):
    user_text = message.text  # что написал пользователь

    # отправляем инфу тебе
    bot.send_message(
        YOUR_CHAT_ID,
        f"Новый пользователь:\n"
        f"chat_id: {message.chat.id}\n"
        f"user_id: {message.from_user.id}\n"
        f"username из ответа: {user_text}"
    )

    # отвечаем пользователю
    bot.send_message(
        message.chat.id,
        "Спасибо! Данные переданы продавцу, скоро свяжемся 🙂"
    )


import time

while True:
    try:
        bot.polling()
    except Exception as e:
        if '409' in str(e):
            print('Error 409: Conflict. Restarting...')
            time.sleep(5)
        else:
            print(f'Bot error: {e}')
            time.sleep(2)

