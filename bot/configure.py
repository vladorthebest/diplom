import telebot

config = {
	'name' : 'stppbot',
	'token' : '622233587:AAG6fg0yuZ7Zr4kj1E7yCEJcqxIogI1L_sk'
}
# MAIN Kayboard
main_kayboard = telebot.types.ReplyKeyboardMarkup(True, False)
main_kayboard.row('\U0001F4D7Сьогодні', '\U0001F4D8Завтра', '\U0001F465Інша група')
main_kayboard.row('Розклад дзвінків \U0001F552')
main_kayboard.row('Допомога', 'Контакти')
main_kayboard.row('Пошук аудиторії')

# REG Kayboard
reg_kayboard = telebot.types.ReplyKeyboardMarkup(True, True)
reg_kayboard.row('Студент', 'Викладач')

# END REG
end_reg = telebot.types.ReplyKeyboardMarkup(True, False)
end_reg.row('Так', 'Ні')


# Time 
time = '''
		\n<b>Звичайний день</b> \n
		\u0031\u20E3 пара 08:30 - 09:50
		\u0032\u20E3 пара 10:00 - 11:20
		\u0033\u20E3 пара 12:10 - 13:30
		\u0034\u20E3 пара 13:40 - 15:00
		\u0035\u20E3 пара 15:10 - 16:30\n
		<b>Скорочений день (по 1 часу)</b> \n
		\u0031\u20E3 пара 08:30 - 09:30
		\u0032\u20E3 пара 09:40 - 10:40
		\u0033\u20E3 пара 10:50 - 11:50
		\u0034\u20E3 пара 12:00 - 13:00 '''
		
help = '''
Головне меню /start 
Видалення акаунту  /delete 
Пошук групи\викладача /find 
Розробники:
<a href="tg://user?id=538771062">Михайло</a>
<a href="tg://user?id=650020538">Владислав</a>'''

contacts = '''Юридична адреса коледжу: вулиця Ярослава Мудрого, 60, Суми, Сумська область, 40000.
Телефон 61-04-35, факс 61-05-23, ідентифікаційний код 26440067.

<a href="https://www.google.com/maps/place/@50.9086079,34.7872783,20.5z/">Ми на карті</a>'''