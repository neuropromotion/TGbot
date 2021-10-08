from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import telebot
owm = OWM('2b3175d5116fab7ff2e63169233c9fce')
mgr = owm.weather_manager() 
bot = telebot.TeleBot("2072071285:AAELgCFHqFUZDrlXHPjAWnJp-Omig063fik", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message): 
	bot.reply_to(message, "In which city do you want to know weather?")

@bot.message_handler(content_types=['text'])
def send_weather(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    cloud_speed = w.wind()['speed']
    temp = w.temperature('celsius')["temp"]
    answer = "В городе " + message.text + " на данный момент следующие погодные условия:\n"
    answer += "Teмпература: " + str(temp) + " градусов Цельсия\n"
    answer += "Влажность воздуха: " + str(w.humidity) + "%\n"
    answer += "Скорость воздуха: " + str(cloud_speed) + " метров в секунду\n"
    bot.send_message (message.chat.id, answer)

bot.polling(non_stop = True)
