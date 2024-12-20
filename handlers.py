from aiogram.dispatcher.filters.state import State, StatesGroup
import texts
from keyboards import *
from aiogram.types import InputMediaPhoto, InputMediaVideo
import config
import database
from aiogram import types


async def start(message):
    """
    Функция для работы команды /start проверяет является ли пользователь администратором.
    Если id пользователя есть в списке admins, отправляет сообщение с приветствием и клавиатурой
    для администратора start_kb2 (с кнопкой 'Admin panel').
    Если id пользователя нет в списке admins, отправляет сообщение с приветствием и клавиатурой
    для пользователя start_kb1 (без кнопки 'Admin panel'). Получает id и имя пользователя.
    Добавляет пользователя в базу данных.

    :param message: Сообщение от пользователя - команда /start
    :return: Ответ пользователю - приветствие + клавиатура. Сохранение пользователя в базу данных.
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
    Функция для кнопки reply клавиатуры '📌 О нас'. Открывает файл - фото, отправляет сообщение пользователю
    с фото и текстом texts.about_us

    :param message: Сообщение от пользователя - нажатие кнопки reply клавиатуры
    :return: Ответ пользователю - фото + описание.
    """

    with open('files/about.jpg', "rb") as img:
        await message.answer_photo(img, texts.about_us, parse_mode='HTML', reply_markup=start_kb1)

async def teachers(message):
    """
    Функция для кнопки reply клавиатуры '📌 Наши преподаватели'. Отправляет сообщение с предложением выбрать ФИО
    преподователя из inline клавиатуры teachers_kb

    :param message: Сообщение от пользователя - нажатие кнопки reply клавиатуры
    :return: Ответ пользователю - текст + inline клавиатура
    """

    await message.answer('<b>Выберите преподавателя ⬇️⬇️⬇️</b>', parse_mode='HTML', reply_markup=teachers_kb)

async def teacher_Anastasia(call):
    """
    Функция для кнопки inline клавиатуры 'Шапошникова Анастасия Васильевна'. Открывает файл - фото.
    Создает переменную mes для подготовки ответа - фото + текст с описанием texts.teacher_Anastasia.
    Отправляет сообщение с переменной mes

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + фото преподавателя + inline клавиатура
    """

    with open('files/anastasia.jpg.', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.teacher_Anastasia, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=teachers_kb)
    await call.answer()

async def teacher_Valentina(call):
    """
    Функция для кнопки inline клавиатуры 'Карпова Валентина Алексеевна'. Открывает файл - фото.
    Создает переменную mes для подготовки ответа - фото + текст с описанием texts.teacher_Valentina.
    Отправляет сообщение с переменной mes.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + фото преподавателя + inline клавиатура
    """

    with open('files/valentina.jpg.', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.teacher_Valentina, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=teachers_kb)
    await call.answer()

async def teacher_Aleksandra(call):
    """
    Функция для кнопки inline клавиатуры 'Кялина Александра Семеновна'. Открывает файл - фото.
    Создает переменную mes для подготовки ответа - фото + текст с описанием texts.teacher_Aleksandra.
    Отправляет сообщение с переменной mes.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + фото преподавателя + inline клавиатура
    """

    with open('files/aleksandra.jpg.', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.teacher_Aleksandra, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=teachers_kb)
    await call.answer()

