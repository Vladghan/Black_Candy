from sqlite3 import IntegrityError
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Regexp
from aiogram.types import Message, CallbackQuery
from aiogram import types
from aiogram.utils.exceptions import BadRequest, BotBlocked
from config import admin_ids
from my_logger import logger
from keyboards import kb1b
from loader import dp, bot
import asyncio
from datetime import datetime


@dp.message_handler(Command("sessions"))
async def update_questions(message: Message):
    logger.debug(f'{message.from_user.id} entered /sessions command')
    await message.answer('Эта команда отправляет список текущих активных котировочных сессий, в которых вы участвуете')


@dp.message_handler(Command("start"))
async def start(message: Message):
    try:
        date = message.date.strftime('%Y-%m-%d %H:%M:%S')
        # db.add_user(message.from_user.id, date, message.from_user.first_name,
        #             message.from_user.last_name, message.from_user.username)
        await message.answer(text=f"Добрый день. Вы зарегестрировались в боте портала zakupki.mos.ru\n\n"
                                  f"Здесь вы сможете получать уведомления о статусе ваших текущих котировочных сессий.\n\n"
                             )
        logger.debug(f'{message.from_user.id} joined bot.')
    except IntegrityError as err:
        logger.error(f'Пользователь {message.from_user.id}: {err}')
        await message.answer(text="Кажется, вы уже нажимали эту кнопку…\n"
                                  "Если возниклик какие-то трудности — напишите @(аккаунт поддержки)")
        logger.debug(f'{message.from_user.id} tried to use /start command again')

