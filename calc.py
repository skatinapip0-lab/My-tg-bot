import telebot

# Твой токен тут
bot = telebot.TeleBot("8763385275:AAF7CLd1vBQpjLtEOqUG1_XCL3rB7WiKhkU")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "О, заработало! Я на связи.")

# Эта штука ловит ВООБЩЕ ВСЁ
@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        # Пытаемся посчитать
        result = eval(message.text)
        bot.send_message(message.chat.id, f"Результат: {result}")
    except:
        # Если прислали текст, который нельзя посчитать
        bot.send_message(message.chat.id, f"Ты написал: {message.text}. А я жду пример, например 2+2")
bot.polling(none_stop=True)