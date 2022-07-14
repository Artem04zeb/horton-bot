from aiogram import executor, types, utils 
import logging  
from create_bot import dp
from handlers import commands, teacher, student, admin


logging.basicConfig(level=logging.INFO)


commands.register_commands(dp)
student.student_handlers(dp)
teacher.teacher_handlers(dp)
admin.admin_handlers(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)

