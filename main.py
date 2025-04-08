from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import types
from aiogram.utils import executor
import random
import logging
import os

API_TOKEN = "8166036388:AAETVsoAEJiJTabvTKTgz3b_7eilRpL3emA"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

def main_menu_keyboard():
    buttons = [
        KeyboardButton("Старт"),
        KeyboardButton("Регистрация"),
        KeyboardButton("Помощь")
    ]
    return ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer_photo(photo=open("media/welcome.jpg", "rb"),
        caption="Привет! Этот бот поможет тебе узнать секреты алгоритмов 1WIN и заработать."
                "Но для начала тебе нужно пройти регистрацию и пополнить баланс."
                "Готов? Жми кнопку ниже!",
        reply_markup=main_menu_keyboard())

@dp.message_handler(lambda message: message.text.lower() == "старт")
async def handle_start(message: types.Message):
    await message.answer_photo(photo=open("media/legend.jpg", "rb"),
        caption="Меня зовут Артём, я бывший сотрудник 1WIN."
                "Я создал бота, чтобы делиться алгоритмами, которые раньше сам писал для них."
                "Чтобы получить доступ к алгоритму, пройди шаги ниже.",
        reply_markup=main_menu_keyboard())

@dp.message_handler(lambda message: message.text.lower() == "регистрация")
async def handle_register(message: types.Message):
    await message.answer_photo(photo=open("media/register.jpg", "rb"),
        caption="1. Перейди по ссылке: https://1wqjnb.com/?p=d57c"
                "2. Введи промокод: TYKI"
                "3. Пополни баланс от 500 рублей"
                "После пополнения вернись и нажми 'Получить доступ'.",
        reply_markup=main_menu_keyboard())

@dp.message_handler(lambda message: message.text.lower() == "помощь")
async def handle_help(message: types.Message):
    await message.answer_photo(photo=open("media/help.jpg", "rb"),
        caption="Если возникли трудности:"
                "- Убедись, что перешёл по ссылке и ввёл промокод TYKI"
                "- Пополни баланс от 500₽"
                "- Если всё сделал — возвращайся и жми 'Получить доступ'"
                "Поддержка: @support_username",
        reply_markup=main_menu_keyboard())

@dp.message_handler(lambda message: message.text.lower() == "получить доступ")
async def handle_access(message: types.Message):
    await message.answer("Ошибка: вы ещё не зарегистрировались или не пополнили баланс.",
                         reply_markup=main_menu_keyboard())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
