from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from handlers import values


bttn_come_back = 'Главное меню'
bttn_a = 'Администратор'
bttn_back = '⬇' 

'''Main Menu'''
bttn_s = 'Ученик'    
bttn_t = 'Учитель'   
main_Menu = ReplyKeyboardMarkup(resize_keyboard=True).add(bttn_s, bttn_t, bttn_a)

'''Student Menu'''
bttn_act_hw = 'Актуальное дз'
bttn_all_hw = 'Все дз'
student_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2).add(bttn_act_hw, bttn_all_hw, bttn_back)

'''Teacher Menu'''
what_hw = 'Добавить дз'
change_hw = 'Изменить дз'
teacher_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2).add(change_hw, what_hw, bttn_back)

teacher_subject = ReplyKeyboardMarkup(resize_keyboard= True, row_width= 1).add(bttn_back)

def clean_1():
    return ReplyKeyboardMarkup(resize_keyboard= True, row_width= 1).add(bttn_back)


def subject_menu(les):
    for i in values.all_lessons:
        if i in les:
            teacher_subject.add(i)

'''Class Menu'''
bttn_11B = '11Б'
class_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(bttn_11B, bttn_back)

'''Register'''
bttn_register = 'Регистрация'
regist_menu = ReplyKeyboardMarkup(resize_keyboard= True).add(bttn_register, bttn_back)

'''Admin Menu'''
# Главное меню

bttn_a_app = 'Заявки'
bttn_teach_list = 'Список учителей'

# Меню выбора действия

bttn_accept = 'Принять'
bttn_reject = 'Отклонить'
bttn_cancle = 'Отмена'

# Функция для создания кнопок в зависимости от количества заявок

number_menu = ReplyKeyboardMarkup(resize_keyboard= True).add(bttn_cancle)
def next_n_menu(number):
    global number_menu
    number_menu.add(number)

# Функция для очищения меню с кнопками(потому что, если этого не делать, то кнопки будут увеличичваться с каждым разом)

def clean():
    return ReplyKeyboardMarkup(resize_keyboard= True).add(bttn_cancle)

# меню изменения списка учителей

bttn_change_tch = 'Изменить'
bttn_delete_tch = 'Удалить'

# меню классов

bttn_next = 'Далее'


admin_act_menu = ReplyKeyboardMarkup(resize_keyboard= True, row_width= 2).add(bttn_a_app, bttn_teach_list, bttn_back)# главное меню админа
a_chosea_menu = ReplyKeyboardMarkup(resize_keyboard= True).add(bttn_accept, bttn_reject, bttn_back) # меню принятия заявки или нет
teach_look_menu = ReplyKeyboardMarkup(resize_keyboard= True).add(bttn_change_tch, bttn_back) # меню изменения списка учителей
delite_or_not = ReplyKeyboardMarkup(resize_keyboard= True).add(bttn_delete_tch, bttn_back) # меню удаления учителя из списка
lessons_menu = ReplyKeyboardMarkup(resize_keyboard= True, row_width= 1).add(bttn_back, *values.all_lessons, bttn_next)
class_admin_menu = ReplyKeyboardMarkup(resize_keyboard= True, row_width= 1).add(bttn_back, *values.all_class, bttn_next)
last_menu = ReplyKeyboardMarkup(resize_keyboard= True).add(bttn_accept, bttn_cancle) 