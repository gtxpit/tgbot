import requests
import telebot
from telebot import types
bot = telebot.TeleBot ("6887880331:AAH9vDIwQNMcgymo8E1ajtCHGhH6tP-CwAo")


@bot.message_handler(commands=["start"])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = ("часовой пояс")
    markup.add(item1)
    bot.send_message(m.chat.id, "бот работает!!" , reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(m):
    if m.text.strip() == "часовой пояс":
        messg = bot.send_message(m.chat.id, "Введите ваш город")
        bot.register_next_step_handler(messg, sms)

def sms(m):
    city = m.text
    api_url = 'https://api.api-ninjas.com/v1/timezone?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'INssUwRQjjXITaArFPCLBA==VBCaFxP1TdE3zhcs'})
    if response.status_code == requests.codes.ok:
        print(response.text)
        txt = eval(response.text)["timezone"]
        bot.send_message(m.chat.id, "Ваша таймзона - " + txt)
    else:
        print("Error:", response.status_code, response.text)



bot.polling(none_stop=True, interval=0)