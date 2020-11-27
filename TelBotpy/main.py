import telebot
from telebot import types
from bs4 import BeautifulSoup
from urllib.request import urlopen
import psycopg2
from validate_email import validate_email

conn = psycopg2.connect(database="postgres",
  user="postgres",
  password="7530159",
  host="127.0.0.1",
  port="5432"
)
cursor = conn.cursor()

bot = telebot.TeleBot('1250487291:AAEd2xynjPPTYXRoaZd0SBlY540wqdt1y4w')
user_dict = {}


class User:
    def __init__(self,chat_id):
        self.chat_id = chat_id
        self.name = None
        self.mail = None
        self.age = None
        self.sex = None
        self.weight = None
        self.height = None
        self.purpose = None
        self.purpose = None
        self.amr = None


@bot.message_handler(commands=['start'])
def start_message(message):
    user = User(message.chat.id)
    user_dict[message.chat.id] = user
    bot.send_message(message.chat.id, 'Привет, для начала познакомимся!')
    ask_name(message.from_user.first_name,message) #-----  call getting NAME



#------------------------------------------------   GET THE NAME    ------------------------------------------------#

def ask_name(get_name,message):
    user = user_dict[message.chat.id]
    user.name = get_name
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = "Это твое имя?\n" + user.name
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


def get_name(message):
    user = user_dict[message.chat.id]
    user.name = message.text
    ask_name(user.name, message)

#------------------------------------------------   GETTING EMAIL   ------------------------------------------------#

def get_mail(message):
    user = user_dict[message.chat.id]
    user.mail = message.text
    if not validate_email(user.mail):
        msg = bot.reply_to(message, 'Эл.почта не верна. Ввведите повторно:')
        bot.register_next_step_handler(msg, get_mail)
        return
    ask_age(message)  #-----  call getting AGE


#------------------------------------------------   GET AGE    ------------------------------------------------#

