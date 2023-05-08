import telebot

bot = telebot.TeleBot("6151963303:AAFP9eCp_sGahYiQvAp9rqVpowz4qMIrlI0")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)

bot.polling(none_stop = True)