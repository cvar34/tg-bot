import telebot
from bot_logic import pass_gen, flip_coin
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['genpass'])
def send_pass(message):
    bot.reply_to(message, pass_gen(5))

@bot.message_handler(commands=['flipcoin'])
def send_coin(message):
    bot.reply_to(message, flip_coin())

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('images/mem1.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def on_user_joins(message):

    user = message.new_chat_members[0]

    name = user.first_name
    if hasattr(user, 'last_name') and user.last_name is not None:
        name += u" {}".format(user.last_name)

    if hasattr(user, 'username') and user.username is not None:
        name += u" (@{})".format(user.username)

    bot.reply_to(message, "Привет, {name}".format(name=name))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()