import os
import time


# from datetime import datetime

# print(os.name)
# print(os.environ)
# print(os.getenv("TMP"))
# print(os.getcwd())
# os.startfile("репка.txt")
# # print(os.path.exists("C:\Users\Alexx_ADM\PycharmProjects\UrbanUni_HT"))
# print(os.path.exists("C:/Users/Alexx_ADM/PycharmProjects/UrbanUni_HT"))
# print(os.listdir(os.getcwd()))
# print(os.walk(os.getcwd()))

def formatted_time(full_path): # получение по полному пути даты модификации файла/папки в читаемом формате
    return time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(full_path)))


def formatted_list(root, directories, files):
    print(f'..Головная директория: \033[31m{root}:\033[0m')
    for directory in directories:
        full_path = os.path.join(root, directory)
        print(f'\tПапка: \033[33m{directory}\033[0m | modified: {formatted_time(full_path)}')
    for file in files:
        full_path = os.path.join(root, file)
        # вариант без преобразования формата вывода даты/времени:
        # print(f'{full_path} | modified: {datetime.fromtimestamp(os.path.getmtime(full_path))}')
        print(f'\tФайл: \033[34m{file}\033[0m | size: {os.path.getsize(full_path)} byte | '
              f'modified: {formatted_time(full_path)}')


def list_dir(dir_to_work):  # результат только для текущей папки:
    work_dir_list = os.walk(dir_to_work)
    root, directories, files = next(work_dir_list)
    formatted_list(root, directories, files)


def list_tree(dir_to_work):  # результат для текущей и всех вложенных папок и файлов:
    work_dir_list = os.walk(dir_to_work)
    for root, directories, files in work_dir_list:
        formatted_list(root, directories, files)


work_dir = os.getcwd()

print(f'\033[36mСОДЕРЖИМОЕ ТЕКУЩЕЙ ПАПКИ И ВСЕХ ВЛОЖЕННЫХ:\033[0m')
list_tree(work_dir)

print(f'\033[36mСОДЕРЖИМОЕ ТЕКУЩЕЙ ПАПКИ:\033[0m')
list_dir(work_dir)
