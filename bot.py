from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)