from aiogram.dispatcher.filters.state import State, StatesGroup
import texts
from keyboards import *
from aiogram.types import InputMediaPhoto, InputMediaVideo
import config
import database
from aiogram import types


async def start(message):
    """
    Функция для работы команды /start
    - Проверка является ли пользователь администратором
    - Если id пользователя есть в списке admins, отправка сообщения с приветствием и клавиатурой
    для администратора start_kb2 (с кнопкой 'Admin panel')
    - Если id пользователя нет в списке admins, отправка сообщения с приветствием и клавиатурой
    для пользователя start_kb1 (без кнопки 'Admin panel')
    - Получение id пользователя
    - Получение имени пользователя
    - Добавление пользователя в базу данных
    """
    if message.from_user.id in config.admins:
        await message.answer(f'✅ Добро пожаловать, @{message.from_user.username}!\n\n' + texts.start, parse_mode='HTML',
                             reply_markup=start_kb2)
    else:
        await message.answer(f'✅ Добро пожаловать, @{message.from_user.username}!\n\n' + texts.start, parse_mode='HTML',
                             reply_markup=start_kb1)
    id = message.from_user.id
    username = message.from_user.username
    database.add(id, username)



async def about_us(message):
    """
    Функция для кнопки reply клавиатуры '📌 О нас'
    - Открытие файла - фото
    - Отправка сообщения с фото и текстом texts.about_us
    """
    with open('files/about.jpg', "rb") as img:
        await message.answer_photo(img, texts.about_us, parse_mode='HTML', reply_markup=start_kb1)

async def teachers(message):
    """
    Функция для кнопки reply клавиатуры '📌 Наши преподаватели'
    - Отправка сообщения с предложением выбрать ФИО преподователя из inline клавиатуры teachers_kb
    """
    await message.answer('<b>Выберите преподавателя ⬇️⬇️⬇️</b>', parse_mode='HTML', reply_markup=teachers_kb)

async def teacher_Anastasia(call):
    """
    Функция для кнопки inline клавиатуры 'Шапошникова Анастасия Васильевна'
    - Открытие файла - фото
    - Создание переменной mes для подготовки ответа - фото + текст с описанием texts.teacher_Anastasia
    - Отправка сообщения с переменной mes
    """
    with open('files/anastasia.jpg.', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.teacher_Anastasia, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=teachers_kb)
    await call.answer()

async def teacher_Valentina(call):
    """
    Функция для кнопки inline клавиатуры 'Карпова Валентина Алексеевна'
    - Открытие файла - фото
    - Создание переменной mes для подготовки ответа - фото + текст с описанием texts.teacher_Valentina
    - Отправка сообщения с переменной mes
    """
    with open('files/valentina.jpg.', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.teacher_Valentina, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=teachers_kb)
    await call.answer()

async def teacher_Aleksandra(call):
    """
    Функция для кнопки inline клавиатуры 'Кялина Александра Семеновна'
    - Открытие файла - фото
    - Создание переменной mes для подготовки ответа - фото + текст с описанием texts.teacher_Aleksandra
    - Отправка сообщения с переменной mes
    """
    with open('files/aleksandra.jpg.', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.teacher_Aleksandra, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=teachers_kb)
    await call.answer()

async def teacher_Vaselina(call):
    """
    Функция для кнопки inline клавиатуры 'Алексахина Васелина Игоревна''
    - Открытие файла - фото
    - Создание переменной mes для подготовки ответа - фото + текст с описанием texts.teacher_Vaselina
    - Отправка сообщения с переменной mes
    """
    with open('files/vaselina.jpg.', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.teacher_Vaselina, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=teachers_kb)
    await call.answer()

async def dance_styles(message):
    """
    Функция для кнопки reply клавиатуры '📌 Танцевальные направления'
    - Отправка сообщения с предложением выбрать танцевальное направление из inline клавиатуры dance_styles_kb
    """
    await message.answer('<b>Выберите стиль ⬇️⬇️⬇️</b>', parse_mode='HTML', reply_markup=dance_styles_kb)


