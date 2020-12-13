import json
import time
import telebot
from telebot import types
from bs4 import BeautifulSoup
from urllib.request import urlopen
from multiprocessing import *
import schedule
from validate_email import validate_email
import requests

bot = telebot.TeleBot('1250487291:AAEd2xynjPPTYXRoaZd0SBlY540wqdt1y4w')

user_dict = {}
dishes_dict = {}
body_dict = {}
ration_dict = {}
url_api = 'http://localhost:8080/api/'
headers_dict = {
    'Content-Type': 'application/json'
}
id = 469272479

class User:
    def __init__(self, idChat):
        self.idChat = idChat
        self.name = None
        self.email = None
        self.password = None


class Body:
    def __init__(self, idChat):
        self.idChat = idChat
        self.weight = None
        self.height = None
        self.age = None
        self.bmr = None
        self.amr = None
        self.calRate = None
        self.purpose = None
        self.typeDiet = None
        self.gender = None

class Dish:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.type = None
        self.calories = None
        self.proteins = None
        self.fats = None
        self.carbohydrates = None

class Ration:
    def __init__(self, id):
        self.id = id
        self.date = None
        self.purpose = None
        self.breakfast = None
        self.lunch = None
        self.dinner = None
        self.user = None


def get_info(response):
    for item in response:
       user = User(item['idChat'])
       user.name = item['name']
       user.email = item['email']
       user.password = item['password']
       body = Body(item['body']['idChat'])
       body.weight = item['body']['weight']
       body.height = item['body']['height']
       body.age = item['body']['age']
       body.calRate = item['body']['calRate']
       body.gender = item['body']['gender']
       body.amr = item['body']['amr']
       body.bmr = item['body']['gender']
       body.purpose = item['body']['purpose']
       body.typeDiet = item['body']['typeDiet']
       user_dict[item['idChat']] = user
       body_dict[item['idChat']] = body

@bot.message_handler(commands=['start'])
def start_message(message):
    mess = 'Привет! Выберите действия:\n' \
           '/registration - регистрация \n' \
           '/login - вход в аккаунт'
    print(message.chat.id)
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/registration', '/login')
    bot.send_message(message.from_user.id, text=mess, reply_markup=keyboard)

@bot.message_handler(commands=['registration'])
def call_registration(message):
    response = requests.get('http://localhost:8080/api/user/%s' % message.chat.id)
    print(response.status_code)
    if response.status_code == 200:
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы, введите "/login"')
        start_message(message)
        return
    else:
        user = User(message.chat.id)
        body = Body(message.chat.id)
        body_dict[message.chat.id] = body
        user_dict[message.chat.id] = user
        print(user.name)
        bot.send_message(message.chat.id, 'Давайте знакомиться!', reply_markup=types.ReplyKeyboardRemove())
        ask_name(message.from_user.first_name, message)  # -----  call getting NAME

@bot.message_handler(commands=['login'])
def ask_login(message):
    #user = user_dict[message.chat.id]

    response = requests.get('http://localhost:8080/api/user/%s' % message.chat.id)
    if response.status_code == 200:
        print('ok')
        get_info(response.json())
        msg = user_dict[message.chat.id].name + ', с возвращением!'
        bot.send_message(message.chat.id, msg,
                         reply_markup=types.ReplyKeyboardRemove())
        main_menu(message)
        return
    else:
        bot.send_message(message.chat.id, 'Вы не зарегистрированны, пройдите регистрацию', reply_markup=types.ReplyKeyboardRemove())
        call_registration(message)

#------------------------------------------------   GET THE NAME    ------------------------------------------------#

def ask_name(get_name,message):
    user = user_dict[message.chat.id]
    user.name = get_name
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = "Это Ваше имя?\n" + user.name
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


def get_name(message):
    user = user_dict[message.chat.id]
    user.name = message.text
    ask_name(user.name, message)

#------------------------------------------------   GETTING EMAIL  -------------------------------------------#

def get_mail(message):
    user = user_dict[message.chat.id]
    user.email = message.text
    if not validate_email(user.email):
        msg = bot.reply_to(message, 'Эл.почта не верна. Ввведите повторно:')
        bot.register_next_step_handler(msg, get_mail)
        return
    bot.send_message(message.chat.id, 'Отлично, регистрация окончена')
    ask_age(message)



#------------------------------------------------   GET AGE    ------------------------------------------------#

