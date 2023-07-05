from telebot.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton
)


# Inline Keyboards


# Reply Keyboards

user_type = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
client = KeyboardButton('Хочу заказать модель')
executor = KeyboardButton('Я — исполнитель')
user_type.add(client, executor)

client_menu = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
new_order = KeyboardButton('Новый заказ')
status_order = KeyboardButton('Статус заказов')
client_menu.add(new_order, status_order)

offer_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
yes = KeyboardButton('Да')
no = KeyboardButton('Нет')
offer_markup.add(yes, no)

skip_markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
skip_btn = KeyboardButton('Пропустить')
skip_markup.add(skip_btn)

executor_type_markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
self_employed = KeyboardButton('Самозанятый')
ip = KeyboardButton('ИП')
ooo = KeyboardButton('ООО')
executor_type_markup.add(self_employed, ip, ooo, skip_btn)

next_steps_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
new_order_btn = KeyboardButton('Новый заказ')
order_list_btn = KeyboardButton('Список моих заказов')
next_steps_markup.add(new_order_btn, order_list_btn)

