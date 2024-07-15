# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
#
# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут
# file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
# Алгоритм получения словаря такого вида в методе get_all_words:
# Создайте пустой словарь all_words.
# Переберите названия файлов и открывайте каждый из них, используя оператор with.
# Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
# Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
# (тире обособлено пробелами, это не дефис в слове).
# Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
# В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
#
# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
# позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
# количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла
# и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться
# методом словаря - item().

import os
from datetime import datetime


class WordsFinder:
    # немного усложняю задачу - буду сохранять не только имена файлов по ТЗ (file_names),
    # но и дату их создания на момент вызова в методе check_init
    work_file_list = dict()  # "имя_файла":время_последней_модификации
    all_words = dict()
    # перечень возможных разделителей в файле (к удалению)
    sep_list = [',', '.', '=', '!', '?', ';', ':', '\n', '\t']

    # случай с ' - ' рассматривается отдельной проверкой дабы только ради него не вводить проверку вхождения строк

    def __init__(self, *file_list):
        self.check_init(*file_list)
        self.current_state()
        # self.get_all_words()  # заполняем искомый словарь результатами вычислений на момент инициализации

    def check_init(self, *file_list):
        for file_name in file_list:
            try:
                m_time = os.path.getmtime(file_name)
            except FileNotFoundError:
                print(f'\033[31mФайл "{file_name}" не найден!\033[0m')
            else:
                self.work_file_list.update({file_name: m_time})
            finally:
                pass

    def current_state(self):
        print(f'\033[34mПеречень файлов и даты их модификации на момент создания экземпляра класса:\033[0m')
        for key, value in self.work_file_list.items():
            print(f'\t{key}: {datetime.fromtimestamp(value)}')

    def get_all_words(self):
        print(f'\033[34mРабочий словарь формата {{"Имя_файла": ["слова"]}}. '
              f'"слово" без разделяющих знаков, в нижнем регистре:\033[0m')
        file_list = self.work_file_list.keys()
        for file_name in file_list:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    all_file_words = str()
                    # по сути - строка, в которую мы построчно добавляем содержимое нашего файла,
                    # выполняя необходимые преобразования.
                    for line in file:
                        # работаем с файлом построчно, дабы не вгонять весь файл в список в случае большого файла
                        line = list(line)
                        # далее работаем со списком, созданным из строки, проверяем список посимвольно
                        # убираем все символы - разделители и частный случай ' - '
                        for i in range(len(line)):
                            if line[i] in self.sep_list or (line[i] == '-' and ''.join(line[i - 1:i + 2]) == ' - '):
                                line[i] = ' '
                            line[i] = line[i].lower()
                            # коли и так работаем в цикле посимвольно - переводим в нижний регистр
                        all_file_words += ''.join(line)
                    self.all_words.update({file_name: (all_file_words.split())})
            except UnicodeDecodeError:
                print(f'\033[31mФайл "{file_name}" не в формате UTF-8! Не добавлен к поиску.\033[0m')
        return self.all_words

    def find(self, word):  # поиск первого вхождения
        # проверить бы актуальность данных в словаре на момент вызова.
        # мало ли, может между инициализацией и этим вызовом прошло много времени и файл поменяли
        # допишу позже
        print(f'\033[34mПоиск первого вхождения слова {word} в рабочий словарь в разрезе файлов:\033[0m')
        result = dict()
        for name, words in self.all_words.items():
            try:
                result.update({name: (words.index(word.lower()) + 1)})
            except ValueError:
                result.update({name: 'not found'})
        return result

    def count(self, word):
        print(f'\033[34mПодсчет вхождения слова {word} в рабочий словарь в разрезе файлов (без учета регистра):\033[0m')
        result = dict()
        for name, words in self.all_words.items():
            result.update({name: words.count(word.lower())})
        return result


finder2 = WordsFinder('a.txt', 'test_file_7_3.txt', 'репка.txt', 'test.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
