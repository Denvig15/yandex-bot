import telebot
import time
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
YOUR_CHAT_ID = 1322005220

bot = telebot.TeleBot(BOT_TOKEN)

# обработчик ВСЕ сообщений - пересылает тебе
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_text = f"📨 {message.from_user.first_name}: {message.text}\nID: {message.from_user.id}"
    bot.send_message(YOUR_CHAT_ID, user_text)

while True:
    try:
        bot.polling()
    except Exception as e:
        if '409' in str(e):
            print('Error 409: Restarting...')
            time.sleep(5)
        else:
            print(f'Error: {e}')
            time.sleep(2)
