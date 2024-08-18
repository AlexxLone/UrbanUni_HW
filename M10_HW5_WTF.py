# Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.
#
# Задача "Многопроцессное считывание":
# Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
# Подготовка:
# Скачайте архив с файлами для считывания данных и распакуйте его в проект для дальнейшего использования.
# Выполнение:
# Создайте функцию read_info(name), где name - название файла. Функция должна:
# Создавать локальный список all_data.
# Открывать файл name для чтения.
# Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
# Во время считывания добавлять каждую строку в список all_data.
# Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
# Создайте список названий файлов в соответствии с названиями файлов архива.
# Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль
# Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with
# и объект Pool. Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов.
# Измерьте время выполнения и выведите его в консоль.
# Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
# предварительно закомментировав другой.

from datetime import datetime
import multiprocessing
from time import sleep

all_data, all_data_mono, all_data_multi = [], [], []
files_path = 'C:/Temp/'  # директория с рабочими файлами
file_name_list = [f'./file {number}.txt' for number in range(1, 5)]  # список имен рабочих файлов
file_list = [files_path + f for f in file_name_list]


def read_info(filename):
    with open(filename, 'r', encoding='UTF-8') as file_:
        for line in file_:
            all_data.append(line)


if __name__ == '__main__':

    start_mono = datetime.now()
    for file in file_list:
        read_info(file)
    end_mono = datetime.now()
    print(f'В линейном режиме чтение данных заняло: {end_mono - start_mono}')

    all_data_mono, all_data = all_data, []

    start_multi = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_list)
    end_multi = datetime.now()
    print(f'В многопроцессорном режиме чтение данных заняло: {end_multi - start_multi}')
    print(all_data)

    # sleep(10)
    all_data_multi, all_data = all_data, []
    # print(len(all_data_mono))
    # print(len(all_data_multi))

    print('Сравнение полученных данных:')
    differ = False
    if len(all_data_mono) != len(all_data_multi):
        print('Полученные списки различной длинны!')
        differ = True
    else:
        for i in range(len(all_data_mono)):
            if all_data_mono[i] != all_data_multi[i]:
                print(f'Отличие! элементы №{i}: {all_data_mono[i]} vs {all_data_multi[i]}')
                differ = True
    if differ is False:
        print('Отличий нет')
