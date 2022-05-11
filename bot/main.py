import telebot
from telebot import types
import sqlite3
from time import sleep
import threading
import datetime
import configure
import send_mes

lock = threading.Lock()

# Подключение к БД (расписание, пользыватели)

global db
global sql
db = sqlite3.connect('../db.sqlite3', check_same_thread = False)
sql = db.cursor()

global db_user
global sql_user
db_user = sqlite3.connect('bd_user.db', check_same_thread = False)
sql_user = db_user.cursor()


bot = telebot.TeleBot(configure.config['token'])


@bot.message_handler(commands=['start'])
def com_start(message):
	#Регистрация
	sql_user.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
	if sql_user.fetchone() is None:
		bot.send_message(message.chat.id, 'Для початку роботи потрібно зареєструватися, Ви студент чи викладач?', reply_markup=configure.reg_kayboard)
		bot.register_next_step_handler(message, cheack_users)
	else:  # Ветка если человек зарегестирован
		bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}, чим можу допомогти?', reply_markup=configure.main_kayboard)


def cheack_users(message):
	if message.text == "Викладач":
		markup = types.InlineKeyboardMarkup(row_width=2)
		bot.send_message(message.chat.id, 'Введіть ваше ПІБ: (Наприклад: Коваленко Людмила Іванівна)')
		bot.register_next_step_handler(message, teacher)

	elif message.text == "Студент":
		markup = types.InlineKeyboardMarkup(row_width=2)
		# Создание пустого списка, добавление в него цыклом списка груп 
		group_all = []
		for value in db.execute("SELECT name FROM mainapp_name_group"):
			group_all.append(value[0])
		x = len(group_all)
		i = 0
		# Создание клавиатури из списка груп
		while i != len(group_all):  
			item = types.InlineKeyboardButton(group_all[i], callback_data="group_{0}".format(group_all[i]))  
			i = i + 1
			if i != len(group_all):
				item1 = types.InlineKeyboardButton(group_all[i], callback_data="group_{0}".format(group_all[i]))
				markup.add(item,item1)
				i = i + 1
			else:
				markup.add(item)
		bot.send_message(message.chat.id, 'Оберіть свою групу:', reply_markup = markup)

	else:
		bot.send_message(message.chat.id, "Оберіть пункт із меню.", reply_markup = configure.reg_kayboard)
		bot.register_next_step_handler(message, cheack_users)


def teacher(message):
	sql.execute(f"SELECT teacher FROM mainapp_lesson_e WHERE `teacher` LIKE '%{message.text}%'")
	teacher = sql.fetchone()
	if teacher != None:
		bot.send_message(message.chat.id, f'<b>{teacher[0]}</b> все вірно?', reply_markup=configure.end_reg, parse_mode="html")
		bot.register_next_step_handler(message, end_reg, teacher)
	else:
		bot.send_message(message.chat.id, f'Такого викладача не знайдено', reply_markup=configure.reg_kayboard)
		bot.register_next_step_handler(message, cheack_users)


def end_reg(message, teacher):
	if message.text == "Так":
		sql_user.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (message.from_user.id, message.from_user.first_name, teacher[0], '+'))
		db_user.commit()
		logi(message.from_user.first_name, teacher[0])
		bot.send_message(message.chat.id, "Реєстрація успішна!", reply_markup=configure.main_kayboard)
	elif message.text == "Ні":
		bot.send_message(message.chat.id, f'Спробуйте знову', reply_markup=configure.reg_kayboard)
		bot.register_next_step_handler(message, cheack_users)
	else:
		bot.send_message(message.chat.id, f'Оберіть пункт з меню!', reply_markup=configure.end_reg)
		bot.register_next_step_handler(message, end_reg, teacher)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	user = call.from_user.first_name
	chat_id = call.message.chat.id
	if "group" in call.data:
		id = call.data.split('_')[1]
		sql_user.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (chat_id, user, id, ''))
		db_user.commit()
		logi(user, id)
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ви обрали групу <b>{0}</b>".format(id),
																								parse_mode="HTML", reply_markup=None)                                                                                       
		bot.send_message(call.message.chat.id, "Реєстрація успішна!", reply_markup=configure.main_kayboard)
	

