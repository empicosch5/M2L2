import telebot
from random import get_random_tip  

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("токен")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(
        message,
        f'Привет! Я бот {bot.get_me().first_name} и я помогу тебе заботиться о природе при помощи команд /ecology, /ecology_tip, /ecology2 und /tip!'
    )

@bot.message_handler(commands=['ecology'])
def send_ecology(message):
    bot.reply_to(
        message,
        'Чтобы помочь с проблемой экологии, надо сначала утилизировать отходы классов 1 до 4. Например, батарейки — 2 класс. Как их правильно утилизировать, можешь найти на сайте: https://vinser.ru/info/utilizaciya-othodov-1-4-klassov-opasnosti'
    )

@bot.message_handler(commands=['ecology_tip'])
def send_tip(message):
    bot.reply_to(
        message,
        'Вот подсказка: НИКОГДА не выбрасывай мусор в природу! Просто найди мусорку, а если это отход опасного класса — утилизируй его правильно!'
    )

@bot.message_handler(commands=['ecology2'])
def send_cooltip(message):
    bot.reply_to(
        message,
        'Для утилизации отходов класса 1 их нужно перевозить в безопасных контейнерах, потому что этот класс может нанести большой вред экологии, если попадет в окружающую среду!'
    )

@bot.message_handler(commands=['tip'])
def send_random_tip(message):
    tip = get_random_tip()
    bot.reply_to(message, tip)

# Запуск бота
bot.polling()
