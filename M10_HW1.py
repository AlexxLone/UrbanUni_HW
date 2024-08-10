# Цель: понять как работают потоки на практике, решив задачу
#
# Задача "Потоковая запись в файлы":
# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
# после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции
# к домашнему заданию.

from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word, word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'{word} №{i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


print('Запись последовательным вызовом функций:')
func_time_start = datetime.now()
write_words('Какое-то слово', 10, 'example1.txt')
write_words('Какое-то слово', 30, 'example2.txt')
write_words('Какое-то слово', 200, 'example3.txt')
write_words('Какое-то слово', 100, 'example4.txt')
func_time_end = datetime.now()
print(f'На выполнение последовательного вызова функций затрачено: {func_time_end - func_time_start}')

print('\nЗапись в потоках:')
thread_first = Thread(target=write_words, args=('Какое-то слово', 10, 'example1.txt'))
thread_second = Thread(target=write_words, args=('Какое-то слово', 30, 'example2.txt'))
thread_third = Thread(target=write_words, args=('Какое-то слово', 200, 'example3.txt'))
thread_fourth = Thread(target=write_words, args=('Какое-то слово', 100, 'example4.txt'))

threads_time_start = datetime.now()

thread_first.start()
thread_second.start()
thread_third.start()
thread_fourth.start()

thread_first.join()
thread_second.join()
thread_third.join()
thread_fourth.join()

threads_time_end = datetime.now()
print(f'На выполнение функций в потоках затрачено: {threads_time_end - threads_time_start}')
