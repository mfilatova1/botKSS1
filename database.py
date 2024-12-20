"""
Модуль database.py.
Модуль подключается к базе данных, создает таблицы. В модуле расположены функции для работы с таблицами базы данных.
"""

import sqlite3

#Подключение к базе данных
conn = sqlite3.connect('database.db')
cur = conn.cursor()
#создание таблицы users
cur.execute("CREATE TABLE IF NOT EXISTS users(id INT, username TEXT); ")


def add(id, username):
    """
    Функция добавления пользователей в таблицу users. Проверяет есть ли пользователь в таблице, если есть
    не добавляет пользователя. В ином случае добавляет пользователя в таблицу users.

    :param id: id пользователя
    :param username: username пользователя
    :return: Добавление пользователя в таблицу users
    """

    if (id,) in get_id(): return
    cur.execute("INSERT INTO users (id, username) VALUES (?, ?)", (f'{id}', f'{username}'))
    conn.commit()

def get_all():
    """
    Функция получения пользователей из таблицы users. Создает переменную s, получает всех пользователей, сохраняет их,
    возвращает переменную полученных пользователей из таблицы users

    :return: Все пользователи из таблицы users
    """

    s = cur.execute("SELECT * FROM users;").fetchall()
    conn.commit()
    return s

def count():
    """
    Функция подсчета количества пользователей. Создает переменную s , подсчитывает всех пользователей, сохраняет
    результат, возвращает информацию из переменной

    :return: Количество пользователей из таблицы users
    """

    s = cur.execute("SELECT COUNT(*) FROM users;").fetchone()
    conn.commit()
    return s[0]

def get_id():
    """
    Функция получения id пользователей. Создает переменную s , получает id всех пользователей, сохраняет результат,
    возвращает ифнормацию из переменной

    :return: Id пользователей из таблицы users
    """

    s = cur.execute("SELECT id FROM users;").fetchall()
    conn.commit()
    return s

#создание таблицы sign_up
cur.execute("CREATE TABLE IF NOT EXISTS sign_up(id INT, username TEXT, name TEXT, age TEXT, style TEXT, date TEXT); ")

def add1(id, username, name, age, style, date):
    """
    Функция добавления информации о записи на первое пробное занятие в таблицу sign_up/
    Добавляет информаци. о записи на первое пробное занятие в таблицу sign_up. Сохраняет информацию.

    :param id: id пользователя
    :param username: username пользователя
    :param name: имя пользователя
    :param age: возраст пользователя
    :param style: танцевальный стиль, заинтересовавший пользователя
    :param date: дата записи на занятие
    :return: Добавление информации о записи на занятие в таблицу sign_up
    """
    cur.execute("INSERT INTO sign_up (id, username, name, age, style, date) "
                "VALUES (?, ?, ?, ?, ?, ?)", (f'{id}', f'{username}', f'{name}', f'{age}', f'{style}', f'{date}'))
    conn.commit()

