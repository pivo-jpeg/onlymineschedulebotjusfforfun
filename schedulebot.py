import logging
 
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2127777447:AAHQqAxxmNF-C0XxopunCWxX2NHnnQM6tVA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
   "Это сообщение будет показываться при вводе команд: /start или /help."
   await message.reply("Привет! При вводе команд, вы увидите расписание! Если у вас есть какие-то идеи — просто пишите их сюда!")

@dp.message_handler(commands=["monday"])
async def chat(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.reply('1. Физкультура, спорт.зал;\n2. Английский язык, 99/74;\n3. История, ?;\n4. Физика, 5;\n5. Воспитание, ?;\n6. Узбекский, 65/?.')
@dp.message_handler(commands=["tuesday"])
async def tuesday(message: types.Message):
    await message.reply("1. Биология, 30;\n2.География, 40;\n3. Математика, 19;\n4. ИЗО, 73;\n5. Английский язык, 99/?;\n6. Физика, 5.")
@dp.message_handler(commands=["wednesday"])
async def wednesday(message: types.Message):
    await message.reply("1. Технология, ?/?;\n2. Технология, ?/?;\n3. Биология, ?;\n4.Английский язык, 99/?;\n5. История, ?;\n6. Литература, ?.")
@dp.message_handler(commands=['thursday'])
async def thursday(message: types.Message):
    await message.reply("1. Литература, ;?\n2.Математика, 19;\n3. Музыка, 27;\n4. Математика, 19;\n5.Русский язык, ?.")
@dp.message_handler(commands=["friday"])
async def friday(message: types.Message):
    await message.reply("1. Воспитательный час, 65;\n2. Информатика, 3/1;\n3. Узбекский язык, 65/?;\n4. Русский язык, ?;\n5. Физика, 5;\n6. Математика, 19.")
@dp.message_handler(commands=["source_code"])
async def code(message: types.Message):
    await message.reply('<a href="https://github.com/pivo-jpeg/onlymineschedulebotjusfforfun"><b>GitHub</b></a>', parse_mode= "HTML")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)