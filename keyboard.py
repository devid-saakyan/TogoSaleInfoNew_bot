from aiogram import types

def keyboard1():
    markup = types.InlineKeyboardMarkup(resize_keyboard=True, selective=True)
    button_1 = types.InlineKeyboardButton('Завершено', callback_data='finish')
    markup.add(button_1)
    return markup

def keyboard2():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('Управляющий')
    button2 = types.KeyboardButton('HR')
    button3 = types.KeyboardButton('Начальник склада')
    button4 = types.KeyboardButton('IT-директор')
    button5 = types.KeyboardButton('Бухгалтер')
    button6 = types.KeyboardButton('Офис-менеджер')
    button7 = types.KeyboardButton('Ассистент руководителя')
    button8 = types.KeyboardButton('Ассистент управляющего')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
    return markup

def keyboard3():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('Склад')
    button2 = types.KeyboardButton('Офис-собственника')
    button3 = types.KeyboardButton('Администарция')
    button4 = types.KeyboardButton('Важная информация')
    button5 = types.KeyboardButton('Отдел продаж')
    markup.add(button1, button2, button3, button4, button5)
    return markup

def keyboard_sklad():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('Обеспечение жизнедеятельности склада')
    button2 = types.KeyboardButton('Распределение магазинов и ИП')
    button3 = types.KeyboardButton('Регламент работы сотрудников склада')
    button4 = types.KeyboardButton('Начальник склада')
    button5 = types.KeyboardButton('Закупка')
    button6 = types.KeyboardButton('Должности')
    button_back = types.KeyboardButton('⬅ Назад')
    sp = [button1, button2, button3, button4, button5, button6]
    for i in sp:
        markup.row(i)
    markup.row(button_back)
    return markup

def keyboard_ofis():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('Юридическая безопасность')
    button2 = types.KeyboardButton('Организационная политика')
    button3 = types.KeyboardButton('Финаносовая система')
    button4 = types.KeyboardButton('Технологии')
    button5 = types.KeyboardButton('Управление директором')
    button6 = types.KeyboardButton('Управление ценным имуществом')
    button7 = types.KeyboardButton('Построение компании')
    button8 = types.KeyboardButton('Должности')
    sp = [button1, button2, button3, button4, button5, button6, button7, button8]
    button_back = types.KeyboardButton('⬅ Назад')
    for i in sp:
        markup.row(i)
    markup.row(button_back)
    return markup

def keyboard_admin():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('Должностные инструкции')
    button2 = types.KeyboardButton('Логистика')
    button3 = types.KeyboardButton('IT-отдел')
    button4 = types.KeyboardButton('HR-отдел')
    button_back = types.KeyboardButton('⬅ Назад')
    markup.add(button1, button2, button3, button4)
    markup.row(button_back)
    return markup

def keyboard_vajn_infa():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('Шаблон письма для регистрации ТЗ')
    button2 = types.KeyboardButton('Дорога до офиса и склада')
    button3 = types.KeyboardButton('Контакты сотрудников')
    button4 = types.KeyboardButton('Увольнение')
    button5 = types.KeyboardButton('Чаты компании')
    button6 = types.KeyboardButton('Миссия и цели компании')
    button7 = types.KeyboardButton('Протоколы планерок')
    button8 = types.KeyboardButton('Шаблон для постановки задач')
    button9 = types.KeyboardButton('Список печатей и их наличие на складе и в офисе')
    button10 = types.KeyboardButton('Закупка канцелярии в офис')
    button11 = types.KeyboardButton('Инструкция по обращению с пропусками')
    sp = [button2, button3, button4, button5, button6, button7, button8, button10, button11]
    button_back = types.KeyboardButton('⬅ Назад')
    for i in sp:
        markup.row(i)
    markup.row(button_back)
    return markup

def keyboard_op():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    button1 = types.KeyboardButton('Распределение магазинов и ИП')
    button2 = types.KeyboardButton('Инвентаризация склада')
    button3 = types.KeyboardButton('Работа с Ozon и WB')
    button_back = types.KeyboardButton('⬅ Назад')
    markup.add(button1, button2, button3)
    markup.row(button_back)
    return markup