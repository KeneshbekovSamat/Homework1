import telebot

bot = telebot.TeleBot('pip freeze > requirements.txt')


@bot.message_handler(commands=['start'])
def main(messege):
    bot.send_message(messege.chat.id, 'Привет')

@bot.message_handler(commands=['myinfo'])
def main(messege):
    bot.send_message(messege.chat.id, f'Привет, {messege.from_user.first_name} {messege.from_user.id} ')

@bot.message_handler(commands=['random_pic'])
def start(message):
    file = open('./photo.jpeg', 'rb')
    bot.send_photo(message.chat.id, file)

bot.polling(none_stop=True)
