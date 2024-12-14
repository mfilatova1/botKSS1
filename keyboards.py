
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



start_kb1= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '📌 О нас'),
            KeyboardButton(text = '📌 Наши преподаватели'),
        ],
        [   KeyboardButton(text = '📌 Танцевальные направления'),
            KeyboardButton(text = '📌 Расписание занятий'),
        ],
        [
            KeyboardButton(text='📌 Стоимость абонементов'),
            KeyboardButton(text='📌 Записаться на занятие')
        ],
        [
            KeyboardButton(text = '📌 Наши контакты'),
            KeyboardButton(text = '📌 Наша локация и залы'),

        ],
        [
            KeyboardButton(text='📌 Наши достижения')
        ]

    ], resize_keyboard=True, one_time_keyboard=True,
)

start_kb2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '📌 О нас'),
            KeyboardButton(text = '📌 Наши преподаватели'),
        ],
        [   KeyboardButton(text = '📌 Танцевальные направления'),
            KeyboardButton(text = '📌 Расписание занятий'),
        ],
        [
            KeyboardButton(text='📌 Стоимость абонементов'),
            KeyboardButton(text='📌 Записаться на занятие')
        ],
        [
            KeyboardButton(text = '📌 Наши контакты'),
            KeyboardButton(text = '📌 Наша локация и залы'),

        ],
        [
            KeyboardButton(text='📌 Наши достижения'),
            KeyboardButton(text='📌 Админ панель')
        ]
    ], resize_keyboard=True, one_time_keyboard=True, row_width=1
)


teachers_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Шапошникова Анастасия Васильевна', callback_data = 'Шапошникова Анастасия Васильевна'),
        ],
        [
            InlineKeyboardButton(text = 'Карпова Валентина Алексеевна', callback_data = 'Карпова Валентина Алексеевна'),
        ],
        [
            InlineKeyboardButton(text='Кялина Александра Семеновна', callback_data='Кялина Александра Семеновна'),
        ],
        [
            InlineKeyboardButton(text='Алексахина Васелина Игоревна', callback_data='Алексахина Васелина Игоревна'),
        ],

    ]
)

dance_styles_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Hip-hop', callback_data = 'Hip-hop'),
        ],
        [
            InlineKeyboardButton(text = 'Krump', callback_data = 'Krump'),
        ],
        [
            InlineKeyboardButton(text = 'Afro', callback_data = 'Afro'),
        ],
[
            InlineKeyboardButton(text = 'K-pop', callback_data = 'K-pop'),
        ],
        [
            InlineKeyboardButton(text = 'High Heels', callback_data = 'High Heels'),
        ],
        [
            InlineKeyboardButton(text='Waacking', callback_data='Waacking'),
        ],
    ]
)

AdminPanel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Пользователи", callback_data = "users"),
        ],
        [
            InlineKeyboardButton(text="📊 Статистика", callback_data = "statistick"),
        ],
        [
            InlineKeyboardButton(text="✉️ Рассылка", callback_data = "mailing"),
        ],
    ]
)

back_to_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data = "back_to_admin"),
        ],
    ]
)








