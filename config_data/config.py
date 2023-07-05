import os

from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.getenv('TOKEN')

DEFAULT_COMMANDS = (
    ('start', 'Run the bot'),
    ('help', 'Show Help'),
)
