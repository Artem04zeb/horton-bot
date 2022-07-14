import sqlite3
from sqlite3.dbapi2 import Cursor, complete_statement
from typing import Counter

from aiogram.types import message
import simple_funcs

uid = 0 #int
name = 'none' #str
classes = 'none' #str

# Подключение к БД
conn = sqlite3.connect("teachers.db")
cursor = conn.cursor()

# CREATE AND CONNECT TABLE
def start():
    # Создание таблицы, если она не создана
    cursor.execute( """CREATE TABLE IF NOT EXISTS teachers
                    (
                    uid INTEGER,
                    name TEXT,
                    subject TEXT,
                    classes TEXT
                    )"""
                    )

# ADD NEW TEACHER TO DB
def new_teacher(uid, name, subject, classes):
    #Функция получается на вход ID, имя учителя, предметы которые он может изменять и классы с котороми может работать

    cursor.execute(f"""INSERT INTO teachers VALUES({str(uid)}, '{str(name)}', '{str(subject)}', '{str(classes)}')""") #
    conn.commit()

# RETURN teachers
def get_teachers(): 
    if cursor.execute('SELECT * FROM teachers').fetchone() is None: 
        teachers2 = 'Список учителей пуст!'
    else:
        cursor.execute("SELECT uid, name FROM teachers")
        teachers1 = cursor.fetchall()
        teachers2 = 'Список учителей:\n'
        for i in range(len(teachers1)):
            teachers2+=(str(teachers1[i][1])) + ' '
            teachers2+=(str(teachers1[i][0])) + '\n'
    return(teachers2)

# RETURN UID's
def get_teacher_id():
    cursor.execute("SELECT uid FROM teachers")
    teachers1 = cursor.fetchall()
    teachers2 = []
    for i in range(len(teachers1)):
        teachers2.append(teachers1[i][0])
    return(teachers2)

def check_classes(message): # get_classes in last
    cursor.execute(f"SELECT classes FROM teachers WHERE uid = {message.from_user.id}")
    if (message.text in cursor.fetchall()[0][0]) or (message.from_user.id in [520365159, 1799501141]):
        simple_funcs.say_operation(message,'Доступ к классу разрешен')
        return(True)
    else: 
        simple_funcs.say_operation(message,'Доступ к классу запрещён')
        return(False)


def get_classes(uid):
    # выводит классы, которые может редактировать учитель
    cursor.execute(f"SELECT subject FROM teachers WHERE uid = {uid}")
    return(cursor.fetchall()[0][0])



