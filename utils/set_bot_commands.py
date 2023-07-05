from aiogram import types

async def set_default_commands(dp):
    # Код для установки стандартных команд бота
    # Создание списка команд
    commands = [
        types.BotCommand(command='/start', description='Start the bot'),
        types.BotCommand(command='/make_order', description='Make an order'),
    ]
    # Установка списка команд
    await dp.bot.set_my_commands(commands)