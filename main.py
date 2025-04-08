import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.executor import start_polling
import os

API_TOKEN = os.getenv("API_TOKEN")
PARTNER_LINK = os.getenv("PARTNER_LINK")
PROMOCODE = os.getenv("PROMOCODE")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_markup = ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.add(KeyboardButton("Старт"))

menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
menu_markup.add(KeyboardButton("Получить доступ"), KeyboardButton("Регистрация"), KeyboardButton("Помощь"))

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer_photo(open("assets/hello.jpg", "rb"), caption="Добро пожаловать! Жми 'Старт'", reply_markup=start_markup)

@dp.message_handler(lambda message: message.text == "Старт")
async def show_menu(msg: types.Message):
    await msg.answer_photo(open("assets/legend.jpg", "rb"),
        caption="Я — бывший инсайдер 1win. Помогаю людям узнать алгоритмы!",
        reply_markup=menu_markup)

@dp.message_handler(lambda message: message.text == "Получить доступ")
async def try_access(msg: types.Message):
    await msg.answer_photo(open("assets/error.jpg", "rb"),
        caption="Вы не зарегистрированы. Сначала пройдите регистрацию.")

@dp.message_handler(lambda message: message.text == "Регистрация")
async def register(msg: types.Message):
    await msg.answer(f"Зарегистрируйтесь на сайте {PARTNER_LINK} и используйте промокод: {PROMOCODE}")

@dp.message_handler(lambda message: message.text == "Помощь")
async def help_msg(msg: types.Message):
    await msg.answer_photo(open("assets/help.jpg", "rb"),
        caption="Если возникли проблемы — напиши @SupportHelper")

if __name__ == '__main__':
    start_polling(dp, skip_updates=True)