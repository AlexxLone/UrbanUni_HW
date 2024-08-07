# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое чиcло number и подсчитывает произведение ц
# ифр этого числа.
#
# Пункты задачи:
# Напишите функцию get_multiplied_digits и параметр number в ней.
# Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
# Основной задачей будет отделение первостоящей цифры в числе:
# создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
# Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
# Таким образом вы умножите первую цифру числа на результат работы этой же функции c числом, но уже без первой цифры.
# 4 пункт можно выполнить только тогда, когда длина str_number больше 1,
# т.к. в противном случае не получиться взять срез str_number[1:].
# Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
# Стек вызовов будет выглядеть следующим образом:
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0:1:])
    if len(str_number) > 1:
        first = first * get_multiplied_digits(int(str_number[1::]))
    return first


result = get_multiplied_digits(40203)
print(result)
