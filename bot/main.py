from dotenv import load_dotenv
import logging  # после выхода в прод надо выключить
import os
import asyncio

from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, WebAppInfo

web = WebAppInfo(url="https://localhost:3000/")

dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Мое положение")],
        [KeyboardButton(text="Рейтинг", web_app=web),
         KeyboardButton(text="Получить тест-кейс")]
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!\n Что-то надо написать...", reply_markup=keyboard)


@dp.message()
async def cmd_test(message: Message):
    if message.text == "Получить тест-кейс":
        text = "Этот бот  отправляет тесты и ответы для задач Соревнования 'Code&Garden' от Яндекс Лицея." \
               "\nВы вводите номер контеста, задачи и теста. Вам придет файл со входными данным и ожидаемым результатом." \
               "\nЗапросы на получение входных данных вы можете делать не чаще, чем раз в 3 минут." \
               "\n**----------------------------------------------**" \
               "\n**Например**" \
               "\nВведите номер контеста (1 для первого по счету проведенного соревнования, 2 второго и т.д), " \
               "\nзатем букву задачи (буква от A до количества задач в этом контесте), а затем номер теста. " \
               "\nНапример '1 C 3' соответствует тесту номер 3 из задачи C первого контеста."

        await message.answer(text, parse_mode="Markdown")


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN"))
    # dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