def ask_age(message):
    bot.send_message(message.chat.id,'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    user = user_dict[message.chat.id]
    user.age = message.text
    if not user.age.isdigit():
        msg = bot.reply_to(message, 'Возвраст должен быть числом. Сколько тебе лет?')
        bot.register_next_step_handler(msg, get_age)
        return
    keyboard = types.InlineKeyboardMarkup()
    key_MALE = types.InlineKeyboardButton(text='Мужчина', callback_data='MALE')
    keyboard.add(key_MALE)
    key_FEMALE = types.InlineKeyboardButton(text='Женщина', callback_data='FEMALE')
    keyboard.add(key_FEMALE)
    bot.send_message(message.from_user.id, text="Твой пол?", reply_markup=keyboard)

#------------------------------------------------   GET WEIGHT    ------------------------------------------------#

def get_weight(message):
    user = user_dict[message.chat.id]
    user.weight = message.text
    try:
        user.weight = float(user.weight)
    except:
        bot.reply_to(message, 'Вес должен быть числом. Ваш вес?')
        bot.register_next_step_handler(message, get_weight)
        return
    bot.send_message(message.chat.id, 'Ваш рост??')
    bot.register_next_step_handler(message, get_height)

#------------------------------------------------   GET HEIGHT    ------------------------------------------------#

def get_height(message):
    user = user_dict[message.chat.id]
    user.height = message.text
    try:
        user.height = float(user.height)
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
    user = user_dict[call.message.chat.id]
    if (call.data == 'slim'):
        user.purpose = 0
    if (call.data == 'gain'):
        user.purpose = 1
    if (call.data == 'save'):
        user.purpose = 2
    keyboard = types.InlineKeyboardMarkup()
    key_normal = types.InlineKeyboardButton(text='Обычная', callback_data='normal')
    keyboard.add(key_normal)
    key_vegan = types.InlineKeyboardButton(text='Веган', callback_data='vegan')
    keyboard.add(key_vegan)
    key_diabet = types.InlineKeyboardButton(text='Диабет', callback_data='diabet')
    keyboard.add(key_diabet)
    bot.send_message(call.message.chat.id, text="Ваша диета?", reply_markup=keyboard)



#------------------------------------------------   GET DIET    ------------------------------------------------#

def get_diet(call):
    user = user_dict[call.message.chat.id]
    user.diet = call.data
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


#------------------------------------------------   KEYBOARD UNDER MESSAGE    ------------------------------------------------#

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    user = user_dict[call.message.chat.id]
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
        bot.send_message(call.message.chat.id, 'Ввведите свою почту')
        bot.register_next_step_handler(call.message, get_mail)  #----- call to get mail
    if call.data == "no":
        bot.send_message(call.message.chat.id, "Как тебя зовут?")
        bot.register_next_step_handler(call.message, get_name)
    if call.data == "FEMALE" or call.data == "MALE":
        user.sex = call.data
        bot.send_message(call.message.chat.id, 'Сколько вы весите?')
        bot.register_next_step_handler(call.message, get_weight)  #----- call to get weight
    if call.data == "slim" or call.data == "gain" or call.data == "save":
        get_purpose(call) #----- call to get purpose
    if call.data == "normal" or call.data == "vegan" or call.data == "diabet":
        get_diet(call)
    if call.data == "1.2" or call.data == "1.375" or call.data == "1.55" or call.data == "1.725" or call.data == "1.9":
        user.amr = call.data
        save_user(user)
        save_body(user)
        save_character(user)


#------------------------------------------------   SQL ------------------------------------------------#
def save_user(user):
    # try:
    #     postgres_insert_query = """ INSERT INTO users (id_chat, name, mail) VALUES (%s,%s,%s)"""
    #     record_to_insert = (user.chat_id, user.name, user.mail)
    #     cursor.execute(postgres_insert_query, record_to_insert)
    #     conn.commit()
    # except (Exception, psycopg2.Error) as error:
    #     print("Error in update operation", error)
    #     bot.send_message(user.chat_id, 'Произошла ошибка, попробуйте пройти опрос заново /start')
    # finally:
    #     if (conn):
    #         cursor.close()
    print(user.chat_id, user.name, user.mail)


def save_body(user):
    # try:
    #     postgres_insert_query = """ INSERT INTO body (id_chat, weight, height, age, sex) VALUES (%s,%s,%s,%s,%s)"""
    #     record_to_insert = (user.chat_id, user.weight, user.height, user.age, user.sex)
    #     cursor.execute(postgres_insert_query, record_to_insert)
    #     conn.commit()
    # except (Exception, psycopg2.Error) as error:
    #     print("Error in update operation", error)
    #     bot.send_message(user.chat_id, 'Произошла ошибка, попробуйте пройти опрос заново /start')
    # finally:
    #     if (conn):
    #         cursor.close()
    print(user.chat_id, user.weight, user.height, user.age, user.sex)

def save_character(user):
    if (user.sex == 'MALE'):
        BMR = 88.4 + (13.4 * float(user.weight)) + (4.8 * float(user.height)) - (5.7 * float(user.age))
    if (user.sex == 'FEMALE'):
        BMR = 448 + (9.2 * float(user.weight)) + (3.1 * float(user.height)) - (4.3 * float(user.age))
    cal_rate = BMR * float(user.amr)
    float("{0:.1f}".format(BMR))
    cal_rate = int(cal_rate)
    # try:
    #     postgres_insert_query = """ INSERT INTO character (id_chat, BMR, AMR, cal_rate, purpose, diet) VALUES (%s,%s,%s,%s,%s,%s)"""
    #     record_to_insert = (user.chat_id, BMR, user.amr, cal_rate, user.purpose, user.diet)
    #     cursor.execute(postgres_insert_query, record_to_insert)
    #     conn.commit()
    # except (Exception, psycopg2.Error) as error:
    #     print("Error in update operation", error)
    #     bot.send_message(user.chat_id, 'Произошла ошибка, попробуйте пройти опрос заново /start')
    # finally:
    #     if (conn):
    #         cursor.close()
    print(user.chat_id, BMR, user.amr, cal_rate, user.purpose, user.diet)

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















def print_hi(name):
    print(name)


if __name__ == '__main__':
    print_hi('BotStart')


bot.polling()