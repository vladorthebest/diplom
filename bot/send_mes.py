import sqlite3
import threading

lock = threading.Lock()

db = sqlite3.connect('../db.sqlite3', check_same_thread = False)
sql = db.cursor()


def send(date, group, rol):

    schedule = f"<b>Ваш розклад {date}:</b> \n"

    if rol != "":
        number = 1
        while number != 6:
            for value in sql.execute(f"SELECT * FROM mainapp_lesson WHERE `teacher` LIKE '%{group}%' AND `data` LIKE '%{date}%' AND `number` LIKE '%{number}%'"):
                schedule = schedule + str(value[3]) + '. ' + str(value[4]) + '\n    Група\U0001F465 ' + str(value[2]) + '\n    Кабінет \U0001F6AA - '+ str(value[8]) + '\n'
            number = number + 1

    else:
        number = 1
        while number != 6:
            for value in sql.execute(f"SELECT * FROM mainapp_lesson WHERE (`group` LIKE '%{group}%' OR `teacher` LIKE '%{group}%' ) AND `data` LIKE '%{date}%' AND `number` LIKE '%{number}%'"):
                schedule = schedule + str(value[3]) + '. ' + str(value[4]) + '\n    Кабінет \U0001F6AA - '+ str(value[8]) + '\n    Викладач \U0001F464 ' + str(value[5]) + '\n \n'
            number = number + 1
    if schedule == f"<b>Ваш розклад {date}:</b> \n":
            schedule = f"На {date} пар не знайдено"
    return schedule


def find_group(group, date, time):

    if time >= "08:29" and time <= "09:50":
        sql.execute(f"SELECT * FROM mainapp_lesson WHERE (`group` LIKE '%{group}%' OR `teacher` LIKE '%{group}%' ) AND `data` LIKE '%{date}%' AND `number` LIKE '%1%'")
        test = sql.fetchone()
        find = str(test[3])+". " + str(test[4])+'\n   Кабінет \U0001F6AA - ' + str(test[8]) +'\n   Викладач \U0001F464 '+ str(test[5])

    elif time >= "09:50" and time <= "11:20":
        sql.execute(f"SELECT * FROM mainapp_lesson WHERE (`group` LIKE '%{group}%' OR `teacher` LIKE '%{group}%' ) AND `data` LIKE '%{date}%' AND `number` LIKE '%2%'")
        test = sql.fetchone()
        find = str(test[3])+". " + str(test[4])+'\n   Кабінет \U0001F6AA - ' + str(test[8]) +'\n   Викладач \U0001F464 '+ str(test[5])

    elif time >= "11:20" and time <= "13:30":
        sql.execute(f"SELECT * FROM mainapp_lesson WHERE (`group` LIKE '%{group}%' OR `teacher` LIKE '%{group}%' ) AND `data` LIKE '%{date}%' AND `number` LIKE '%3%'")
        test = sql.fetchone()    
        find = str(test[3])+". " + str(test[4])+'\n   Кабінет \U0001F6AA - ' + str(test[8]) +'\n   Викладач \U0001F464 '+ str(test[5])

    elif time >= "13:30" and time <= "15:00":
        sql.execute(f"SELECT * FROM mainapp_lesson WHERE (`group` LIKE '%{group}%' OR `teacher` LIKE '%{group}%' ) AND `data` LIKE '%{date}%' AND `number` LIKE '%4%'")
        test = sql.fetchone()
        find = str(test[3])+". " + str(test[4])+'\n   Кабінет \U0001F6AA - ' + str(test[8]) +'\n   Викладач \U0001F464 '+ str(test[5])

    elif time >= "15:00" and time <= "16:30":
        sql.execute(f"SELECT * FROM mainapp_lesson WHERE (`group` LIKE '%{group}%' OR `teacher` LIKE '%{group}%' ) AND `data` LIKE '%{date}%' AND `number` LIKE '%5%'")
        test = sql.fetchone()
        find = str(test[3])+". " + str(test[4])+'\n   Кабінет \U0001F6AA - ' + str(test[8]) +'\n   Викладач \U0001F464 '+ str(test[5])
    
    elif time > "16:30":    
        find = "Робочій день закінчився"
    else:
        find = "Вікно"

    if find == None:
    	find = "Групу\викдача не знайдено."
    return find


