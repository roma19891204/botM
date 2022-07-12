import telebot

bot = telebot.TeleBot('5386005287:AAF1GsFML64bkHI7V29bhQ8vCLzPuvLLZ4E')

@bot.message_handler(['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


bot.polling(non_stop=True)