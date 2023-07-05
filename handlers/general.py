from aiogram import types
from loader import dp
from messages import *
from aiogram import Dispatcher
from keyboards import start_inline_keyboard


@dp.message_handler(commands=['start', 'help'], state='*')
async def welcome_user(message: types.Message):
    await message.answer(
        text=WELCOME_TEXT,
        reply_markup=start_inline_keyboard
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(
        welcome_user,
        commands=['start', 'help'],
        state='*'
    )