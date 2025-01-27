from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

router = Router()

def webAppKeyboard():
    webAppUrl = WebAppInfo(url="https://swap-rocket.onrender.com/")

    buttons = [
            [
                InlineKeyboardButton(text="Веб приложение", web_app=webAppUrl) #создаем кнопку типа webapp
            ],
        ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет!", reply_markup=webAppKeyboard())
    # await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне команду /id", reply_markup=webAppKeyboard())


# @router.message(Command("id"))
# async def message_handler(msg: Message):
#     await msg.answer(f"Твой ID: {msg.from_user.id}")

