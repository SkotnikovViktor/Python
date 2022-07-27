





# Импорт библиотеки telebot и time
import telebot
import json
# Создание переменной с токеном
bot = telebot.TeleBot('5505530308:AAGoiiUP5dD6GP6eM_3b5AfHJQrVdDXFXQI')

# Функция которая узнает время


with open('file.json','r') as file:
    a = json.load(file)
    

# Создание кнопки в чате [start] + вложенная функция
@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Привет! <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id,mess,parse_mode = 'html')


# Обработка чата и вывод времени 
@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет!':
        bot.send_message(message.chat.id,'Привет мой друг!')
    elif message.text == 'Как дела?':
        bot.send_message(message.chat.id,'Нормально')
    elif message.text == 'Steam':
        bot.send_message(message.chat.id,a)
    elif message.text == 'Hello':
        bot.send_message(message.chat.id,'Нi!')
    elif message.text == 'Name?':
        bot.send_message(message.chat.id, 'BotOnPython!')
    elif message.text == 'Калькулятор!':
        bot.send_message(message.chat.id,'Выберите сложение, вычитание, умножение или деление')
    elif message.text == 'Сложение':
        bot.send_message(message.chat.id,'Напишите числа!')
        if message.text == "5":
            firstnumber = message.text
            bot.send_message(message.chat.id,firstnumber)
        elif message.text == "5":
            secondnumber = message.text
            bot.send_message(message.chat.id,secondnumber)
            


# Запуск бота
bot.polling(none_stop = True)

