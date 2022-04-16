from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
bot = (Bot(token="5399878060:AAHJGUQXmXqfDxSPUbPCc9hDs4JEvbTELIE"))
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"""
    Hello i'm bot for Akbar
    /adress
    /information
    /contact
    """)
@dp.message_handler(commands=['adress'])
async def process_help_command(message: types.Message):
    await message.reply("Uritskogo 13/33\n/start")
@dp.message_handler(commands=['information'])
async def process_help_command(message: types.Message):
    await message.reply("Hojiakbar Kasymov\n02/03/2002\n/start")
@dp.message_handler(commands=['contact'])
async def process_help_command(message: types.Message):
    await message.reply("Hoji Akbar:0222979774\n/start")
@dp.message_handler()
async def process_help_command(message: types.Message):
    await message.reply("error\n/start")
if __name__ == '__main__':
    executor.start_polling(dp)