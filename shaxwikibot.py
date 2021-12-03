import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5028108130:AAGg34KxnI2vYgg1ZROYWFKp3llC-VQLQ90'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum hurmatli do'stlar Wiki botimizga xush kelibsizlar")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Kechirasiz siz qidirgan mavzu topilmadi. Iltimos yana bir bor urinib ko\'ring')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)