async def hip_hop(call):
    """
    Функция для кнопки inline клавиатуры 'Hip-hop'
    - Открытие файла - видео
    - Создание переменной mes для подготовки ответа - видео + текст с описанием texts.hip_hop
    - Отправка сообщения с переменной mes
    """
    with open('files/video/hip-hop.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.hip_hop, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()


async def krump(call):
    """
    Функция для кнопки inline клавиатуры 'Krump'
    - Открытие файла - видео
    - Создание переменной mes для подготовки ответа - видео + текст с описанием texts.krump
    - Отправка сообщения с переменной mes
    """
    with open('files/video/krump.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.krump, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()

async def afro(call):
    """
    Функция для кнопки inline клавиатуры 'Afro'
    - Открытие файла - видео
    - Создание переменной mes для подготовки ответа - видео + текст с описанием texts.afro
    - Отправка сообщения с переменной mes
    """
    with open('files/video/afro.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.afro, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()

async def k_pop(call):
    """
    Функция для кнопки inline клавиатуры 'K-pop''
    - Открытие файла - видео
    - Создание переменной mes для подготовки ответа - видео + текст с описанием texts.k_pop
    - Отправка сообщения с переменной mes
    """
    with open('files/video/k-pop.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.k_pop, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()

async def high_heels(call):
    """
    Функция для кнопки inline клавиатуры 'High Heels''
    - Открытие файла - видео
    - Создание переменной mes для подготовки ответа - видео + текст с описанием texts.high_heels
    - Отправка сообщения с переменной mes
    """
    with open('files/video/high_heels.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.high_heels, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()

async def waacking(call):
    """
    Функция для кнопки inline клавиатуры 'Waacking''
    - Открытие файла - видео
    - Создание переменной mes для подготовки ответа - видео + текст с описанием texts.waacking
    - Отправка сообщения с переменной mes
    """
    with open('files/video/wacking.MP4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.waacking, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()


async def schedule(message):
    """
    Функция для кнопки reply клавиатуры '📌 Расписание занятий'
    - Открытие файла - картинка
    - Отправка сообщения с картинкой (таблица) и описанием texts.schedule
    """
    with open('files/schedule.png', "rb") as img:
        await message.answer_photo(img, texts.schedule, parse_mode='HTML', reply_markup=start_kb1)

async def cost(message):
    """
    Функция для кнопки reply клавиатуры '📌 Стоимость абонементов'
    - Открытие файла - картинка
    - Отправка сообщения с картинкой (таблица) и описанием texts.cost
    """
    with open('files/cost.png', "rb") as img:
        await message.answer_photo(img, texts.cost, parse_mode='HTML', reply_markup=start_kb1)

async def contacts(message):
    """
    Функция для кнопки reply клавиатуры '📌 Наши контакты'
    - Отправка сообщения с описанием texts.contacts
    """
    await message.answer(texts.contacts, parse_mode='HTML', reply_markup=start_kb1)

async def location(message):
    """
    Функция для кнопки reply клавиатуры '📌 Наша локация и залы'
    - Открытие файла - фото
    - Отправка сообщения с фото и описанием texts.location
    """
    with open('files/halls.jpg', "rb") as img:
        await message.answer_photo(img, texts.location, parse_mode='HTML', reply_markup=start_kb1)

async def trophies(message):
    """
    Функция для кнопки reply клавиатуры '📌 Наши достижения'
    - Открытие файла - фото
    - Отправка сообщения с фото и описанием texts.trophies
    """
    with open('files/trophies.jpg', "rb") as img:
        await message.answer_photo(img, texts.trophies, parse_mode='HTML', reply_markup=start_kb1)



class SignUp(StatesGroup):
    """
    Класс SignUp для машины состояний, наследованный от StatesGroup для записи на первое пробное занятие
    - Создание переменных для состояний
    """
    name = State()
    age = State()
    style = State()
    date = State()


async def sign_up(message: types.Message):
    """
    Функция для записи на первое пробное занятие
    - Создание переменной с инструкцией
    - Отправка сообщения с инструкцией
    - Сохранение состояния SignUp.name.set()
    """
    instructions = ("Первое пробное занятие - <b>бесплатно</b>\n"
                    "Введите свою фамилию и имя:")
    await message.answer(instructions, parse_mode="HTML")
    await SignUp.name.set()


async def sign_up1(message: types.Message, state):
    """
    Функция для записи на первое пробное занятие
    - Добавление состояния name в словарь data
    - Создание переменной с инструкцией
    - Отправка сообщения с инструкцией
    - Сохранение состояния SignUp.age.set()
    """
    await state.update_data(name=str(message.text))

    instructions = "Введите свой возраст:"
    await message.answer(text=instructions)
    await SignUp.age.set()

async def sign_up2(message: types.Message, state):
    """
    Функция для записи на первое пробное занятие
    - Добавление состояния age в словарь data
    - Создание переменной с инструкцией
    - Отправка сообщения с инструкцией
    - Сохранение состояния SignUp.style.set()
    """
    await state.update_data(age=str(message.text))

    instructions = "Введите танцевальный стиль, который Вас заинтересовал:"
    await message.answer(text=instructions)
    await SignUp.style.set()

async def sign_up3(message: types.Message, state):
    """
    Функция для записи на первое пробное занятие
    - Добавление состояния style в словарь data
    - Открытие файла картинки "расписание"
    - Создание переменной с инструкцией
    - Отправка сообщения с инструкцией и картинкой "расписание"
    - Сохранение состояния SignUp.date.set()
    """
    await state.update_data(style=str(message.text))

    with open('files/schedule.png', "rb") as img:
        instructions = ("Введите дату, когда посетите пробное занятие в формате <i>'12 декабря'</i>\n "
                        "При выборе даты, пожалуйста, ориентируйтесь на расписание занятий нужной Вам группы")
        await message.answer_photo(img, instructions, parse_mode="HTML")
    await SignUp.date.set()

async def sign_up4(message, state):
    """
    Функция для записи на первое пробное занятие
    - Импорт бота из файла main
    - Добавление состояния date в словарь data
    - Создание переменной словаря data, получение всех состояний state.get_data()
    - Создание переменной username, получение имени пользователя
    - Создание переменной администраторов, получение списка администраторов из файла config
    - Цикл для перебора списка администраторов
    - Пока id == id администраторов, отправка уведомления о записи на первое пробное занятие
    - Создание исключения в случае ошибки
    - Ответ пользователю с ифнормацией о записи на первое пробное занятие с датой
    - Создание переменной id, получение id пользователя
    - Добавление в базу данных информации о записи на первое пробное занятие
    - Завершение машины состояний
    """
    from main import bot
    await state.update_data(date=str(message.text))
    data = await state.get_data()
    username = message.from_user.username
    admins = config.admins
    for id in admins:
        try:
            await bot.send_message(id,
                                   f"Новая запись:\nТг: {username}\nИмя: {data['name']}\nВозраст: {data['age']}\nСтиль: {data['style']}\nДата: {data['date']}")
        except Exception as e:
            print(e)

    await message.answer(f'Вы записаны на пробное занятие на {data["date"]}\nЖдем Вас!🥰')
    id = message.from_user.id
    database.add1(id, username, data['name'], data['age'], data['style'], data['date'])
    await state.finish()


async def admin_panel(message):
    """
    Функция для кнопки reply клавиатуры '📌 Админ панель'
    - Отправка сообщения с предложением выбрать действие из inline клавиатуры AdminPanel
    """
    await message.answer('<b>Вы открыли панель администратора. Выберите действие ⬇️⬇️⬇️</b>', parse_mode='HTML', reply_markup=AdminPanel)


async def statistick(call: types.CallbackQuery):
    """
    Функция для кнопки inline клавиатуры '📊 Статистика'
    - Отправка сообщения с подсчетом количества пользователей
    """
    await call.message.edit_text(texts.statistick(int(database.count())), parse_mode="HTML", reply_markup=back_to_admin)
    await call.answer()

async def back_admin(call: types.CallbackQuery):
    await call.message.edit_text('<b>Вы открыли панель администратора. Выберите действие ⬇️⬇️⬇️</b>', parse_mode='HTML', reply_markup=AdminPanel)
    await call.answer()

async def users(call: types.CallbackQuery):
    """
    Функция для кнопки inline клавиатуры '👥 Пользователи'
    - Отправка сообщения со списком пользователей из базы данных, таблица users - id, username
    """
    await call.message.edit_text(f'<pre>{database.get_all()}</pre>', parse_mode="HTML", reply_markup=back_to_admin)
    await call.answer()



class admins(StatesGroup):
    """
    Класс admins для машины состояний, наследованный от StatesGroup для рассылки информации пользователям
    - Создание переменных для состояний
    """
    mailing_step1 = State()
    mailing_step2 = State()


async def mailing(call: types.CallbackQuery):
    """
    Функция для рассылки информации пользователям
    - Создание переменной с инструкцией
    - Отправка сообщения с инструкцией
    - Сохранение состояния admins.mailing_step1.set()
    """
    instructions = ("Для отмены, нажмите кнопку <b>/cancel</b>\n"
                    "Введите текст сообщения:")
    await call.message.answer(instructions, parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    await call.answer()
    await admins.mailing_step1.set()


async def mailing1(message, state):
    """
    Функция для рассылки информации пользователям
    - Добавление состояния mailing_step1 в словарь data
    - Добавление команды /cancel для отмены создания рассылки
    - Ответ пользователю и возврат в панель администратора, если выбрана команда /cancel
    - Завершение машины состояний
    - Если не выбрана команда /cancel, создание переменной с инструкцией
    - Отправка сообщения с инструкцией
    - Сохранение состояния admins.mailing_step2.set()
    """
    await state.update_data(text=message.text)
    if message.text == '/cancel':
        await message.answer("Вы вернулись в панель администратора", reply_markup=AdminPanel)
        await state.finish()
        return
    else:
        instructions = "Прикрепите фотографию к сообщению:"
        await message.answer(text=instructions, parse_mode="HTML")

        await admins.mailing_step2.set()


async def mailing2(message, state):
    """
    Функция для рассылки информации пользователям
    - Импорт бота с файла main
    - Сохранение полученного фото в директорию files
    - Создание переменной словаря data, получение всех состояний state.get_data()
    - Создание переменной subscribers, получение из базы данных, таблицы users id всех пользователей
    - Создание счетчика c = 0
    - Создание цикла перебора всех пользователей в списке subscribers
    - Открытие сохраненного фото
    - Отправка сообщений всем пользователям с фото и описанием, полученного из словаря data
    - Создание исключения
    - Отправка сообщения администратору с текстом об успещной рассылке и
    количеством отправленных сообщений на основании количества пользователей в базе данных
    - Завершение машины состояний
    """
    from main import bot

    await message.photo[-1].download(destination_file='files/photo.jpg')
    data = await state.get_data()
    subscribers = database.get_id()

    c = 0
    for (user_id,) in subscribers:
        try:
            with open('files/photo.jpg', 'rb') as f:
                await bot.send_photo(user_id, f, data['text'])
            c += 1
        except Exception as e:
            print(e)

    await message.answer(f'Рассылка успешно завершена: {c} / {database.count()}', reply_markup=AdminPanel)
    await state.finish()







