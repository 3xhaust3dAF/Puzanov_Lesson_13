import telebot
from random import choice
token = '6178872349:AAEs99Pg2_seenBONX2OdJhqpQy3sGUJCCU'
bot = telebot.TeleBot(token)
from telebot import types
def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    joke = types.InlineKeyboardButton(text='A joke', callback_data='1')
    hello = types.InlineKeyboardButton(text='Say hello', callback_data='2')
    bye = types.InlineKeyboardButton(text='Say goodbye', callback_data='3')
    sleep = types.InlineKeyboardButton(text='Go to sleep', callback_data='4')
    weather = types.InlineKeyboardButton(text='Get weather', callback_data='5')
    keyboard.add(joke, hello, bye, sleep, weather)
    return keyboard

jokes = [
    'Сборная России по футболу - сдавайте клюшки, снимайте коньки: мы вас узнали!',
    'Настоящий мужик никогда не ищет утром свои носки! Потому что он в них спит.',
    'Лучше всего он разбирался в том, что его абсолютно не касалось',
    'Проводим Старый год, собаки! С Новым годом, свиньи!',
    'Считается, что ум человека делится на два типа. Математический и еще какой-то.',
    '- Попросите к телефону Абрама!- Вы сюда не попали!',
    'Цезарь делал сто дел, а Брут сосредоточился и сделал одно.',
    '- Доктор, я умираю, помогите!- Во народ! Уже и умереть сами не могут!'
]

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Choose!', reply_markup=create_keyboard())

@bot.callback_query_handler(func= lambda call: True if call.message else False)
def callback_inline(call):
    if call.data == '1':
        bot.send_message(call.message.chat.id, choice(jokes), reply_markup=create_keyboard())
    if call.data == '2':
        bot.send_message(call.message.chat.id, 'Greetings! Great to see you!', reply_markup=create_keyboard())
    if call.data == '3':
        bot.send_message(call.message.chat.id, 'It was great seeing you! Farewell.', reply_markup=create_keyboard())
    if call.data == '4':
        bot.send_message(call.message.chat.id, 'You look tired. Indeed, you need to go to bed. Goodnight!', reply_markup=create_keyboard())
    if call.data == '5':
        bot.send_message(call.message.chat.id, 'Weekly weather: https://www.gismeteo.by/weather-minsk-4248/10-days/', reply_markup=create_keyboard())

bot.polling(none_stop=True)
