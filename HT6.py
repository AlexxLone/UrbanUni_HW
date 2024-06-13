# ДЗ по словарям
my_dict = {'Алексей': 1975, 'Валентина': 1951, 'Анастасия': 1974, 'Арсений': 2003}
print('Словарь с именами в качестве ключей и годами рождения соответствующих персон:')
print(my_dict)
print('ГР Арсения:', my_dict['Арсений'])
# print (my_dict['Павел']) # Ошибка - обращение к несуществующему ключу
current_key = input("Введите ключ поиска: ")
print(current_key, ': ', my_dict.get(current_key, 'такого ключа не существует в словаре'), sep='')
my_dict.update({'Павел': 1988, "Ксения": 1998})
Stasy_BD = my_dict.pop('Анастасия')
print('ГР Анастасии: ', Stasy_BD, '. Запись удалена!', sep='')
print('Обновленный словарь: \n', my_dict, sep='')
# ДЗ на множества. Создадим для начала список с повторяющимися значениями, затем преобразуем его во множество
my_list = ['circle', 3.1416, 2.718, "Newton", (1.618, 2.718, 3.1416), 1.618, 2.718, 3.1416]
# повторяющиеся значения списка - 3.1416, 2.718
print('My list:\n', my_list, sep='')
my_set = set(my_list)
print("My set:\n", my_set, sep='')
# после преобразования во множество порядок абсолютно не предскадуем (или все же есть какая-то закономерность?...)
my_set = my_set | {9.8, 'm/s^2'}  # добавляем 2-а новых значения в множество
print("My new set. Two elements added:\n", my_set, sep='')
# print(my_set.remove('Archimedes')) # ошибка удаления отсутствующего значения
print('Trying to delete unpresented Archimedes from set: ', my_set.discard('Archimedes'))
# метод discard не вызывает ошибки удаления отсутствующего значения
my_set.remove((1.618, 2.718, 3.1416))  # удалим кортеж из множества
print('My new set. Tuple in set deleted:\n', my_set, sep='')

