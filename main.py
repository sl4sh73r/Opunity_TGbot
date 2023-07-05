from aiogram import executor
import loader
from utils.notify_admins import on_shutdown_notify, on_startup_notify


if __name__ == '__main__':
    executor.start_polling(
        loader.dp, 
        on_startup=on_startup_notify,
        on_shutdown=on_shutdown_notify
    )