class Room():
    def find_class(self, message):
        class_list = {
            # 1 этаж Глав корпус
            "5": ["img/class_room/5.png", "Головний корпус 1 поверх."],
            "6": ["img/class_room/6.png", "Головний корпус 1 поверх."],
            "7": ["img/class_room/7.png", "Головний корпус 1 поверх."],
            "8": ["img/class_room/8.png", "Головний корпус 1 поверх."],
            # 2 этаж Глав корпус
            "12": ["img/class_room/12.png", "Головний корпус 2 поверх."],
            "13": ["img/class_room/13.png", "Головний корпус 2 поверх."],
            "14": ["img/class_room/14.png", "Головний корпус 2 поверх."],
            "15": ["img/class_room/15.png", "Головний корпус 2 поверх."],
            "16": ["img/class_room/16.png", "Головний корпус 2 поверх."],
            # 3 этаж Глав корпус
            "20": ["img/class_room/20.png", "Головний корпус 3 поверх."],
            "21": ["img/class_room/21.png", "Головний корпус 3 поверх."],
            "22": ["img/class_room/22.png", "Головний корпус 3 поверх."],
            "23": ["img/class_room/23.png", "Головний корпус 3 поверх."],
            "24": ["img/class_room/24.png", "Головний корпус 3 поверх."],
            "25": ["img/class_room/25.png", "Головний корпус 3 поверх."],
            # 1 этаж Лаб корпус
            "30": ["img/class_room/30.png", "Лабораторний корпус 1 поверх."],
            "31А": ["img/class_room/31а.png", "Лабораторний корпус 1 поверх."],
            "32": ["img/class_room/32.png", "Лабораторний корпус 1 поверх."],
            "33": ["img/class_room/33.png", "Лабораторний корпус 1 поверх."],
            "34": ["img/class_room/34.png", "Лабораторний корпус 1 поверх."],
            "35": ["img/class_room/35.png", "Лабораторний корпус 1 поверх."],
            "36": ["img/class_room/36.png", "Лабораторний корпус 1 поверх."],
            "37": ["img/class_room/37.png", "Лабораторний корпус 1 поверх."],
            "37А": ["img/class_room/37а.png", "Лабораторний корпус 1 поверх."],
            # 2 этаж Лаб корпус
            "41": ["img/class_room/41.png", "Лабораторний корпус 2 поверх."],
            "41А": ["img/class_room/41а.png", "Лабораторний корпус 2 поверх."],
            "42": ["img/class_room/42.png", "Лабораторний корпус 2 поверх."],
            "43": ["img/class_room/43.png", "Лабораторний корпус 2 поверх."],
            "44": ["img/class_room/44.png", "Лабораторний корпус 2 поверх."],
            "44А": ["img/class_room/44а.png", "Лабораторний корпус 2 поверх."],
            "47": ["img/class_room/47.png", "Лабораторний корпус 2 поверх."],
            "49": ["img/class_room/49.png", "Лабораторний корпус 2 поверх."],
            "49А": ["img/class_room/49а.png", "Лабораторний корпус 2 поверх."],
            "51": ["img/class_room/51.png", "Лабораторний корпус 2 поверх."],
            "51А": ["img/class_room/51А.png", "Лабораторний корпус 2 поверх."],
            "53": ["img/class_room/53.png", "Лабораторний корпус 2 поверх."],
            "55": ["img/class_room/55.png", "Лабораторний корпус 2 поверх."]
        }
        try:
            self.room_url = class_list[message][0]
            self.room_location = class_list[message][1]
        except KeyError:
            self.room_url = None
            self.room_location = None
        