async def teacher_Vaselina(call):
    """
    Функция для кнопки inline клавиатуры 'Алексахина Васелина Игоревна''. Открывает файл - фото.
    Создает переменную mes для подготовки ответа - фото + текст с описанием texts.teacher_Vaselina.
    Отправляет сообщение с переменной mes.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + фото преподавателя + inline клавиатура
    """

    with open('files/vaselina.jpg.', "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.teacher_Vaselina, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=teachers_kb)
    await call.answer()

async def dance_styles(message):
    """
    Функция для кнопки reply клавиатуры '📌 Танцевальные направления'.
    Отправляет сообщение с предложением выбрать танцевальное направление из inline клавиатуры dance_styles_kb.

    :param message: Сообщение от пользователя - нажатие кнопки reply клавиатуры
    :return: Ответ пользователю - текст + inline клавиатура
    """

    await message.answer('<b>Выберите стиль ⬇️⬇️⬇️</b>', parse_mode='HTML', reply_markup=dance_styles_kb)


async def hip_hop(call):
    """
    Функция для кнопки inline клавиатуры 'Hip-hop'. Открывает файл - видео.
    Создает переменную mes для подготовки ответа - видео + текст с описанием texts.hip_hop.
    Отправляет сообщение с переменной mes.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + видео танцевального направления + inline клавиатура
    """

    with open('files/video/hip-hop.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.hip_hop, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()


async def krump(call):
    """
    Функция для кнопки inline клавиатуры 'Krump'. Открывает файла - видео.
    Создает переменную mes для подготовки ответа - видео + текст с описанием texts.krump.
    Отправляет сообщение с переменной mes.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + видео танцевального направления + inline клавиатура
    """

    with open('files/video/krump.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.krump, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()

async def afro(call):
    """
    Функция для кнопки inline клавиатуры 'Afro'. Открывает файл - видео.
    Создает переменную mes для подготовки ответа - видео + текст с описанием texts.afro
    Отправляет сообщение с переменной mes.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + видео танцевального направления + inline клавиатура
    """

    with open('files/video/afro.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.afro, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()

async def k_pop(call):
    """
    Функция для кнопки inline клавиатуры 'K-pop'. Открывает файл - видео.
    Создает переменную mes для подготовки ответа - видео + текст с описанием texts.k_pop.
    Отправляет сообщение с переменной mes.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + видео танцевального направления + inline клавиатура
    """

    with open('files/video/k-pop.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.k_pop, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()

async def high_heels(call):
    """
    Функция для кнопки inline клавиатуры 'High Heels'. Открывает файл - видео.
    Создает переменную mes для подготовки ответа - видео + текст с описанием texts.high_heels.
    Отправляет сообщение с переменной mes.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + видео танцевального направления + inline клавиатура
    """

    with open('files/video/high_heels.mp4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.high_heels, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()

async def waacking(call):
    """
    Функция для кнопки inline клавиатуры 'Waacking'. Открывает файл - видео.
    Создает переменную mes для подготовки ответа - видео + текст с описанием texts.waacking.
    Отправляет сообщение с переменной mes.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю - текст + видео танцевального направления + inline клавиатура
    """

    with open('files/video/wacking.MP4', "rb") as vid:
        mes = InputMediaVideo(media=vid, caption=texts.waacking, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=dance_styles_kb)
    await call.answer()


async def schedule(message):
    """
    Функция для кнопки reply клавиатуры '📌 Расписание занятий'. Открывает файл - картинка.
    Отправляет сообщение с картинкой (таблица) и описанием texts.schedule.

    :param message: Сообщение от пользователя - нажатие кнопки reply клавиатуры
    :return: Ответ пользователю - текст + картинка (таблица - расписание)
    """

    with open('files/schedule.png', "rb") as img:
        await message.answer_photo(img, texts.schedule, parse_mode='HTML', reply_markup=start_kb1)

async def cost(message):
    """
    Функция для кнопки reply клавиатуры '📌 Стоимость абонементов'. Открывает файл - картинка.
    Отправляет сообщение с картинкой (таблица) и описанием texts.cost.

    :param message: Сообщение от пользователя - нажатие кнопки reply клавиатуры
    :return: Ответ пользователю - текст + картинка (таблица - стоимость абонементов)
    """

    with open('files/cost.png', "rb") as img:
        await message.answer_photo(img, texts.cost, parse_mode='HTML', reply_markup=start_kb1)

async def contacts(message):
    """
    Функция для кнопки reply клавиатуры '📌 Наши контакты'.
    Отправляет сообщение с описанием texts.contacts.

    :param message: Сообщение от пользователя - нажатие кнопки reply клавиатуры
    :return: Ответ пользователю - текст с ссылками на сообщество Вк и контакты преподавателей
    """

    await message.answer(texts.contacts, parse_mode='HTML', reply_markup=start_kb1)

async def location(message):
    """
    Функция для кнопки reply клавиатуры '📌 Наша локация и залы'. Открывает файл - фото.
    Отправляет сообщение с фото и описанием texts.location

    :param message: Сообщение от пользователя - нажатие кнопки reply клавиатуры
    :return: Ответ пользователю - текст + картинка
    """

    with open('files/halls.jpg', "rb") as img:
        await message.answer_photo(img, texts.location, parse_mode='HTML', reply_markup=start_kb1)

async def trophies(message):
    """
    Функция для кнопки reply клавиатуры '📌 Наши достижения'. Открывает файл - фото.
    Отправляет сообщение с фото и описанием texts.trophies.

    :param message: Сообщение от пользователя - нажатие кнопки reply клавиатуры
    :return: Ответ пользователю - текст + картинка
    """

    with open('files/trophies.jpg', "rb") as img:
        await message.answer_photo(img, texts.trophies, parse_mode='HTML', reply_markup=start_kb1)



class SignUp(StatesGroup):
    """
    Класс SignUp для машины состояний, наследованный от StatesGroup для записи на первое пробное занятие.
    Создает переменные для состояний.

    Attributes
    ----------
    name: Сохранение имени пользователя
    age: Сохранение возраста пользователя
    style: Сохранение танцевального стиля, который заинтересовал пользователя
    date: Сохранение даты посещения первого пробного занятия

    Methods
    -------
    sign_up(message)
        Отправляет пользователю сообщение с просьбой указать свою фамилию и имя.
        Сохраняет полученную информацию от пользователя с помощью состояния SignUp.name.set().
    sign_up1(message, state)
        Добавляет состояние SignUp.name.set() в словарь data.
        Отправляет пользователю сообщение с просьбой указать свой возраст.
        Сохраняет полученную информацию от пользователя с помощью состояния SignUp.age.set().
    sign_up2(message, state)
        Добавляет состояние SignUp.age.set() в словарь data.
        Отправляет пользователю сообщение с просьбой указать понравившийся танцевальный стиль.
        Сохраняет полученную информацию от пользователя с помощью состояния SignUp.style.set().
    sign_up3(message, state)
        Добавляет состояние SignUp.style.set() в словарь data.
        Открывает файл - расписание.
        Отправляет пользователю сообщение с файлом - расписание и просьбой указать дату для первого занятия.
        Сохраняет полученную информацию от пользователя с помощью состояния SignUp.date.set().
    sign_up4(message, state)
        Добавляет состояние SignUp.style.set() в словарь data.
        Получает все значения из словаря data. С помощью цикла перебирает всех администраторов и отправляет им
        уведомление о записи на занятие. Сохраняет информацию о записи на занятие в базу данных.
        Отправляет пользователю сообщение с текстом (в тексте указана информация на какую дату записался пользователь).
        Завершает машину состояний state.finish().
    """

    name = State()
    age = State()
    style = State()
    date = State()


async def sign_up(message: types.Message):
    """
    Функция для получения информации от пользователя о фамилии, имени. Создает переменную с инструкцией.
    Отправляет сообщение пользователю с инструкцией. Получает состояние SignUp.name.set() - информация от пользователя.

    :param message: Сообщение от пользователя
    :return: Ответ пользователю, получение состояния SignUp.name.set()
    """

    instructions = ("Первое пробное занятие - <b>бесплатно</b>\n"
                    "Введите свою фамилию и имя:")
    await message.answer(instructions, parse_mode="HTML")
    await SignUp.name.set()


async def sign_up1(message: types.Message, state):
    """
    Функция для получения информации от пользователя о возрасте. Добавляет состояние name в словарь data.
    Создает переменную с инструкцией. Отправляет сообщение с инструкцией. Получает состояния SignUp.age.set().

    :param message: Сообщение от пользователя
    :param state: Состояние SignUp.name.set()
    :return: Ответ пользователю, получение состояния SignUp.age.set()
    """

    await state.update_data(name=str(message.text))

    instructions = "Введите свой возраст:"
    await message.answer(text=instructions)
    await SignUp.age.set()

async def sign_up2(message: types.Message, state):
    """
    Функция для получения информации от пользователя о заинтересовавшем танцевальном стиле.
    Добавляет состояние age в словарь data. Создает переменную с инструкцией.
    Отправляет сообщения с инструкцией. Получает состояние SignUp.style.set().

    :param message: Сообщение от пользователя
    :param state: Состояние SignUp.age.set()
    :return: Ответ пользователю, получение состояния SignUp.style.set()
    """

    await state.update_data(age=str(message.text))

    instructions = "Введите танцевальный стиль, который Вас заинтересовал:"
    await message.answer(text=instructions)
    await SignUp.style.set()

async def sign_up3(message: types.Message, state):
    """
    Функция для получения информации от пользователя о дате посещения первого пробного занятия.
    Добавляет состояние style в словарь data. Открывает файл "расписание". Создает переменную с инструкцией.
    Отправляет сообщение с инструкцией и файлом "расписание". Сохраняет состояние SignUp.date.set().

    :param message: Сообщение от пользователя
    :param state: Состояние SignUp.style.set()
    :return: Ответ пользователю, получение состояния SignUp.date.set()
    """

    await state.update_data(style=str(message.text))

    with open('files/schedule.png', "rb") as img:
        instructions = ("Введите дату, когда посетите пробное занятие в формате <i>'12 декабря'</i>\n "
                        "При выборе даты, пожалуйста, ориентируйтесь на расписание занятий нужной Вам группы")
        await message.answer_photo(img, instructions, parse_mode="HTML")
    await SignUp.date.set()

async def sign_up4(message, state):
    """
    Функция для отправки уведомления о записи на первое пробное занятие администраторам и для отправки пользователю
    сообщения об успешной записи на дату. Импортирует бота из файла main. Добавляет состояние date в словарь data.
    Создает переменную словаря data, получает все состояния state.get_data().
    Создает переменную username, получает имя пользователя.
    Создает переменную администраторов, получает списое администраторов из файла config.
    Создает цикл для перебора списка администраторов.
    Пока id == id администраторов, отправляет уведомление администраторам о записи на первое пробное занятие.
    Создает исключение в случае ошибки. Отвечает пользователю - информация о записи на первое пробное занятие с датой
    Создает переменную id, получает id пользователя.
    Добавляет в базу данных информации о записи на первое пробное занятие. Завершает машину состояний.

    :param message: Сообщение от пользователя
    :param state: Состояние SignUp.date.set()
    :return: Уведомление администраторам о записи, ответ пользователю об успешной записи на дату, добавление информации
    в базу данных
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
    Функция для кнопки reply клавиатуры '📌 Админ панель'. Отправляет сообщение с предложением выбрать действие из
    inline клавиатуры AdminPanel.

    :param message: Сообщение от пользователя (администратора) - нажатие кнопки reply клавиатуры
    :return: Ответ пользователю с предложением выбрать действие + inline клавиатура
    """

    await message.answer('<b>Вы открыли панель администратора. Выберите действие ⬇️⬇️⬇️</b>', parse_mode='HTML', reply_markup=AdminPanel)


async def statistick(call: types.CallbackQuery):
    """
    Функция для кнопки inline клавиатуры '📊 Статистика'. Отправляет сообщение с подсчетом количества пользователей.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю с информацией о подсчете количества пользователей
    """

    await call.message.edit_text(texts.statistick(int(database.count())), parse_mode="HTML", reply_markup=back_to_admin)
    await call.answer()

async def back_admin(call: types.CallbackQuery):
    """
    Функция для кнопки inline клавиатуры '🔙 Назад'. Возвращает пользователя в панель администратора.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю с сообщением и inline клавиатурой
    """

    await call.message.edit_text('<b>Вы открыли панель администратора. Выберите действие ⬇️⬇️⬇️</b>', parse_mode='HTML', reply_markup=AdminPanel)
    await call.answer()

async def users(call: types.CallbackQuery):
    """
    Функция для кнопки inline клавиатуры '👥 Пользователи'. Отправляет сообщение со списком пользователей из
    базы данных, таблица users - id, username.

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю с информацией о пользователях из базы данных - id, username
    """

    await call.message.edit_text(f'<pre>{database.get_all()}</pre>', parse_mode="HTML", reply_markup=back_to_admin)
    await call.answer()



class admins(StatesGroup):
    """
    Класс admins для машины состояний, наследованный от StatesGroup для рассылки информации пользователям

    Attributes
    ----------
    mailing_step1: Сохранение текста для рассылки
    mailing_step2: Сохранение файла для рассылки

    Methods
    -------
    mailing(call)
        Отправляет пользователю - администратору сообщение с просьбой ввести текст рассылки, для отмены предлагает
        нажать команду /cancel. Получает ответ от пользователя admins.mailing_step1.set().
    mailing1(message, state)
        Сохраняет информацию полученную от пользователя в словарь data. Если пользователь выбрал команду /cancel,
        возвращает пользователя в панель администратора. Если пользователь ввел текст сообщения, отправляет сообщение с
        просьбой прикрепить фотографию. Получает ответ от пользователя admins.mailing_step2.set().
    mailing2(message, state)
        Сохраняет полученное фото в директорию files. Получает информацию со словаря data. Отправляет всем пользователям
        рассылку. Отправляет сообщение администратору об успешной рассылке и статистику об отправленных сообщениях.
    """

    mailing_step1 = State()
    mailing_step2 = State()


async def mailing(call: types.CallbackQuery):
    """
    Функция для получения текста рассылки от пользователя-администратора. Создает переменную с инструкцией.
    Отправляет сообщение с инструкцией. Получает состояние admins.mailing_step1.set()

    :param call: Выбор кнопки inline клавиатуры пользователем
    :return: Ответ пользователю с предложением отменить действие или ввести текст сообщения для рассылки,
    получение состояния admins.mailing_step1.set()
    """

    instructions = ("Для отмены, нажмите кнопку <b>/cancel</b>\n"
                    "Введите текст сообщения:")
    await call.message.answer(instructions, parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    await call.answer()
    await admins.mailing_step1.set()


async def mailing1(message, state):
    """
    Функция для получения файла для рассылки. Добавляет состояние mailing_step1 в словарь data.
    Добавляет команду /cancel для отмены создания рассылки.
    Отвечает пользователю и возвращает в панель администратора, если выбрана команда /cancel.
    Завершает машину состояний. Если не выбрана команда /cancel, создает переменную с инструкцией.
    Отправляет сообщение с инструкцией. Сохраняет состояние admins.mailing_step2.set().

    :param message: Сообщение от пользователя-администратора
    :param state: Состояние admins.mailing_step1.set()
    :return: В случае выбора команды /cancel, возврат в панель администратора. В случае текста рассылки, отправка
    пользователю сообщения с просьбой прикрепить фотографию, получение состояния admins.mailing_step1.set()
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
    Функция для сохранения файла, рассылки информации всем пользователям из базы данных,
    ответа администратору об успешной рассылке и статистике. Импортирует бота с файла main.
    Сохраняет полученное фото в директорию files. Создает переменную словаря data,
    получает все состояния state.get_data(). Создает переменную subscribers, получает из базы данных таблицы
    users id всех пользователей. Создает счетчик "c = 0". Создает цикл перебора всех пользователей в списке subscribers.
    Открывает сохраненное фото. Отправляет сообщение всем пользователям с фото и описанием, полученного из словаря data
    Создает исключение. Отправляет сообщение администратору с текстом об успешной рассылке иколичеством отправленных
    сообщений на основании количества пользователей в базе данных. Завершает машину состояний.

    :param message: Сообщение от пользователя-администратора
    :param state: Состояние admins.mailing_step2.set()
    :return: Рассылка пользователям, уведомление администарторов об успешной рассылке и статистике
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







