from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from set_bot_commands import set_default_commands
from dotenv import load_dotenv
import os
from time import sleep
from keyboard import *


load_dotenv()
TOKEN = os.environ.get("TOKEN")

bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

async def on_startup(dp):
    await set_default_commands(dp)


class States(StatesGroup):
    state1 = State()
    state2 = State()
    sklad = State()
    ofis_s = State()
    admin = State()
    vajn_infa = State()
    otdel_prodaj = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет👋\nЯ ваш виртуальный помощник по освоению материала в нашей компании')
    sleep(2)
    await message.answer('Ах, да... Забыл представиться, я - бот Лера, к вашим услугам')
    sleep(2)
    await message.answer("Чтобы мы продолжили дальнейшее общение, вам необходимо заполнить форму по ссылке ниже\nПрошу, после завершения, нажать на кнопку 'Завершено'")
    sleep(2)
    await message.answer('https://docs.google.com/forms/d/e/1FAIpQLSeuziM3rTD0Cwj2o_YkD5Vq67AbwE65Z80ZvV2evciSvCBsrw/viewform', reply_markup=keyboard1())

@dp.message_handler(commands=['menu'])
async def menu(message:types.Message):
    await message.answer('Выберите пункт из меню: ', reply_markup=keyboard3())
    await States.state2.set()

@dp.callback_query_handler(lambda c: c.data == 'finish')
async def process_after_finish(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, text = 'Отлично! Теперь введите пароль, чтобы я смог помочь вам!')

@dp.message_handler(content_types=['text'])
async def message(message:types.Message):
    if message.text == '11111':
        await message.answer('Открываю доступ...')
        await message.answer('На какую должность вы вступаете:', reply_markup = keyboard2())
        await States.state1.set()
    else:
        await message.answer('Неверный пароль, попробуйте ещё раз')

@dp.message_handler(state = States.state1)
async def state1(message: types.Message):
    await message.answer('Хорошо, выберите пункт из меню', reply_markup=keyboard3())
    await States.state2.set()

@dp.message_handler(state = States.state2)
async def state2(message: types.Message, state: FSMContext):
    if message.text == 'Склад':
        await message.answer('Вы выбрали пункт Склад, выберите направление из меню', reply_markup=keyboard_sklad())
        await States.sklad.set()
    elif message.text == 'Офис-собственника':
        await message.answer('Вы выбрали пункт Офис-собственника, выберите направление из меню', reply_markup=keyboard_ofis())
        await States.ofis_s.set()
    elif message.text == 'Администарция':
        await message.answer('Вы выбрали пункт Администарция, выберите направление из меню', reply_markup=keyboard_admin())
        await States.admin.set()
    elif message.text == 'Важная информация':
        #await message.answer('Вы выбрали пункт Важная информация, выберите направление из меню', reply_markup=keyboard_vajn_infa())
        await message.answer('https://docs.google.com/document/d/1AZsS7gbPooiElsF_kThMiNM27EcTvp50to4YcOKXWuY/edit')
        #await States.vajn_infa.set()
        await state.reset_state()
    elif message.text == 'Отдел продаж':
        await message.answer('Вы выбрали пункт Отдел продаж, выберите направление из меню', reply_markup=keyboard_op())
        await States.otdel_prodaj.set()

@dp.message_handler(state = States.sklad)
async def state_sklad(message: types.Message, state: FSMContext):
    if message.text == '⬅ Назад':
        await message.answer('Выберите пункт из меню:', reply_markup=keyboard3())
        await States.state2.set()
        return True
    if message.text == 'Должности':
        await message.answer('https://docs.google.com/document/d/12PPNiRoFa0R6I5o91Felo9esoT522fvm8BIBgGqr6ek/edit')
    await state.reset_state()

@dp.message_handler(state = States.ofis_s)
async def state_sklad(message: types.Message, state: FSMContext):
    if message.text == '⬅ Назад':
        await message.answer('Выберите пункт из меню:', reply_markup=keyboard3())
        await States.state2.set()
        return True
    if message.text == 'Должности':
        await message.answer('https://docs.google.com/document/d/12PPNiRoFa0R6I5o91Felo9esoT522fvm8BIBgGqr6e')
    await state.reset_state()

@dp.message_handler(state = States.admin)
async def state_sklad(message: types.Message, state: FSMContext):
    if message.text == '⬅ Назад':
        await message.answer('Выберите пункт из меню:', reply_markup=keyboard3())
        await States.state2.set()
        return True
    await message.answer('Пока пусто')
    await state.reset_state()

@dp.message_handler(state = States.otdel_prodaj)
async def state_sklad(message: types.Message, state: FSMContext):
    if message.text == '⬅ Назад':
        await message.answer('Выберите пункт из меню:', reply_markup=keyboard3())
        await States.state2.set()
        return True
    await message.answer('Пока пусто')
    await state.reset_state()

@dp.message_handler(state = States.vajn_infa)
async def state_vajn_infa(message: types.Message, state: FSMContext):
    if message.text == '⬅ Назад':
        await message.answer('Выберите пункт из меню:', reply_markup=keyboard3())
        await States.state2.set()
        return True
    await message.answer('https://docs.google.com/document/d/1zdNjI7w92XhQyV1QZNbTMSxZaEV_dLz_kq8YTBPZWx8/edit')
    await message.answer('https://docs.google.com/document/d/1AZsS7gbPooiElsF_kThMiNM27EcTvp50to4YcOKXWuY/edit')
    await state.reset_state()
executor.start_polling(dp, on_startup=on_startup)