def ask_age(message):
    user = user_dict[message.chat.id]
    mess = str(user.name) + ', для точной работы сервиса, нужно узнать некоторую информацию.'
    bot.send_message(message.chat.id, mess)
    time.sleep(2)
    bot.send_message(message.chat.id, 'Сколько Вам лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    user = user_dict[message.chat.id]
    body = body_dict[message.chat.id]
    body.age = message.text
    if not body.age.isdigit():
        msg = bot.reply_to(message, 'Возвраст должен быть числом. Сколько Вам лет?')
        bot.register_next_step_handler(msg, get_age)
        return
    keyboard = types.InlineKeyboardMarkup()
    key_MALE = types.InlineKeyboardButton(text='Мужчина', callback_data='MALE')
    keyboard.add(key_MALE)
    key_FEMALE = types.InlineKeyboardButton(text='Женщина', callback_data='FEMALE')
    keyboard.add(key_FEMALE)
    bot.send_message(message.from_user.id, text="Ваш пол?", reply_markup=keyboard)

#------------------------------------------------   GET WEIGHT    ------------------------------------------------#

def get_weight(message):
    body = body_dict[message.chat.id]
    body.weight = message.text
    try:
        body.weight = float(body.weight)
    except:
        bot.reply_to(message, 'Вес должен быть числом. Ваш вес?')
        bot.register_next_step_handler(message, get_weight)
        return
    bot.send_message(message.chat.id, 'Ваш рост?')
    bot.register_next_step_handler(message, get_height)

#------------------------------------------------   GET HEIGHT    ------------------------------------------------#

def get_height(message):
    body = body_dict[message.chat.id]
    body.height = message.text
    try:
        body.height = float(body.height)
    except:
        bot.reply_to(message, 'Рост должен быть числом. Ваш рост?')
        bot.register_next_step_handler(message, get_height)
        return
    keyboard = types.InlineKeyboardMarkup()
    key_slim = types.InlineKeyboardButton(text='Похудеть', callback_data='slim')
    keyboard.add(key_slim)
    key_gain = types.InlineKeyboardButton(text='Набрать вес', callback_data='gain')
    keyboard.add(key_gain)
    key_save = types.InlineKeyboardButton(text='Сохранить вес', callback_data='save')
    keyboard.add(key_save)
    bot.send_message(message.from_user.id, text="Ваша цель с весом?", reply_markup=keyboard)

#------------------------------------------------   GET PURPOSE    ------------------------------------------------#


def get_purpose(call):
    body = body_dict[call.message.chat.id]
    if (call.data == 'slim'):
        body.purpose = 0
    if (call.data == 'gain'):
        body.purpose = 1
    if (call.data == 'save'):
        body.purpose = 2
    keyboard = types.InlineKeyboardMarkup()
    key_normal = types.InlineKeyboardButton(text='Неважно', callback_data='normal')
    keyboard.add(key_normal)
    key_vegetarian = types.InlineKeyboardButton(text='Вегатарианская еда', callback_data='vegetarian')
    keyboard.add(key_vegetarian)
    key_vegan = types.InlineKeyboardButton(text='Веганская еда', callback_data='vegan')
    keyboard.add(key_vegan)
    key_lenten = types.InlineKeyboardButton(text='Постная еда', callback_data='lenten')
    keyboard.add(key_lenten)
    key_diabet = types.InlineKeyboardButton(text='Меню при диабете', callback_data='diabet')
    keyboard.add(key_diabet)
    bot.send_message(call.message.chat.id, text="Какое меню предпочитаете?", reply_markup=keyboard)

#------------------------------------------------   GET DIET    ------------------------------------------------#

def get_diet(call):
    body = body_dict[call.message.chat.id]
    body.typeDiet = call.data
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='Сидячий образ жизни', callback_data=1.2)
    keyboard.add(key_1)
    key_2 = types.InlineKeyboardButton(text='Умеренная активность (легкие физические нагрузки (тренировки) 1-3 раз в неделю)',
                                           callback_data=1.375)
    keyboard.add(key_2)
    key_3 = types.InlineKeyboardButton(text='Средняя активность (тренировки 3-5 раз в неделю)', callback_data=1.55)
    keyboard.add(key_3)
    key_4 = types.InlineKeyboardButton(text='Активные люди (интенсивные нагрузки 6-7 раз в неделю)', callback_data=1.725)
    keyboard.add(key_4)
    key_5 = types.InlineKeyboardButton(text='Спортсмены и люди, выполняющие тяжелые физические нагрузки (6-7 раз в неделю)',
                                            callback_data=1.9)
    keyboard.add(key_5)
    bot.send_message(call.message.chat.id, text="Ваш образ жизни?", reply_markup=keyboard)

#------------------------------------------------   MAIN MENU    ------------------------------------------------#

