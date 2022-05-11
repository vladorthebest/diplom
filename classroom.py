import sqlite3
import datetime

class classroom():		
	def classroom_main(self):
		db = sqlite3.connect('base_teacher.db')
		sql = db.cursor()
		db_l = sqlite3.connect('db.sqlite3')
		sql_l = db_l.cursor()
		db_l1 = sqlite3.connect('db.sqlite3')
		sql_l1 = db_l.cursor()

		d1 = datetime.datetime.today()
		d1 = d1 + datetime.timedelta(days=1)
		day = str(d1.isoweekday())
		if day == '6':
			d1 = d1 + datetime.timedelta(days=2)
		if day == '7':
			d1 = d1 + datetime.timedelta(days=1)
		print(day)
		date = str(d1.day) + '.' + str(d1.month) + '.' + str(d1.year)
		print(date)

		
		for lesson in sql_l.execute(f"SELECT * FROM mainapp_lesson WHERE data = '{date}' and classroom = '-'"):
				#print(lesson)
			for value in sql_l1.execute(f'SELECT * FROM mainapp_lesson_e WHERE number = "{lesson[3]}" and lesson = "{lesson[4]}" and day =  "{lesson[6]}" and teacher = "{lesson[5]}"'):
				#print('1')
				if value[7] != '-':
					sql.execute(f"SELECT lesson FROM classroom_db WHERE classroom = '{value[7]}' and paran = '{value[3]}'")
					clas = sql.fetchone()
					if clas == None:
						#print(value[7])
						sql.execute(f"INSERT INTO classroom_db VALUES (?, ?, ?)", (value[7], lesson[0], value[3]))
						db.commit()
						
					#else:
						#print('zan')

		for lesson in sql.execute(f"SELECT * FROM classroom_db"):
			sql_l.execute(f'UPDATE mainapp_lesson SET classroom = "{lesson[0]}" WHERE id = "{lesson[1]}"')		
			db_l.commit()

		for lesson in sql_l.execute(f"SELECT * FROM mainapp_lesson WHERE data = '{date}' and classroom = '-'"):	
			#print(lesson)			
			for value in sql_l1.execute(f'SELECT * FROM mainapp_lesson_e WHERE lesson = "{lesson[4]}" and teacher = "{lesson[5]}"'):
				#print('2')
				if value[7] != '-':
					sql.execute(f"SELECT lesson FROM classroom_db WHERE classroom = '{value[7]}' and paran = '{value[3]}'")
					clas = sql.fetchone()
					if clas == None:
						print(value[7])
						sql.execute(f"INSERT INTO classroom_db VALUES (?, ?, ?)", (value[7], lesson[0], value[3]))
						db.commit()
					#else:
						#print('zan')

		for lesson in sql.execute(f"SELECT * FROM classroom_db"):
			sql_l.execute(f'UPDATE mainapp_lesson SET classroom = "{lesson[0]}" WHERE id = "{lesson[1]}"')		
			db_l.commit()

		for lesson in sql_l.execute(f"SELECT * FROM mainapp_lesson WHERE data = '{date}' and classroom = '-'"):				
			teacher1 =lesson[5]
			for value in sql.execute(f'SELECT id FROM teachers WHERE teacher = "{teacher1}"'):
				#print(3)
				sql.execute(f"SELECT classroom FROM classroom WHERE id = '{value[0]}'")
				cla = sql.fetchone()
					#print(cla)
				sql.execute(f"SELECT lesson FROM classroom_db WHERE classroom = '{cla[0]}' and paran = '{str(lesson[3])}'")
				clas = sql.fetchone()
								#print(clas)
				if clas == None:
						#print(cla[0])
					sql.execute(f"INSERT INTO classroom_db VALUES (?, ?, ?)", (cla[0], lesson[0], lesson[3]))
					db.commit()
		

		for lesson in sql.execute(f"SELECT * FROM classroom_db"):
			sql_l.execute(f'UPDATE mainapp_lesson SET classroom = "{lesson[0]}" WHERE id = "{lesson[1]}"')		
			db_l.commit()
		
			
		
	def classroom_train_main(self):
		db = sqlite3.connect('db.sqlite3')
		sql = db.cursor()

		db_t = sqlite3.connect('base_teacher.db')
		sql_t = db_t.cursor()


		for value in sql.execute("SELECT * FROM mainapp_lesson_e"):
			if value[7]!='-':
				#print(value[0])
				sql_t.execute(f"SELECT classroom FROM classroom WHERE classroom = {value[7]}")
				clas = sql_t.fetchone()
				#print (clas[0])
				if clas == None:
					sql_t.execute(f"INSERT INTO classroom VALUES (?, ?, ?, ?)", (value[7], None, None, None))
					db_t.commit()
					#print(value[0])
				sql_t.execute(f"SELECT id FROM classroom WHERE classroom = {value[7]}")
				clas = sql_t.fetchone()
				sql_t.execute(f'SELECT teacher FROM teachers WHERE teacher="{value[5]}" and id ="{clas[0]}"')
				clast = sql_t.fetchone()
				print (clast)

				if clast == None:
					sql_t.execute(f"INSERT INTO teachers VALUES (?, ?)", (value[5], clas[0]))
					db_t.commit()

		
t = classroom()
t.classroom_train_main()
t.classroom_main()		

		




