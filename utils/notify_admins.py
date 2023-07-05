from aiogram import types


async def on_startup_notify(dp):
    from handlers import general, client, seller
    general.register_handlers(dp)
    seller.register_handlers(dp)
    client.register_handlers(dp)
    chat_id = 539288377 #1065623427
    message = 'Bot has been started'
    await dp.bot.send_message(chat_id, message)


async def on_shutdown_notify(dp):
    chat_id = 539288377 #1065623427
    message = 'Bot has been stopped'
    await dp.bot.send_message(chat_id, message)
