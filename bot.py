#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'Вставьте ваш ТОКЕН'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🔥Git ")
	item2 = types.KeyboardButton("🤝Гоу в ЛС)")
	item3 = types.KeyboardButton("📩Депеша")
	item4 = types.KeyboardButton("🕸Web")

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Шо ты КАК, {0.first_name}?)".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🔥Git':
			bot.send_message(message.chat.id, 'https://github.com/StanislavGanin')
		elif message.text == '🤝Гоу в ЛС)':
			bot.send_message(message.chat.id, 'https://t.me/QAStanislav')
		elif message.text == '📩Депеша':
			bot.send_message(message.chat.id, 'qaganin@gmail.com')
		elif message.text == '🕸Чекни CV':
			bot.send_message(message.chat.id, 'https://stanislavganin.ru/')
		else:
			bot.send_message(message.chat.id, 'https://stanislavganin.ru/')


bot.polling(none_stop=True)
