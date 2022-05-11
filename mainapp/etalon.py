import requests
import sqlite3
import datetime
import time

class etalon():
	def main(self):
		
		db = sqlite3.connect('db.sqlite3')
		sql = db.cursor()
		query = 'https://data.stpp.sumy.ua/rozklad/group.php'
		response = requests.get(query)
		global gr
		global gr_url
		gr = response.json()
		gr1 = list(gr.items())	
		gr_url = []
		gr = []
		delete_table = 'DELETE FROM mainapp_name_group'
		sql.execute(delete_table)
		db.commit()
		for i in range(len(gr1)):
			gr_url.append (gr1[i][0])
			gr.append (gr1[i][1])
			sql.execute(f"INSERT INTO mainapp_name_group VALUES (?, ?, ?)", (None, gr1[i][1], gr1[i][0]))
			db.commit()
		

		delete_table = 'DELETE FROM mainapp_lesson_e'
		sql.execute(delete_table)
		db.commit()
		for value in sql.execute("SELECT * FROM mainapp_lesson_e"):
			print (value)
		

		ti = 1
		d1 = datetime.datetime.today()
		while ti <8:
			d1 = d1 + datetime.timedelta(days=1)
			date = str(d1.day) + '.' + str(d1.month) + '.' + str(d1.year)
			day = d1.isoweekday()
			print(date)

			for i in range(len(gr)):	
				query = f'https://data.stpp.sumy.ua/rozklad/json_replacement.php?groupId={gr_url[i]}&date={date}&subgroup=1'
				#query = f'https://data.stpp.sumy.ua/rozklad/json_replacement.php?group={gr_url[i]}&date={date}&subgroup=1'
				response = requests.get(query)
				raspis = response.json()
				#print(raspis[0])
				
				group_norm = str(gr[i])
				print(group_norm)

				npara = 0
				while npara<5:
					#print(raspis[npara]['less'])
					if raspis[npara]['less'] != 'Немає':
						prepod = raspis[npara]['teach']
						item = prepod.find(',\n')
						if 	item != -1:
							prepod1 = prepod.split(',\n')[0]
							prepod2 = prepod.split(',\n')[1]
							sql.execute(f"INSERT INTO mainapp_lesson_e VALUES (?, ?, ?, ?, ?,?, ?, ?)", (None, date, group_norm, npara+1, raspis[npara]['less'], prepod1, day, '-'))
							db.commit()
							
							sql.execute(f"INSERT INTO mainapp_lesson_e VALUES (?, ?, ?, ?, ?,?, ?, ?)", (None, date, group_norm, npara+1, raspis[npara]['less'], prepod2, day, '-'))
							db.commit()
							
						else:
							prepod1 = prepod
							sql.execute(f"INSERT INTO mainapp_lesson_e VALUES (?, ?, ?, ?, ?,?, ?, ?)", (None, date, group_norm, npara+1, raspis[npara]['less'], prepod1, day, '-'))
							db.commit()
							
					npara = npara+1


				query = f'https://data.stpp.sumy.ua/rozklad/json_replacement.php?group={gr_url[i]}&date={date}&subgroup=2'
				response = requests.get(query)
				raspis = response.json()
				npara = 0
				while npara<5:
					if raspis[npara]['less'] != 'Немає':
						if raspis[npara]['repl'] == '1':
							prepod = raspis[npara]['teach']
							item = prepod.find(',\n')
							if 	item != -1:
								prepod1 = prepod.split(',\n')[0]
								prepod2 = prepod.split(',\n')[1]
								sql.execute(f"INSERT INTO mainapp_lesson_e VALUES (?, ?, ?, ?, ?,?, ?, ?)", (None, date, group_norm, npara+1, raspis[npara]['less'], prepod1, day, '-'))
								db.commit()
								
								sql.execute(f"INSERT INTO mainapp_lesson_e VALUES (?, ?, ?, ?, ?,?, ?, ?)", (None, date, group_norm, npara+1, raspis[npara]['less'], prepod2, day, '-'))
								db.commit()
								
							else:
								prepod1 = prepod
								sql.execute(f"INSERT INTO mainapp_lesson_e VALUES (?, ?, ?, ?, ?,?, ?, ?)", (None, date, group_norm, npara+1, raspis[npara]['less'], prepod1, day, '-'))
								db.commit()
								
					npara = npara+1
			ti=ti+1

		db = sqlite3.connect('db.sqlite3')
		sql = db.cursor()

		for value in sql.execute("SELECT * FROM mainapp_lesson_e"):
			print (value)


		
			

