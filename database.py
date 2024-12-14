import sqlite3

#Подключение к базе данных
conn = sqlite3.connect('database.db')
cur = conn.cursor()
#создание таблицы users
cur.execute("CREATE TABLE IF NOT EXISTS users(id INT, username TEXT); ")


def add(id, username):
    """
    Функция добавления пользователей в таблицу users
    - Проверка есть ли пользователь в таблице, если есть не добавлять
    - В ином случае добавление пользователя в таблицу
    """
    if (id,) in get_id(): return
    cur.execute("INSERT INTO users (id, username) VALUES (?, ?)", (f'{id}', f'{username}'))
    conn.commit()

def get_all():
    """
    Функция получение пользователей из таблицы users
    - Создание переменной, получение всех пользователей
    - Сохранение
    - Возврат переменной
    """
    s = cur.execute("SELECT * FROM users;").fetchall()
    conn.commit()
    return s

def count():
    """
    Функция подсчета количества пользователей
    - Создание переменной, подсчет всех пользователей
    - Сохранение
    - Возврат переменной
    """
    s = cur.execute("SELECT COUNT(*) FROM users;").fetchone()
    conn.commit()
    return s[0]

def get_id():
    """
    Функция получения id пользователей
    - Создание переменной, получение id
    - Сохранение
    - Возврат переменной
    """
    s = cur.execute("SELECT id FROM users;").fetchall()
    conn.commit()
    return s

#создание таблицы sign_up
cur.execute("CREATE TABLE IF NOT EXISTS sign_up(id INT, username TEXT, name TEXT, age TEXT, style TEXT, date TEXT); ")

def add1(id, username, name, age, style, date):
    """
    Функция добавления информации о записи на первое пробное занятие в таблицу sign_up
    - Добавление информации о записи на первое пробное занятие в таблицу
    - Сохранение
    """
    cur.execute("INSERT INTO sign_up (id, username, name, age, style, date) "
                "VALUES (?, ?, ?, ?, ?, ?)", (f'{id}', f'{username}', f'{name}', f'{age}', f'{style}', f'{date}'))
    conn.commit()