# Отправка расписания
@bot.message_handler(func=lambda mess: "\U0001F4D7Сьогодні" == mess.text, content_types=['text'])
def shedule(message):
	sql_user.execute(f"SELECT rol FROM users WHERE id = {message.from_user.id}")
	rol = sql_user.fetchone()[0]
	try:
		lock.acquire(True)
		sql_user.execute(f"SELECT groupa FROM users WHERE id = '{message.from_user.id}'")
		groupa = sql_user.fetchone()[0]

	finally:
		lock.release()
	
	d = datetime.datetime.today()
	date = str(d.day) + '.' + str(d.month) + '.' + str(d.year)
	bot.send_message(message.chat.id, send_mes.send(date, groupa, rol), parse_mode="HTML", reply_markup=configure.main_kayboard)


@bot.message_handler(func=lambda mess: "\U0001F4D8Завтра" == mess.text, content_types=['text'])
def shedule_tomorrow(message):
	sql_user.execute(f"SELECT rol FROM users WHERE id = {message.from_user.id}")
	rol = sql_user.fetchone()[0]

	try:
		lock.acquire(True)
		sql_user.execute(f"SELECT groupa FROM users WHERE id = '{message.from_user.id}'")
		groupa = sql_user.fetchone()[0]

	finally:
		lock.release()
	
	d = datetime.datetime.today()
	d = d + datetime.timedelta(days=1)
	date = str(d.day) + '.' + str(d.month) + '.' + str(d.year)
	bot.send_message(message.chat.id, send_mes.send(date, groupa, rol), parse_mode="HTML", reply_markup=configure.main_kayboard)


@bot.message_handler(func=lambda mess: "\U0001F465Інша група" == mess.text, content_types=['text'])
def shedule_other(message):
	bot.send_message(message.chat.id, "Введіть групу")
	bot.register_next_step_handler(message, shedule_date)


def shedule_date(message):
	group = message.text
	bot.send_message(message.chat.id, f"Введіть дату в форматі  1.1.2021")
	bot.register_next_step_handler(message, shedule_print, group)


def shedule_print(message, group):
	bot.send_message(message.chat.id, send_mes.send(message.text, group, ""), parse_mode="HTML", reply_markup=configure.main_kayboard)


# Кнопки Main Menu
@bot.message_handler(func=lambda mess: "Допомога" == mess.text, content_types=['text'])
def help(massage):
    bot.send_message(massage.from_user.id, configure.help, parse_mode="HTML" )


@bot.message_handler(func=lambda mess: "Контакти" == mess.text, content_types=['text'])
def contacts(message):
    bot.send_message(message.from_user.id, configure.contacts)
    bot.send_chat_action(message.from_user.id, 'find_location')
    bot.send_location(message.from_user.id, 50.909102, 34.787885)


@bot.message_handler(func=lambda mess: "Розклад дзвінків \U0001F552" == mess.text, content_types=['text'])
def clock(massage):
	bot.send_message(massage.from_user.id, configure.time, parse_mode="HTML")


@bot.message_handler(func=lambda mess: "Пошук аудиторії" == mess.text, content_types=['text'])
def find(message):
	bot.send_message(message.chat.id, "Введіть № аудиторії")
	bot.register_next_step_handler(message, find_send)
def find_send(message): 
	find = send_mes.Room()
	find.find_class(message.text)
	dist = find.room_url
	room = find.room_location 
	if dist == None and room == None :
		bot.send_message(message.chat.id, "Аудиторія не знайдена")
	else:
		bot.send_message(message.chat.id, room, reply_markup=configure.main_kayboard)
		img = open(dist, "rb")
		bot.send_photo(message.chat.id, img, reply_markup=configure.main_kayboard)


#удаление аккаунта
@bot.message_handler(commands=['delete'])
def com_delete(message):
	sql_user.execute(f"DELETE FROM users WHERE id = '{message.from_user.id}'")
	db_user.commit()
	bot.send_message(message.chat.id, 'Вас немає в базі даних, потрібно пройти реєстрацію!', reply_markup=configure.reg_kayboard)
	bot.register_next_step_handler(message, com_start)


@bot.message_handler(commands=['find'])
def find(message):
	bot.send_message(message.chat.id, "Введіть викладача або групу:")
	bot.register_next_step_handler(message, find_step)
def find_step(message):
	d = datetime.datetime.now()
	date = str(d.day) + '.' + str(d.month) + '.' + str(d.year)
	str(date)
	time = d.strftime("%H:%M")
	bot.send_message(message.chat.id, send_mes.find_group(message.text, date, time), reply_markup=configure.main_kayboard)


def logi(user_name, user_group):
	d = datetime.datetime.now()
	str(d)
	d = d.strftime("%d-%m-%Y %H:%M:%S")
	print(f'[{d}]: Зареєструвався новий користувач: {user_name}; Група\викладач: {user_group}')
	

def main():
	print("--------------------Telegram Bot v.0.1--------------------")
	bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
