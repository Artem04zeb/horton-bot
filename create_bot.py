from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Bot object
# Создаем объект бота
bot = Bot(token='1796345486:AAFmfOAmi9I_Mq6KPHrEyIsNWFZoGQqgUcc')
# Dispatcher for bot
# Диспетчер для бота
dp = Dispatcher(bot, storage= MemoryStorage())