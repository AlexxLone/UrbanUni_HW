# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел
# среди 3-х введённых.
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0
first = int(input('Input first integer value: '))
second = int(input('Input second integer value: '))
third = int(input('Input third integer value: '))
# дабы избежать повторных вычислений в условиях - для начала вычислим булевы переменные равенства каждой пары чисел:
_1st_eq_2nd = (first == second)
_1st_eq_3rd = (first == third)
_2nd_eq_3rd = (second == third)
# print(_1st_eq_2nd, _1st_eq_3rd, _2nd_eq_3rd, )
result = int()  # результирующая переменная
if _1st_eq_2nd and _1st_eq_3rd and _2nd_eq_3rd:
    result = 3
elif _1st_eq_2nd or _1st_eq_3rd or _2nd_eq_3rd:
    result = 2
else:
    result = 0
print("Результат =", result)