def main_menu(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    mess = 'Главное меню. Выберите действия:\n' \
           '/menu - составить меню\n' \
           '/update обновить информацию\n'
    keyboard.row('/menu', '/update')
    bot.send_message(message.chat.id, text=mess, reply_markup=keyboard)

@bot.message_handler(commands=['menu'])
def menu(message):
    response = requests.get('http://localhost:8080/api/ration?idChat=%s' % message.chat.id)
    if response.status_code == 200:
        data = response.json()
        bot.send_message(message.chat.id, 'Меню на ' + data['date'] + ':')
        bot.send_message(message.chat.id, 'Завтрак: ' + data['breakfast']['name'] + '\n' + \
                data['breakfast']['url'])
        bot.send_message(message.chat.id, 'Обед: '+ data['lunch']['name'] + '\n' +\
                data['lunch']['url'])
        bot.send_message(message.chat.id, 'Ужин: ' + data['dinner']['name'] + '\n' +\
                data['dinner']['url'])
    main_menu(message)


@bot.message_handler(commands=['update'])
def update(message):
    user = user_dict[message.chat.id]
    bot.send_message(message.chat.id, 'Для измения информации нужно перейти на сайт:\n http://localhost:8080/\n')
    bot.send_message(message.chat.id, 'Логин для входа на сайт: ' + str(user.idChat) + '\n')
    bot.send_message(message.chat.id, 'Пароль: ' + str(user.password) + '\n')
    main_menu(message)


#------------------------------------------------   KEYBOARD UNDER MESSAGE    ------------------------------------------------#

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    user = user_dict[call.message.chat.id]
    body = body_dict[call.message.chat.id]
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
        bot.send_message(call.message.chat.id, 'Ввведите свою почту')
        bot.register_next_step_handler(call.message, get_mail)  #----- call to get mail
    if call.data == "no":
        bot.send_message(call.message.chat.id, "Как тебя зовут?")
        bot.register_next_step_handler(call.message, get_name)
    if call.data == "FEMALE" or call.data == "MALE":
        body.gender = call.data
        bot.send_message(call.message.chat.id, 'Сколько вы весите?')
        bot.register_next_step_handler(call.message, get_weight)  #----- call to get weight
    if call.data == "slim" or call.data == "gain" or call.data == "save":
        get_purpose(call) #----- call to get purpose
    if call.data == "normal" or call.data == "vegetarian" or call.data == "vegan" or call.data == "lenten" or \
            call.data == "diabet":
        get_diet(call)
    if call.data == "1.2" or call.data == "1.375" or call.data == "1.55" or call.data == "1.725" or call.data == "1.9":
        body.amr = float(call.data)
        save_user(user)
        save_body(body)
        main_menu(call.message)



#------------------------------------------------   SQL ------------------------------------------------#
def save_user(user):
    url = url_api + 'user'
    json_data = json.dumps(user.__dict__)
    print(json_data)
    r = requests.post(url, headers=headers_dict, data=json_data)
    #response_json = r.json()
    user.password = r.json()['password']



def save_body(body):
    if (body.gender == 'MALE'):
        bmr = 88.4 + (13.4 * float(body.weight)) + (4.8 * float(body.height)) - (5.7 * float(body.age))
    if (body.gender == 'FEMALE'):
        bmr = 448 + (9.2 * float(body.weight)) + (3.1 * float(body.height)) - (4.3 * float(body.age))
    cal_rate = bmr * float(body.amr)
    float("{0:.1f}".format(bmr))
    body.bmr = bmr
    body.calRate = int(cal_rate)
    url = url_api + 'body'
    json_data = json.dumps(body.__dict__)
    print(json_data)
    r = requests.post(url, headers=headers_dict, data=json_data)
    response_json = r.json()


def parse_dishes(message):
    url = message.text
    html_doc = urlopen(url).read()
    soup = BeautifulSoup(html_doc, "html.parser")
    mess = ""
    while soup.find('span', "linked-content clearfix print-invisible"):
        span = soup.find('span', "linked-content clearfix print-invisible")
        span.decompose()
    for tag in soup.find_all('div', "instruction__wrap"):
        text = ("{0}".format(tag.text))
        mess += (' '.join(text.split())) + "\n"
    bot.send_message(message.from_user.id, mess)

def send_message():
    response = requests.get('http://localhost:8080/api/ration?idChat=%s' % id)
    if response.status_code == 200:
        data = response.json()
        bot.send_message(id, 'Меню на ' + data['date'] + ':')
        bot.send_message(id, 'Завтрак: ' + data['breakfast']['name'] + '\n' + \
                data['breakfast']['url'])
        bot.send_message(id, 'Обед: '+ data['lunch']['name'] + '\n' +\
                data['lunch']['url'])
        bot.send_message(id, 'Ужин: ' + data['dinner']['name'] + '\n' +\
                data['dinner']['url'])
    else:
        pass

def start_process():
    p = P_schedule()
    p1 = Process(target=p.start_schedule(), args=()).start()


class P_schedule():  # Class для работы с schedule
    def __init__(self):
        pass
    def start_schedule(self):  # Запуск schedule

        schedule.every().day.at("19:22").do(self.send_message1)


        while True:  # Запуск цикла
            schedule.run_pending()
            time.sleep(1)

    def send_message1(self):
        bot.send_message(id, 'Отправка сообщения по времени')

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        pass