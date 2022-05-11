import sqlite3


class classroom_train():		
	def classroom_train_main(self):
		db = sqlite3.connect('db.sqlite3')
		sql = db.cursor()

		db_t = sqlite3.connect('base_teacher.db')
		sql_t = db_t.cursor()


		for value in sql.execute("SELECT classroom FROM mainapp_lesson_e"):
			if value[0]!='-':
				print(value[0])
				for clas in sql_t.execute("SELECT classroom FROM classroom"):
					if clas[0] == None:
						sql_t.execute(f"INSERT INTO classroom VALUES (?, ?, ?, ?)", (value[0], None, None, None))
						db_t.commit()
						