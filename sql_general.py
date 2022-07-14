#from _typeshed import StrOrBytesPath

import sqlite3
from sqlite3.dbapi2 import Cursor, complete_statement
from typing import Counter

#Импорт модулей
import classes
import subjects 
import sql_teach

"""
Этот файл для работы с баззой данных. Привязан к классу 11Б или же 'cl11'.
"""

# Подключение к БД
conn = sqlite3.connect("classes_HW.db")
cursor = conn.cursor()

# Этот массив используется для создания колонок таблицы с домашним заданием. 
# Массив содержит названия предметов на английском языке.
list_of_subjects = ['economy', 
                    'english_grop_1',
                    'english_grop_2', 
                    'biology',
                    'math',
                    'physics',
                    'geography',
                    'o_bj',
                    'chemistry',
                    'history',
                    'russian',
                    'social',
                    '_PE',
                    'inf']

def start():
    # Функция создаёт таблицу, если она не существует, заполняет её дефолтными значениями.
    if cursor.execute("""SELECT count(*) FROM sqlite_master WHERE type='table' AND name='cl11';""").fetchall()[0][0] != 1:
        # Процесс создания строки для sql запроса 
        str_list_of_subject = ''
        for sub in list_of_subjects:
            if sub == list_of_subjects[-1]: str_list_of_subject+=sub
            else:  str_list_of_subject+=sub+','

        cursor.execute("""CREATE TABLE IF NOT EXISTS cl11
                    (id INTEGER, """+str_list_of_subject+""")""")

        insert_default() 


def insert_default():
    # Process of inserting defaults parameters in every day
    # Процесс вставки дефолтной домашки в каждый день в каждый урок
    for i in range(1,4):
        cursor.execute("""INSERT INTO cl11 VALUES("""+str(i)+""",'def', 
            'def', 
            'def',
            'def',
            'def',
            'def',
            'def',
            'def',
            'def',
            'def',
            'def',
            'def',
            'def',
            'def')""")
        conn.commit()

def new_HW(lesson, home_work):
    start()
    subject = subjects.subjects[lesson]

    # Get home work from real day
    # Получение домашней работы с настоящего дня
    cursor.execute("SELECT "+subject+" FROM cl11 WHERE id=1")
    real_result = cursor.fetchone()
    #print(real_result[0])

    #Get home work from last day
    # Получение ДЗ с прошлого дня
    cursor.execute("SELECT "+subject+" FROM cl11 WHERE id=2")
    last_result = cursor.fetchone()
    #print(last_result[0])

    # UPDATING
    # Обновление
    # Update current home work
    # Обновление текущего ДЗ
    cursor.execute("""UPDATE cl11 SET """+subject+""" = '"""+home_work+"""' WHERE id = 1;""")
    # Update last home work
    # Обновление прошлого ДЗ
    cursor.execute("""UPDATE cl11 SET """+subject+""" = '"""+real_result[0]+"""' WHERE id = 2;""")
    # Update last before home work
    # Обновление позапрошлого ДЗ 
    cursor.execute("""UPDATE cl11 SET """+subject+""" = '"""+last_result[0]+"""' WHERE id = 3;""")
    conn.commit()

def show_act_HW(cl_name):
    start()
    # Показывает ДЗ для выбранного дня
    # Show home work for choosed day 
    cl_id = classes.classes[cl_name]

    cursor.execute(f"SELECT * FROM {cl_id} WHERE id=1")

    subjects = cursor.fetchall()
    subjects = subjects[0][1:]


    # Урок и его ДЗ
    home_work = [] 

    # Все уроки с их ДЗ
    lesson = () 

    # Процесс заполнения 
    for i in range(len(subjects)):
        lesson = (list_of_subjects[i], subjects[i])
        home_work.append(lesson)

    # Процесс формирования строки для вывода в чат
    stroka = ''
    for element in home_work:
        stroka += element[0] + ': '
        stroka += element[1] + '\n'
    return stroka # Возвращает строку значений базы данных

def show_all_HW(cl_name):
    start()
    # Показывает ДЗ для выбранного дня
    # Show home work for choosed day 
    cl_id = classes.classes[cl_name]
    
    cursor.execute(f"SELECT * FROM {cl_id} WHERE id IN (1,2,3)")
    home_work = cursor.fetchall()

    lessons = list_of_subjects
    
    big_str = ''
    for i in range(3):
        big_str += 'День ' + str(i+1) +'\n'
        for j in range(len(list_of_subjects)):
            big_str += list_of_subjects[j] + ': ' + home_work[i][j+1] +'\n'
        big_str += '\n'
    
    return(big_str)

def correct_HW(lesson,home_work):
    start()
    subject = subjects.subjects[lesson]

    # Update current home work
    # Обновление только текущей домашней работы
    cursor.execute("""UPDATE cl11 SET """+subject+""" = '"""+home_work+"""' WHERE id = 1;""")
    conn.commit()

def get_personal_hw(id, cl_name):
    start()

    cl_id = classes.classes[cl_name]

    lessons = ''
    for element in sql_teach.get_classes(520365159).split(' '):
        lessons += subjects.subjects[element] + ', '
    
    cursor.execute(f"SELECT {lessons[0:-2]} FROM {cl_id} WHERE id=1")
    home_work = cursor.fetchall()
    home_work = home_work[0]
    return(home_work)
