from aiogram.types import (
    ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
)


start_keyboard = ReplyKeyboardMarkup()

client_button = KeyboardButton('Я - заказчик')
seller_button = KeyboardButton('Я - исполнитель')

start_keyboard.add(client_button).add(seller_button)