from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton
)


start_inline_keyboard = InlineKeyboardMarkup(row_width=1)
client_button = InlineKeyboardButton(
    text='Я - заказчик',
    callback_data='i_am_client'
)
seller_button = InlineKeyboardButton(
    text='Я - исполнитель',
    callback_data='i_am_seller'
)
start_inline_keyboard.add(client_button).add(seller_button)


acceptance_keyboard = InlineKeyboardMarkup(row_width=1)
accept_button = InlineKeyboardButton(
    text='Принять',
    callback_data='accept'
)
decline_button = InlineKeyboardButton(
    text='Отклонить',
    callback_data='decline'
)
acceptance_keyboard.add(accept_button).add(decline_button)