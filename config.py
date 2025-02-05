from os import getenv
from dotenv import load_dotenv
from typing import Final

load_dotenv()

BOT_TOKEN: Final = getenv("BOT_TOKEN")
BOT_USERNAME: Final = getenv("BOT_USERNAME")
API_ID: Final = getenv("API_ID")
API_HASH: Final = getenv("API_HASH")
