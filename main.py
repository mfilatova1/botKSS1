from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
import asyncio
import config
import texts
import handlers

#Подключение к боту
api = config.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

#Создание хэндлера-обработчика для команды /start
dp.message_handler(commands=['start'])(handlers.start)

#Создание хэндлера-обработчика для reply-кнопки '📌 О нас'
dp.message_handler(Text(equals=['📌 О нас']))(handlers.about_us)

#Создание хэндлера-обработчика для reply-кнопки '📌 Наши преподаватели'
dp.message_handler(Text(equals=['📌 Наши преподаватели']))(handlers.teachers)

#Создание хэндлеров-обработчиков для inline-клавиатуры teachers_kb
dp.callback_query_handler(text='Шапошникова Анастасия Васильевна')(handlers.teacher_Anastasia)
dp.callback_query_handler(text='Карпова Валентина Алексеевна')(handlers.teacher_Valentina)
dp.callback_query_handler(text='Кялина Александра Семеновна')(handlers.teacher_Aleksandra)
dp.callback_query_handler(text='Алексахина Васелина Игоревна')(handlers.teacher_Vaselina)

#Создание хэндлера-обработчика для reply-кнопки '📌 Танцевальные направления'
dp.message_handler(Text(equals=['📌 Танцевальные направления']))(handlers.dance_styles)

#Создание хэндлеров-обработчиков для inline-клавиатуры dance_styles_kb
dp.callback_query_handler(text='Hip-hop')(handlers.hip_hop)
dp.callback_query_handler(text='Krump')(handlers.krump)
dp.callback_query_handler(text='Afro')(handlers.afro)
dp.callback_query_handler(text='K-pop')(handlers.k_pop)
dp.callback_query_handler(text='High Heels')(handlers.high_heels)
dp.callback_query_handler(text='Waacking')(handlers.waacking)

#Создание хэндлеров-обработчиков для остальных кнопок reply-клавиатуры start_kb1
dp.message_handler(Text(equals=['📌 Расписание занятий']))(handlers.schedule)
dp.message_handler(Text(equals=['📌 Стоимость абонементов']))(handlers.cost)
dp.message_handler(Text(equals=['📌 Наши контакты']))(handlers.contacts)
dp.message_handler(Text(equals=['📌 Наша локация и залы']))(handlers.location)
dp.message_handler(Text(equals=['📌 Наши достижения']))(handlers.trophies)

dp.message_handler(Text(equals=['📌 Записаться на занятие']))(handlers.sign_up)
#Создание хэндлеров-обработчиков для машины состояний - запись на занятия
dp.message_handler(state=handlers.SignUp.name)(handlers.sign_up1)
dp.message_handler(state=handlers.SignUp.age)(handlers.sign_up2)
dp.message_handler(state=handlers.SignUp.style)(handlers.sign_up3)
dp.message_handler(state=handlers.SignUp.date)(handlers.sign_up4)

#Создание хэндлера-обработчика для кнопки '📌 Админ панель' reply-клавиатуры start_kb2
dp.message_handler(Text(equals=['📌 Админ панель']))(handlers.admin_panel)

#Создание хэндлеров-обработчиков для inline-клавиатуры AdminPanel
dp.callback_query_handler(text='statistick')(handlers.statistick)
dp.callback_query_handler(text="users")(handlers.users)
#Создание хэндлеров-обработчиков для машины состояний - рассылка
dp.callback_query_handler(text="mailing")(handlers.mailing)
dp.message_handler(state=handlers.admins.mailing_step1)(handlers.mailing1)
dp.message_handler(content_types=types.ContentTypes.PHOTO, state=handlers.admins.mailing_step2)(handlers.mailing2)
#Создание хэндлера-обработчика для inline клавиатуры back_to_admin
dp.callback_query_handler(text="back_to_admin")(handlers.back_admin)


#Запуск файла main, как главного
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)