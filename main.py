import telebot

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("TOKEN")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(
        message,
        f'Привет! Я бот {bot.get_me().first_name} и я помогу тебе заботиться о природе при помощи команд /ecology и /ecology_tip и ише /ecology2!'
    )

# Обработчик команды '/heh'


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

@bot.message_handler(commands=['help'])
def send_cooltip(message):
    bot.reply_to(
        message,
        'чтобы получить подсказки по экологии, используй команды /ecology, /ecology_tip и /ecology2. Если ты хочешь узнать, как правильно утилизировать отходы класса 1 до 4, используй команду /ecology.'
    )
# Запуск бота
bot.polling()
