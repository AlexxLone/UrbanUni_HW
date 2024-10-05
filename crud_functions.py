import sqlite3


def convert_to_blob(filename):
    try:
        with open(filename, 'rb') as file:
            blob = file.read()
        return blob
    except IOError as err:
        print(f'Error reading file {filename}:\n{err}')
        return False


def prod_db_insert(cursor, title, price, description, photo_file):  # insert new line into production db
    insert_query = '''INSERT INTO Products (title, price, description, photo) VALUES (?, ?, ?, ?)'''
    # if having any problems with image convertion write without it
    photo_binary = None
    photo = convert_to_blob(photo_file)
    if photo:
        photo_binary = sqlite3.Binary(photo)
    insert_data = (title, price, description, photo_binary)
    cursor.execute(insert_query, insert_data)


# Наполнение БД (тему управления БД можно было бы развить, есть широкое поле для наполнения функционалом)
# Тут - заполнение БД из файлов в текущей директории дабы не уходить далеко от сути ДЗ
# количество нумерация файлов должно соответствовать входящим данным start stop
# Имена файлов с описаниями задаются как Prod{i}.txt
# сам файл должен содержать строки:
#   1-я - Наименование;
#   2-я - Цена;
#   3-я и все последующие - описание товара.
# Имена файлов с изображениями - Prod{i}.jpg

def initiate_db(start, stop):
    try:
        connection = sqlite3.connect("TG_Healthy_Bot.db")
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        price INTEGER NOT NULL,
        description TEXT,
        photo BLOB
        )
        ''')

        for i in range(start, stop + 1):
            try:
                with open(f'Prod{i}.txt', 'rt', encoding='utf-8') as file:
                    db_line = []  # parameters for prod_db_insert function
                    db_line.append(file.readline())
                    db_line.append(file.readline())
                    db_line.append(file.read())
            except FileNotFoundError as err1:
                print(err1)
            except UnicodeDecodeError as err2:
                print(err2)
            else:
                db_line.append(f'Prod{i}.jpg')
                prod_db_insert(cursor, *db_line)
        connection.commit()
    except sqlite3.Error as sql3err:
        print(sql3err)
        connection.rollback()
    finally:
        if connection:
            connection.close()


def get_all_products():
    with sqlite3.connect("TG_Healthy_Bot.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Products")
    return cursor.fetchall()


if __name__ == '__main__':
    initiate_db(1, 4)
