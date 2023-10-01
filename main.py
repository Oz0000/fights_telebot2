import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import tyson, sugar, ali, marciano, mayweather, hearns, jones, louis, foreman, frazier

token = '6318692304:AAGk6FI8dsv6RwcnfD_zDZCu_c41kUWj9Og'
dis = Dispatcher()

@dis.message(CommandStart())
async def answer_commands(message):
    boxers = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Mike Tyson')],
    [KeyboardButton(text='Sugar Ray Leonard')],
    [KeyboardButton(text='Muhammad Ali')],
    [KeyboardButton(text='Rocky Marciano')],
    [KeyboardButton(text='Floyd Mayweather')],
    [KeyboardButton(text='Thomas Hearns')],
    [KeyboardButton(text='Roy Jones')],
    [KeyboardButton(text='Joe Louis')],
    [KeyboardButton(text='George Foreman')],
    [KeyboardButton(text='Joe Frazier')]])

    await message.answer('Hey kid. right here, you can see the Legendary Boxers:', reply_markup=boxers)


@dis.message()
async def answer_message(message):
    dct = {'Mike Tyson': ('Mike Tyson with:', tyson), 'Sugar Ray Leonard': ('Sugar Ray with:', sugar), 'Muhammad Ali': ('Muhammad Ali with:', ali), 'Rocky Marciano': ('Rocky Marciano with:', marciano), 'Floyd Mayweather': ('Floyd Mayweather with:', mayweather), 'Thomas Hearns': ('Thomas Hearns with:', hearns), 'Roy Jones': ('Roy Jones with:', jones), 'Joe Louis': ('Joe Louis with:', louis), 'George Foreman': ('George Foreman with:', foreman), 'Joe Frazier': ('Joe Frazier with:', frazier)}
    text = message.text
    await message.answer(dct[text][0], reply_markup=dct[text][1])

async def start():
    tb = Bot(token=token)
    await dis.start_polling(tb)


if __name__ == '__main__':
    asyncio.run(start())

